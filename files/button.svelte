<style>
    .disabled {
      @apply opacity-50 cursor-not-allowed;
    }
  
    .enabled:hover {
      @apply bg-indigo-500;
    }
</style>

<span class="inline-flex rounded-md shadow-sm">
    <button
      {...$$props}
      type="button"
      class="inline-flex items-center px-4 py-2 border border-transparent text-sm leading-5 font-medium rounded-md text-white bg-indigo-600 focus:outline-none focus:border-indigo-700 focus:shadow-outline-indigo active:bg-indigo-700"
      class:disabled={$$props.disabled}
      class:enabled={!$$props.disabled}
      on:click
    >
    
      <slot />
    </button>
</span>