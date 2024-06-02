from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import numpy as np
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI API client
openai_api_key = os.getenv('OPENAI_API_KEY')
if not openai_api_key:
    raise ValueError("No OpenAI API key found. Please set the OPENAI_API_KEY environment variable.")
client = OpenAI(api_key=openai_api_key)

# Download NLTK data
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the pre-trained model and tokenizer
model_path = './models/ann-model-v3.h5'
tokenizer_path = './models/ann-tokenizer.pkl'

try:
    model = load_model(model_path)
    with open(tokenizer_path, 'rb') as handle:
        tokenizer = pickle.load(handle)
    print("Model and tokenizer loaded successfully.")
except Exception as e:
    print(f"Error loading model or tokenizer: {e}")

# Define text preprocessing function
def process_text(text):
    text = re.sub(r'\s+', ' ', text, flags=re.I)
    text = re.sub(r'\W', ' ', str(text))
    text = re.sub(r'\s+[a-zA-Z]\s+', ' ', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.lower()
    words = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word not in stop_words]
    words = [word for word in words if len(word) > 3]
    indices = np.unique(words, return_index=True)[1]
    cleaned_text = np.array(words)[np.sort(indices)].tolist()
    return cleaned_text

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    article = data.get('article', '')
    if not article:
        return jsonify({'error': 'No article text provided'}), 400

    try:
        # Truncate the article text to 1000 characters
        if len(article) > 1000:
            article = article[:1000]

        # Process the input article
        cleaned_text = process_text(article)
        sequence = tokenizer.texts_to_sequences([cleaned_text])
        padded_sequence = pad_sequences(sequence, maxlen=150)

        # Make prediction
        prediction = model.predict(padded_sequence)
        predicted_label = np.argmax(prediction, axis=1)[0]
        label = 'REAL' if predicted_label == 1 else 'FAKE'

        # Generate image using OpenAI API (new API call)
        response = client.images.generate(
            prompt=article,
            n=1,
            size="256x256"
        )
        image_url = response.data[0].url

        return jsonify({'prediction': label, 'image_url': image_url})
    except Exception as e:
        print(f"Error during prediction or image generation: {e}")
        return jsonify({'error': f"Internal server error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
