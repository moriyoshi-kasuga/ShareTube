#!/usr/bin/env bash
curl https://raw.githubusercontent.com/PrismarineJS/minecraft-assets/refs/heads/master/data/1.21.1/texture_content.json | jq '.[] | select(.texture != null) | {(.name) : .texture}' | jq -s 'add' > textures.json
