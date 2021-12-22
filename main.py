import pyfirma
import os
import random
import threading
import time
import cv2
import requests
import base64
import io
from PIL import Image

cam  = cv2.VideoCapture(0)



dire = ['top','right','bottom','left']
findball = False
i = 0

def api(imagename):
	image = Image.open(imagename).convert("RGB")
	buffered = io.BytesIO()
	image.save(buffered,quality=90,format="JPEG")
	img_str = base64.b64encode(buffered.getvalue())
	img_str = img_str.decode("ascii")
	upload_url = "".join([
		    "https://detect.roboflow.com/minge/2",
		    "?api_key=qG35nU2qVCqQDzCgOqnL",
		    f"&name={imagename}"
	])
	r = requests.post(upload_url,data = image_str,headers={
		"Content-Type": "application/x-www-form-urlencoded"
		})
	preds = r.json()
	detections = preds['predicitons']
	for target in detections:
		x1 = box['x'] - box['width']/2
		x2 = box['x'] + box['width']/2
		y1 = box['y'] - box['height']/2
		y2 = box['y'] + box['height']/2
	return x1,x2,y1,y2
def get_image():
	s,img = cam.read()
	if s:
		imwrite(f'{dire[i]}.jpg',img)
		image_name = dire[i].'jpg'
		x1,x2,y1,y2 = api(image_name)
		if x1!=0 and x2!=0 and y1!=0 and y2!=0:
			findball = True
def rotate():
	#rotate 90* grade
	if i == 0:
		get_image()
		i = i + 1
	else:
		i = i + 1
		get_image()




while True:
	if findball == True:
		break
	rotate()