from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
import torch
import os
import pathlib
print(os.environ)
path = os.environ.get('path')


model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5_weights.pt')
print(model.conf) #threshold = 0.25
# model.conf = 0.25

app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}

class Payload(BaseModel):
    url: str
    image_id: str

@app.post("/"+path+"/predict")
def predict(payload: Payload):
	results = model(payload.url)
	detections = results.xywh
	bbox_list = []
	map_predictions = {1:2,2:3,3:1,4:4}
	for detection in detections[0]:
		bbox = {
		"category_id":map_predictions[detection[-1].item()],
		"bbox":{
			"x" :  detection[0].item() - (detection[2].item()/2),
			"y" :  detection[1].item() - (detection[3].item()/2),
			"w" :  detection[2].item(),
			"h" :  detection[3].item()},
		"score": detection[4].item()}
		bbox_list.append(bbox)
	
	submission = {"image_id": payload.image_id,"bbox_list":bbox_list}
	
	return submission