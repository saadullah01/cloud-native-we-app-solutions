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
</div>