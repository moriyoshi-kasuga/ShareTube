<script lang="ts">
	import type { Recipe, Texture } from '$lib';
	import { getRecipe } from '$lib/store.svelte';

	// eslint-disable-next-line @typescript-eslint/no-unused-vars
	let { selected, items }: { selected: undefined | Recipe[]; items: Texture[] } = $props();

	async function select(id: number) {
		selected = await getRecipe(id);
	}
</script>

<div id="ingredients">
	{#each items as { texture, name, id }}
		<!-- svelte-ignore a11y_click_events_have_key_events -->
		<div class="grid" role="button" tabindex="0" onclick={() => select(id)}>
			<img src={texture} alt={name} />
		</div>
	{/each}
</div>

<style>
	#ingredients {
		display: flex;
		justify-content: center;
		flex-wrap: wrap;
		padding: 10px;
		background: #c6c6c6;
		border: 2px solid #373737;
		border-right-color: #fff;
		border-bottom-color: #fff;
	}

	#ingredients {
		overflow-y: scroll;
		width: 33%;
		height: 600px;
	}

	#ingredients::-webkit-scrollbar {
		width: auto;
	}

	#ingredients::-webkit-scrollbar-track {
		background-color: #8b8b8b;
	}

	#ingredients::-webkit-scrollbar-thumb {
		height: 10px;
		background-color: #c6c6c6;
		border: 2px solid #373737;
		border-right-color: #fff;
		border-bottom-color: #fff;
	}

	.grid:hover {
		background-color: rgba(255, 255, 255, 0.4);
	}

	.grid {
		height: 32px;
		width: 32px;
		position: relative;
		display: inline-block;
		text-align: center !important;
		background-color: #8b8b8b;
		border: 2px solid;
		border-top-color: #373737;
		border-right-color: #fff;
		border-bottom-color: #fff;
		border-left-color: #373737;
		vertical-align: middle;
	}

	.grid::before {
		bottom: -2px;
		left: -2px;
	}

	.grid::after {
		top: -2px;
		right: -2px;
	}

	.grid::before,
	.grid::after {
		content: '';
		position: absolute;
		background-color: #8b8b8b;
		height: 2px;
		width: 2px;
		pointer-events: none;
	}
</style>
