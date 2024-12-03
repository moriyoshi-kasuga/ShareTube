import { items } from 'minecraft-textures/dist/textures/json/1.21.json';
import minecraftData, { type Recipe } from 'minecraft-data';

// const recipes = minecraftData('1.21').recipes;
//
// export function getRecipe(id: number): Recipe[] {
// 	return recipes[id];
// }
//
export type Texture = {
	name: string;
	texture: string;
};

export const textures: Map<string, Texture> = new Map<string, Texture>();

items.forEach((item) => {
	textures.set(item.id, { texture: item.texture, name: item.readable });
});
