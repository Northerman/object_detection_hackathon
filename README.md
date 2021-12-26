## A code used for the object detection hackathon on under water pipes
- Model used: Yolov5s

## To Deploy
```
docker build -t <image_name> .
docker run -e path=env -p 8000:8000 -t --name <container_name> <image_name>
```

## Sample inference

After deploying, go to http://127.0.0.1:8000/docs
