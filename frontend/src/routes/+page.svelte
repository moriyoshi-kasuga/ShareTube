<script>
	import { textures } from '$lib';
</script>

<div class="ingredients">
	{#each [...textures] as [, { texture, name }]}
		<img src={texture} alt={name} />
	{/each}
</div>

<style lang="scss">
	.ingredients {
		display: flex;
		flex-wrap: wrap;
		padding: 10px;
		margin-top: 10px;
		background: #c6c6c6;
		border: 2px solid #373737;
		border-right-color: #fff;
		border-bottom-color: #fff;
	}

	.ingredients {
		max-height: 700px;
		max-width: 33%;
		overflow-y: scroll;
	}

	.ingredients::-webkit-scrollbar {
		width: auto;
	}

	.ingredients::-webkit-scrollbar-track {
		background-color: #8b8b8b;
	}

	.ingredients::-webkit-scrollbar-thumb {
		height: 10px;
		background-color: #c6c6c6;
		border: 2px solid #373737;
		border-right-color: #fff;
		border-bottom-color: #fff;
	}
</style>
