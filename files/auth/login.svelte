<script>
    import { goto } from '@sapper/app';
    import { onMount } from "svelte";
    
    export let firebaseAuthUiConfig = {};
    let isSignInUiShown = false;
    onMount(() => {
        firebaseAuthUiConfig = {
            callbacks: {
                signInSuccessWithAuthResult: () => {
                    goto("/admin");
                    return false;
                },
                uiShown: () => {
                    isSignInUiShown = true;
                }
            },
            credentialHelper: firebaseui.auth.CredentialHelper.NONE,
            signInFlow: "popup",
            signInOptions:[firebase.auth.EmailAuthProvider.PROVIDER_ID]
        };
    });
  
    const signIn = () => {
      firebaseAuthUi.start("#firebaseui-auth-container", firebaseAuthUiConfig);
    };
</script>

{#if !isSignInUiShown}
<button on:click={signIn}>Sign In</button>
{/if}
<div id="firebaseui-auth-container"></div>
