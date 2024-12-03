// import { json } from '@sveltejs/kit';
// import { items } from 'minecraft-textures/dist/textures/json/1.21.json';
//
// const textures: Map<string, string> = new Map<string, string>();
//
// items.forEach((item) => {
// 	textures.set(item.id, item.texture);
// });
//
// export function GET() {
// 	const toJson = JSON.stringify(Array.from(textures.entries()));
// 	return json(toJson);
// }
