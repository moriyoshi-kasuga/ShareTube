#!/usr/bin/env bash

docker compose -f compose.prod.yaml down && docker compose -f compose.prod.yaml up -d --build
