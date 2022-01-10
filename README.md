## Used for the object detection hackathon on underwater pipes (Yolov5s)


### To Deploy Locally run
```
docker build -t <image_name> .
docker run -e path=env -p 8000:8000 -t --name <container_name> <image_name>
```

### Sample Inferencing
- After deploying, go to http://127.0.0.1:8000/docs
- Test with post request using the payload below:

```
{"url":"https://github.com/Northerman/object_detection_hackathon/blob/main/20201107122805838.png?raw=True","image_id":20201107122805838}
```

### Expected response in xywh and score
![alt text](https://github.com/Northerman/object_detection_hackathon/blob/main/expected_response.png?raw=true)


