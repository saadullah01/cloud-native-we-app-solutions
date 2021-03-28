<script>
    export let elementType;
    export let label;
    export let id;
    export let placeholder;
    export let value;
</script>
  
<label for={id} class="mt-4 block text-sm font-medium leading-5 text-gray-700">
    {label}
</label>
  
<div class="mt-1 relative rounded-md shadow-sm">
    {#if elementType === "input"}
      <input bind:value {id} {placeholder} class="block w-full" />
    {:else if elementType === "textarea"}
      <textarea bind:value rows="10" {placeholder} class="block w-full"></textarea>
    {/if}
</div>