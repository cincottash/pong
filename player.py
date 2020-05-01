from globals import *
class Player:
	def __init__(self, x, y, num):
		self.x = x
		self.y = y
		self.height = canvasHeight/15
		self.width = canvasWidth/100
		self.type = "Player"
		self.velocity = 0
		self.num = num
