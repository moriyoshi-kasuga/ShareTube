import type { Recipe, Recipes } from '$lib';

const recipes: Recipes = $state(new Map());

export async function getRecipe(id: number): Promise<Recipe[] | undefined> {
	const recipe_already = recipes.get(id);
	if (recipe_already != undefined) {
		return recipe_already;
	}
	const recipe_res = await fetch('http://backend:3000/api/recipes/?id=' + id);
	const recipe_json = await recipe_res.json();
	const recipe: Recipe[] = JSON.parse(recipe_json);
	recipes.set(id, recipe);
	return recipe;
}
