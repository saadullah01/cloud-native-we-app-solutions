<script>
    import Button from './ui-elements/button.svelte';
    import InputGroup from './ui-elements/input-group.svelte';
  
    let title;
    let content;
    let successMessage;
    let errorMessage;
  
    $: isPublishDisabled = !(title && content);

    const publish = () => {
      const slug = title.replace(/\s/g, "-").toLowerCase();
      window.db.collection("posts").doc(slug).set({
        title,
        content
      }).then(() => {
        successMessage = "Successfully published your blog post.";
      }).catch((error) => {
        errorMessage = "Oh no... there was an error publishing. Try again later.";
      });
    };
</script>
  
<h1>Add new blog post</h1>
<div class="mt-6">
    <form on:click={publish}>
      <InputGroup 
      elementType="input" 
      label="Title" 
      errorMessage="Please provide a title."
      hasError={!title}
      id="title" 
      placeholder="Untitled" 
      bind:value={title} />

      <InputGroup 
      elementType="textarea" 
      label="Content" 
      errorMessage="Please provide content."
      hasError={!content}
      id="content" 
      placeholder="Your content..." 
      bind:value={content} />
      
      <Button disabled={isPublishDisabled}>Publish</Button>
    </form>
    {#if successMessage}
      <p class="mt-2 text-sm">{successMessage}</p>
    {:else if errorMessage}
      <p class="mt-2 text-sm text-red-600">{errorMessage}</p>
    {/if}
</div>