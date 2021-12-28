import time
import cv2
import random
import pyfirma
import main

indexrotate = []
folderpath='C://photos//'
Webcam = cv.VideoCapture(0)
i = 0
verffffffff = False
max1 = 0,max2 = 0
def distance(x1,x2,y1,y2):
	bestx = 0
	besty = 0
	if(x1>=0):
		bestx = x1
	elif(x2<0):
		bestx = x2

	if(y2<=0):
		besty = y2
	elif(y2>=0):
		besty = y1
	if(x1<=0 and x2>=0):
		max1 = i
		verffffffff = True
		return verffffffff
	else:
		mediesum = (abs(besty)+abs(bestx))/2
		if(mediesum>max2):
			max2 = mediesum
			max1 = i
	i++
def rotate():
	#rotate 45 grade to left
	s,img = cv2.read()
	if s:
		imwrite(f'{indexrotate[i]}.jpg',img)
		image_name = indexrotate[i].'jpg'
		x1,x2,y1,y2 = main.api(image_name)
gata = False
while(gata==False):
	if(i==4):
		gata = True
	if(i==2):
		#rotire(180)
	else:
		rotate()
#maxi = 1 ,45
#maxi = 2, 90
#maxi = 3,270
#maxi = 4,315
#rotim 45
if(maxi==1):
	#rotim 45
if(maxi==2):
	#rotim 90
if(maxi==3):
	#rotim 270
if(maxi==4):
	#rotim 315
