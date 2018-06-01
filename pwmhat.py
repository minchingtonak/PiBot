import Adafruit_PCA9685

class PWMHat:

	def __init__(self, freq):
		self.pwm = Adafruit_PCA9685.PCA9685()
		self.pwm.set_pwm_freq(freq)
	
	def drive(self, channel, val):
		self.pwm.set_pwm(channel, channel, val)