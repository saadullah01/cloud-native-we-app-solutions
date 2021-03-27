<script>
	import Nav from '../components/Nav.svelte';
	import TailwindCSS from '../components/tailwindcss.svelte';
	export let segment;
</script>

<style>
	main {
		position: relative;
		max-width: 56em;
		background-color: white;
		padding: 2em;
		margin: 0 auto;
		box-sizing: border-box;
	}
</style>
<TailwindCSS />

<Nav {segment}/>

<main>
	<slot></slot>
</main>