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
from pymata4 import pymata4
import motor1

cam  = cv2.VideoCapture(0)

triggerPin = 11
echo_pin = 12

board = pymata4.Pymata4()
def the_callback(data):
	print("distance: ",data)
board.set_pin_mode_sonar(triggerPin,echo_pin,the_callback)

dire = ['top','right','bottom','left']
findball = False
i = 0
width,height = 0
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
	for box in detections:
		x1 = box['x'] - box['width']/2
		x2 = box['x'] + box['width']/2
		y1 = box['y'] - box['height']/2
		y2 = box['y'] + box['height']/2
		width = box['width']
		height = box['height']
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
	get_image()
	i = i + 1
def correction(x1,x2,y1,y2):
	rezx = width
	rezy = height
	minimaljokeplus = 200
	minimaljokeminus = -200
	minheigtplus = 200
	minheigtmin = -200
	#width
	if(x1<minimaljokeminus):
		print('The ball is outside of the perimeter')
		motor1.move_left(time)
		distance_correction = abs(x1+minimaljoke)
	elif(x2>minimaljokeplus):
		motor1.move_right(time)
		distance_correction = abs(x2-minimaljoke)
	#height
	if(y1>minimaljokeplus):
		h = abs(y1-minimaljokeplus)
	elif y1<minimaljokeminus:
		h = (y1+minimaljokeminus)
	return distance_correction,h
while True:
	if findball == True:
		break
	x1,x2,y1,y2 = rotate()
	weights,height = correction(x1,x2,y1,y2)
	#move forward



while True:
	try:
		time.sleep(1)
		board.sonar_read(triggerPin)
	except Exception:
		board.shutdown()
