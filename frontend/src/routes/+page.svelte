<script lang="ts">
	import { type Recipe, type Recipes, type Texture } from '$lib';
	import ChoiceItem from '../components/ChoiceItem.svelte';

	export let data: { items: Texture[]; recipes: Recipes };
	let selected = undefined;
</script>

<ChoiceItem {selected} items={data.items} recipes={data.recipes} />
