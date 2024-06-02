<script>
    import { onMount } from 'svelte';
    import axios from 'axios';
    let article = '';
    let prediction = '';
    let imageUrl = '';
    let error = '';

    const submitArticle = async () => {
        try {
            const response = await axios.post('http://127.0.0.1:5000/predict', { article });
            prediction = response.data.prediction;
            imageUrl = response.data.image_url;
            error = '';
        } catch (err) {
            error = 'Error: Unable to get prediction';
            prediction = '';
            imageUrl = '';
        }
    };
</script>

<style>
    body {
        font-family: Arial, sans-serif;
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
        margin: 0;
    }
    .container {
        text-align: center;
        padding: 2rem;
        max-width: 600px;
        margin: 0 auto;
        border: 1px solid #ccc;
        border-radius: 8px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    textarea {
        width: 100%;
        height: 150px;
        margin-bottom: 1.5rem;
        padding: 0.5rem;
        border: 1px solid #ccc;
        border-radius: 4px;
        font-size: 1rem;
    }
    button {
        padding: 0.75rem 1.5rem;
        background-color: #007BFF;
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 1rem;
    }
    button:hover {
        background-color: #0056b3;
    }
    .prediction {
        margin-top: 1.5rem;
        font-weight: bold;
        font-size: 1.25rem;
    }
    .error {
        color: red;
        margin-top: 1.5rem;
    }
    img {
        max-width: 100%;
        margin-top: 1.5rem;
        margin-bottom: 2rem;
        border: 2px solid #ddd;
        border-radius: 8px;
    }
    .info {
        margin-top: 0.5rem;
        font-size: 0.875rem;
        color: #555;
    }
    .image-visualization {
        margin-top: 4rem;
    }
</style>

<main>
    <div class="container">
        <h1>News Article Classifier</h1>
        <textarea bind:value={article} placeholder="Enter news article text..."></textarea>
        <button on:click={submitArticle}>Classify</button>
        <div class="info">(Please wait a few seconds for the result)</div>
        {#if prediction}
            <div class="prediction">Prediction: {prediction}</div>
            <div class="image-visualization">Image visualizing the news article:</div>
            {#if imageUrl}
                <img src={imageUrl} alt="Generated Image">
            {/if}
        {/if}
        {#if error}
            <div class="error">{error}</div>
        {/if}
    </div>
</main>
