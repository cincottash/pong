from globals import *
import random

class Ball:
	def __init__(self):
		self.x = canvasWidth/2
		self.y = canvasHeight/2
		self.radius = 10
		self.type = "Ball"
		self.theta = random.randint(0, 360)
		self.velocity = 1
