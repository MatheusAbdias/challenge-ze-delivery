# Challenge-ze-delivery
Backend  challenge https://github.com/ZXVentures/ze-code-challenges/blob/master/backend.md

`This repository is a practice with PostGIS and DRF, for this challenge we need to create a CRUD for stores, and each store has a point and geometry associate. Must complexity in this challenger is list store and sort for must closer for a geometric point and this point needs to be contained in store geometry.`

- For Running this project you need Poetry for the package manager and docker to run the Postgres container. 

## Steps
 - git clone git@github.com:MatheusAbdias/challenge-ze-delivery.git -> Cloning repo
 - poetry install -> install dependencies
 - poetry shell -> start virtaul env
 - docker compose up or docker-compose up -> check your docker compose version 
 - create .env, your .env file only you need is edit example.env
 ```
src/
  .env
 ```
