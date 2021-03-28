<script>
    import Button from './ui-elements/button.svelte';
    import InputGroup from './ui-elements/input-group.svelte';
  
    let title;
    let content;
  
    $: isPublishDisabled = !(title && content);
</script>
  
<h1>Add new blog post</h1>
<div class="mt-6">
    <form>
      <InputGroup elementType="input" label="Title" id="title" placeholder="Untitled" bind:value={title} />
      <InputGroup elementType="textarea" label="Content" id="content" placeholder="Your content..." bind:value={content} />
      <Button disabled={isPublishDisabled}>Publish</Button>
    </form>
</div>