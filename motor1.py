import pymata4
import pyfirma
import time
echopin_1right = 10
trigger_pin1 = 11
echopin_2right= 9
trigger_pin2= 8
echopin_1left = 7
trigger_pin1le = 6
echopin_2left = 5
trigger_pin2left = 4
def move_right(time):
   #lasam doar motoarele din stanga pornite
   while time:
   	
   	time.sleep(1)
   	time = time-1

def move_left(time):
	#lasam doar motoarele din dreapta pornite
	while time:
		s
		time.sleep(1)
		time = time -1