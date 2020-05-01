import pygame
from globals import *
from player import Player
from ball import Ball
import math
# dx = animal.velocity*math.cos(animal.theta)
# 	dy = animal.velocity*math.sin(animal.theta)

def setup():
	pygame.init()
	canvas = pygame.display.set_mode((canvasWidth, canvasHeight))
	
	return canvas

def main():
	canvas = setup()

	canvas.fill(BLACK)

	#Initialize player
	playerOne = Player(canvasWidth/10, canvasHeight/2, 1)
	playerTwo = Player(canvasWidth-canvasWidth/10, canvasHeight/2, 2)
	ballOne = Ball()

	spriteList.append(playerOne)
	spriteList.append(playerTwo)
	spriteList.append(ballOne)

	while(True):
		
		#x*y rectangle
		canvas.fill(BLACK)

		#UPDATE
		draw(canvas, spriteList)

		updatePlayerOne(playerOne)
		#updatePlayerTwo(playerTwo)
		updateBall(canvas, ballOne, playerOne)
		
		pygame.display.update()

def draw(canvas, spriteList):
	for sprite in spriteList:
		if(sprite.type == "Player"):
			#X&Y are the coords of the upper left of the rect
			pygame.draw.rect(canvas, WHITE, (sprite.x, sprite.y, sprite.width, sprite.height))
		elif(sprite.type == "Ball"):
			pygame.draw.circle(canvas, RED, (int(sprite.x), int(sprite.y)), sprite.radius)

def updateBall(canvas, ball, player):
	
	#check if player hit ball
	for i in range(player.x, player.x + player.width):
		for j in range(player.y, player.y + player.height):
			pixelColor = canvas.get_at((i, j))
			if(pixelColor == RED):
				#send ball straight back for now
				ball.theta = 180 + ball.theta
				break
	dx = ball.velocity * math.cos(ball.theta)
	dy = ball.velocity * math.sin(ball.theta)
				#Now determine what part of the paddle the ball hit

	#Check for collision with bottom of screen
	if(ball.y + dy >= canvasHeight - ball.radius):
		ball.theta += 90
	#top of screen
	elif(ball.y + dy <= 0 + ball.radius):
		ball.theta += 90
	#Right side
	elif(ball.x + dx >= canvasWidth - ball.radius):
		ball.theta += 90
	elif(ball.x + dx <= 0 + ball.radius):
		ball.theta += 90
	else:
		ball.x += dx
		ball.y += dy


def updatePlayerOne(player):
	#Update player

	for event in pygame.event.get():	
		if event.type == pygame.KEYDOWN:
			if(event.key == pygame.K_UP):
				player.velocity = -1
			elif(event.key == pygame.K_DOWN):
				player.velocity = 1
		else:
			player.velocity = 0



	#Check if changing our height will put it over/under screen height
	if(player.y + player.velocity <= 0):
		player.y = 0
	elif(player.y + player.height + player.velocity >= canvasHeight):
		player.y = canvasHeight-player.height
	else:
		player.y += player.velocity


if __name__ == '__main__':
	main()