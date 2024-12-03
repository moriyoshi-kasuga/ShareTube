// import { json } from '@sveltejs/kit';
// import minecraftData, { type Recipe } from 'minecraft-data';
//
// const mcData = minecraftData('1.21');
//
// export function GET(request) {
// 	const id = request.url.searchParams.get('id');
// 	if (id == null) {
// 		return new Response('id is null', { status: 400 });
// 	}
// 	const n = parseInt(id);
// 	if (isNaN(n)) {
// 		return new Response('id is not number', { status: 400 });
// 	}
// 	const data = mcData.recipes[n];
// 	if (data == undefined) {
// 		return new Response('id is not found', { status: 400 });
// 	}
// 	return json(data);
// }
