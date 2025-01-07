<script lang="ts">
	import ChoiceItem from '$lib/components/ChoiceItem.svelte';

	let selected = $state(undefined);
</script>

<div>{JSON.stringify(selected)}</div>
<ChoiceItem {selected} />
