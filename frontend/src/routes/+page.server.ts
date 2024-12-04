import type { Recipes, Texture } from '$lib';

export const ssr = true;

export async function load({ fetch }): Promise<{ items: Texture[]; recipes: Recipes }> {
	const items_res = await fetch('http://backend:3000/api/textures/');
	const items_json = await items_res.json();
	const recipes_res = await fetch('http://backend:3000/api/recipes/');
	const recipes_json = await recipes_res.json();
	return { items: JSON.parse(items_json), recipes: JSON.parse(recipes_json) };
}
