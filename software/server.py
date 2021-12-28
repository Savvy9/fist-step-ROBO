try:
	from pyfirma import Arduino,util
	import time
except:
	import pip
	pip.main(['install','pyfirma'])
	from pyfirma import Arduino,util
def setup():
	board = Arduino("COM3")
	iterator = util.Iterator(board)
	iterator.start()

