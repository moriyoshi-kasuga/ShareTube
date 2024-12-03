# syntax=docker/dockerfile:1

ARG NODE_VERSION=23.3

FROM node:${NODE_VERSION}-slim

WORKDIR /frontend

COPY . .

# RUN npm install -g npm@latest && npm i
RUN npm i

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "5173"]
