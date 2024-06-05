# News Classification

**ML2 MEP Project:** News classification using an ANN and a CNN model. Frontend using Flask and Svelte to classify new articles.

## Start Application

To set up and start the application, follow these steps:

1. Create a new environment using the `requirements.txt` file.
2. Download datasets, models, and the OpenAI API key from the provided link.
3. Clone the GitHub repository.
4. Run Jupyter notebooks and read the documentation PDFs.
5. Start the Flask backend with the command: `python app.py`
6. Start the Svelte frontend: navigate to the svelte-app directory with `cd svelte-app` and then run `npm run dev`.

## Explanation of Project/App

- **Component 1:** This project aims to classify news articles into real and fake news. More information about the motivation and ideas behind the project can be found in `1-goal-motivation.pdf`.
- **Component 2:** Several datasets were used. More details can be found in `2-data-collection-generation.pdf`. The datasets are provided via an additional link because they are too large for GitHub.
- **Component 3:** I trained several models. The models are also provided via the additional link and more information can be found in `3-modeling.pdf`.
- **Component 4:** Interpretation and validation is done and explained in `4-validation-interpretation.pdf`.
- **Addition:** I also created a web app for my project. The web app backend is handled by the `app.py` file and the frontend is created with the Svelte `App.svelte` file. In the frontend, there is the possibility to enter a new news article, which then will be classified as REAL or FAKE and additionally, a picture is created via text-to-image to illustrate the entered article.

The folders `/models`, `/raw-data`, and the file `.env` can be downloaded via the provided link.

## Root Directory Structure

Ensure your root directory is organized as follows to run the code successfully:

news-clasification
├── .venv
├── models
├── raw-data
├── svelte-app
├── .env
├── .gitignore
├── 1-goal-motivation.pdf
├── 2-data-collection-generation.pdf
├── 2-dataset-comparison.ipynb
├── 2-dataset-generation.ipynb
├── 2-dataset-scraping.ipynb
├── 3-model-prediction.ipynb
├── 3-model-training.ipynb
├── 3-modeling.pdf
├── 4-validation-interpretation.pdf
├── app.py
├── README.md
└── requirements.txt
