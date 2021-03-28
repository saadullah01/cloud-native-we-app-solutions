<script>
    export let elementType;
    export let label;
    export let id;
    export let placeholder;
    export let value;
    export let errorMessage;
    export let hasError;

    let isDirty = false;
</script>
  
<label for={id} class="mt-4 block text-sm font-medium leading-5 text-gray-700">
    {label}
</label>
  
<div class="mt-1 relative rounded-md shadow-sm">
    {#if elementType === "input"}
      <input bind:value {id} {placeholder} on:keypress|once={() => isDirty = true} class="block w-full" />
    {:else if elementType === "textarea"}
      <textarea bind:value rows="10" {placeholder} on:keypress|once={() => isDirty = true} class="block w-full"></textarea>
    {/if}

    {#if hasError && isDirty}
      <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
        <svg class="h-5 w-5 text-red-500" fill="currentColor" viewBox="0 0 20 20">
          <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
        </svg>
      </div>
    {/if}
</div>

{#if hasError && isDirty}
  <p class="mt-2 text-sm text-red-600">{errorMessage}</p>
{/if}
