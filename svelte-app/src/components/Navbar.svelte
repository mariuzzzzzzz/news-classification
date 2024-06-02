<script>
    import { Link } from 'svelte-routing';
</script>

<style>
    nav {
        display: flex;
        background-color: #333;
        padding: 1rem;
    }
    a {
        color: white;
        text-decoration: none;
        margin-right: 1rem;
    }
    a:hover {
        text-decoration: underline;
    }
</style>

<nav>
    <Link to="/">Prediction</Link>
    <Link to="/evaluation">Model Evaluation</Link>
</nav>
