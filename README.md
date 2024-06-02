# News Classification
ML2 MEP Project: News classification using an ANN and a CNN model. Frontend using Flask and Svelte to classify new articles.

## Start Application
1. Create a new env using the requirements.txt file
2. Download datasets, models, and OpenAI API key from the provided link
3. Clone the GitHub repo
4. Run Jupyter notebooks and read documentation PDFs
5. Start Flask backend: `python app.py`
6. Start Svelte frontend: `cd svelte-app`, `npm run dev`

## Explanation of Project/App
- Component 1: This project aims to classify news articles into real and fake news. More info about the motivation and ideas behind the project can be found in "1-goal-motivation.pdf".
- Component 2: Several datasets were used. More info can be found in the "2-data-collection-generation.pdf" document. The datasets are provided via an additional link because they are too large for GitHub.
- Component 3: I trained several models. The models are also provided via the additional link and more info can be found in this document: "XY"
- Component 4: Interpretation and validation is done and explained in the "4-validation-interpretation.pdf" document.
- Addition: I also created a web app for my project. The web app backend is handled by the "app.py" file and the frontend is created with the Svelte "App.svelte" file. In the frontend, there is the possibility to enter a new news article, which then will be classified as REAL or FAKE and additionally, a picture is created via text-to-image to illustrate the entered article.