//! this code from https://github.com/PrismarineJS/node-minecraft-data.git repository

export type Recipe = ShapedRecipe | ShapelessRecipe;
/**
 * An item can be represented different ways.
 */
export type RecipeItem = Id | IdMetadata | Id1Metadata1Count1;
/**
 * A single numerical ID or null.
 */
export type Id = number | null;
/**
 * A list of id and metadata. This is preferred if there are many items at once, e.g. in a shape.
 */
export type IdMetadata = [] | [Id] | [Id, Metadata];
export type Metadata = number;
export type Count = number;
/**
 * A shape is a list of rows, which are lists of items. There must be at least one row with at least one item in it. All rows must have the same length. Empty rows at the beginning or end of a shape may be omitted. Empty columns at the end may also be omitted. When an item can be crafted in a 2x2 grid, the shape may not be larger than 2x2.
 *
 * @minItems 1
 * @maxItems 3
 */
export type Shape = [ShapeRow] | [ShapeRow, ShapeRow] | [ShapeRow, ShapeRow, ShapeRow];
/**
 * @minItems 1
 * @maxItems 3
 */
export type ShapeRow =
	| [RecipeItem]
	| [RecipeItem, RecipeItem]
	| [RecipeItem, RecipeItem, RecipeItem];
/**
 * @minItems 1
 */
export type Ingredients = [RecipeItem, ...RecipeItem[]];

/**
 * A dictionary of quoted numerical item IDs. Each ID maps to a list of recipes. There may be multiple different recipes per item (same ID and metadata). The recipes may not be sorted.
 */
export type Recipes = Map<string, Recipe[]>;
/**
 * A shaped recipe is a dictionary of result, inShape and optionally outShape
 */
export interface ShapedRecipe {
	result: RecipeItem;
	inShape: Shape;
	outShape?: Shape;
}
/**
 * A dictionary of at least id, optionally metadata and count. This is preferred if there are not many items at once, e.g. result in a recipe.
 */
export interface Id1Metadata1Count1 {
	id: Id;
	metadata?: Metadata;
	count?: Count;
}
/**
 * A shapeless recipe is a dictionary of result and ingredients
 */
export interface ShapelessRecipe {
	result: RecipeItem;
	ingredients: Ingredients;
}

export type Texture = {
	name: string;
	texture: string;
};
