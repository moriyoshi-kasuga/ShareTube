import json
from typing import Any, List

with open("./data/recipes.json") as f:
    RECIPES: List[Any] = json.load(f)

with open("./data/textures.json") as f:
    TEXTURES: List[Any] = json.load(f)
