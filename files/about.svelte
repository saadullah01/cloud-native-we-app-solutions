<script>
  import FeatureToggle from "../components/feature-toggle.svelte";
  import { FEATURE_TOGGLES } from "../feature-toggles";
</script>

<svelte:head>
	<title>About</title>
</svelte:head>

<h1>About this site</h1>

<p>This is the 'about' page. There's not much here.</p>

<FeatureToggle name={FEATURE_TOGGLES.vipWelcome.name}>
  <p>Some people see this, others don't!</p>
</FeatureToggle>