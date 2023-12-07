# Containerized App Exercise

## Team Members:
[Jazlene Darrisaw](https://github.com/Jazlene30)
[Chang Liu](https://github.com/cl5706)
[Kevin Li](https://github.com/KevinLi2260)

## Image Recognition:

For this project, Image recognition is used through machine learning to help identify an image through photos or the users camera and return the result of what the image resembles and a picture that resembles it.

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


