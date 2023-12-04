# Containerized App Exercise

Build a containerized app that uses machine learning. See [instructions](./instructions.md) for details.
## docker setup:

download mongodb image from docker hub:

```
docker pull mongo
```
	
check mongo installed:
```
docker images
```
run the mongo container:
```
docker run --name mongodb -d -p 27017:27017 mongo
```
check runnning containers:
```
docker ps
docker ps-a
```
## run the web app:
```
python webapp.py
```