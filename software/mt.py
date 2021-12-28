import pymata4
import signal
import time
import sys
def signal(sig,frame):
	print("stoped")
	if board is not None:
		board.reset()

	sys.exit(0)


signal.signal(signal.SIGINT,signal)
board  = pymata4("COM3")

in1 = 8
in2 = 9
board.set_pin_mode(in1,board.OUTPUT,board.DIGITAL)
board.set_pin_mode(in2,board.OUTPUT,board.DIGITAL)
def stop():
	board.digital_write(in1,0)
	board.digital_write(in2,0)

def move_forward():
	board.digital_write(in1,1)
	board.digital_write(in2,0)

def move_back_forward():
	board.digital_write(in1,0)
	board.digital_write(in2,0)	


while True:
	run()
	time.sleep(4)
	stop()
