<script>
    import { onMount } from 'svelte';
    import axios from 'axios';
    let article = '';
    let prediction = '';
    let error = '';

    const submitArticle = async () => {
        try {
            const response = await axios.post('http://127.0.0.1:5000/predict', { article });
            prediction = response.data.prediction;
            error = '';
        } catch (err) {
            error = 'Error: Unable to get prediction';
            prediction = '';
        }
    };
</script>

<style>
    body {
        font-family: Arial, sans-serif;
        padding: 2rem;
        max-width: 600px;
        margin: 0 auto;
    }
    textarea {
        width: 100%;
        height: 150px;
        margin-bottom: 1rem;
    }
    button {
        padding: 0.5rem 1rem;
        background-color: #007BFF;
        color: white;
        border: none;
        cursor: pointer;
    }
    button:hover {
        background-color: #0056b3;
    }
    .prediction {
        margin-top: 1rem;
        font-weight: bold;
    }
    .error {
        color: red;
        margin-top: 1rem;
    }
</style>

<main>
    <h1>News Article Classifier</h1>
    <textarea bind:value={article} placeholder="Enter news article text..."></textarea>
    <button on:click={submitArticle}>Classify</button>
    {#if prediction}
        <div class="prediction">Prediction: {prediction}</div>
    {/if}
    {#if error}
        <div class="error">{error}</div>
    {/if}
</main>
