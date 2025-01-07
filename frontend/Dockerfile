# syntax=docker/dockerfile:1

ARG NODE_VERSION=23.3

FROM node:${NODE_VERSION}-slim AS installer

WORKDIR /frontend

COPY package*.json ./
RUN npm ci

FROM installer AS builder

WORKDIR /frontend

COPY . .

RUN npm run build

FROM builder AS dev

WORKDIR /frontend

COPY package.json .

CMD ["npm", "run", "dev", "--", "--port", "25000", "--host"]

FROM builder AS prod

WORKDIR /frontend

CMD ["npm", "run", "start"]
