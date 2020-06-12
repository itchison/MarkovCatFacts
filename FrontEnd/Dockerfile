# base image
FROM node:13.3.0 AS compile-image
#FROM node:12.13 as build-deps
ENV NODE_ROOT /usr/src/app
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . .

RUN npm install @angular/cli -g --silent
RUN npm install
RUN npm audit fix
RUN ng build
