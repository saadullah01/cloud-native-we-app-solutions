<script context="module">
	export function preload() {
		if (typeof window !== "undefined") {
			return window.db
				.collection("posts")
				.get()
				.then(querySnapshot => {
				const posts = querySnapshot.docs.map(doc => ({
					slug: doc.id,
					...doc.data()
				}));
				return {
					posts
				};
			});
		}
		return null;
	}
</script>

<script>
	export let posts = [];
</script>

<style>
	ul {
		margin: 0 0 1em 0;
		line-height: 1.5;
	}
</style>

<svelte:head>
	<title>Blog</title>
</svelte:head>

<h1>Recent posts</h1>

<ul data-cy="blog-posts-list">
	{#each posts as post}
		<!-- we're using the non-standard `rel=prefetch` attribute to
				tell Sapper to load the data for the page as soon as
				the user hovers over the link or taps it, instead of
				waiting for the 'click' event -->
		<li><a rel="prefetch" href="blog/{post.slug}">{post.title}</a></li>
	{/each}
</ul>
