from controller import Controller
import time

cont = Controller(0)

while 1:
	if cont.get_B():
		exit(0)

	print(cont.get_RS_Y())
	time.sleep(0.1)

