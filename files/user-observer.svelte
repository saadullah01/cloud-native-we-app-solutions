<script>
    import { onMount } from "svelte";
    import {currentUser} from "../stores/user";
  
    onMount(() => {
      firebase.auth().onAuthStateChanged(function(user) {
        user ? currentUser.signIn(user) : currentUser.signOut();
      });
    });
</script>
