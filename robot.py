from controller import Controller
from pwmhat import PWMHat
import time

cont = Controller(0)
p = PWMHat(50)
val = 0

#534 max forward
#320.5 mid neutral
#107 max backward
while 1:
	if cont.get_B():
		exit(0)
	if cont.get_LB() and cont.get_RB():
		val = int(320.5 + (cont.get_LS_Y()**2 * 213.5))
	else:
		val = 50
	p.drive(0, val)
	print(val)

