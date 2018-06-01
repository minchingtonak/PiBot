import pygame, os

class Controller:
	
	def __init__(self, port):
		os.environ["SDL_VIDEODRIVER"] = "dummy"
		pygame.init()
		self.c = pygame.joystick.Joystick(port)
		self.c.init()
		print 'Initialized controller:', self.c.get_name()

	def refresh_button_presses(self):
		pygame.event.get(pygame.JOYBUTTONDOWN)
	
	def refresh_joystick_moves(self):
		pygame.event.get(pygame.JOYAXISMOTION)
		
	def refresh_hat_presses(self):
		pygame.event.get(pygame.JOYHATMOTION)
		
	def get_button_pressed(self, num):
		self.refresh_button_presses()
		return self.c.get_button(num)
		
	def get_axis_moved(self, num):
		self.refresh_joystick_moves()
		return self.c.get_axis(num)
	
	def get_A(self):
		return self.get_button_pressed(0)
	
	def get_B(self):
		return self.get_button_pressed(1)

	def get_X(self):
		return self.get_button_pressed(2)
		
	def get_Y(self):
		return self.get_button_pressed(3)
	
	def get_LB(self):
		return self.get_button_pressed(4)
		
	def get_RB(self):
		return self.get_button_pressed(5)
		
	def get_SELECT(self):
		return self.get_button_pressed(6)
	
	def get_START(self):
		return self.get_button_pressed(7)
		
	def get_HOME(self):
		return self.get_button_pressed(8)
		
	def get_LS(self):
		return self.get_button_pressed(9)
	
	def get_RS(self):
		return self.get_button_pressed(10)
		
	def get_LS_X(self):
		return self.get_axis_moved(0)
		
	def get_LS_Y(self):
		return -self.get_axis_moved(1) + 0
		
	def get_RS_X(self):
		return self.get_axis_moved(3)
		
	def get_RS_Y(self):
		return -self.get_axis_moved(4) + 0
		
	def get_LT(self):
		return (self.get_axis_moved(2) / 2.0) + 0.5
		
	def get_RT(self):
		return (self.get_axis_moved(5) / 2.0) + 0.5
		
	def get_triggers(self):
		return self.get_RT() - self.get_LT()
		
	def get_hat(self):
		self.refresh_hat_presses()
		return self.c.get_hat(0)
