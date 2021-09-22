import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

pygame.init()
#* X = < ----- > #Y = /\ \/
screenWidth = 640
screenHeight = 480

screen = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('python-icon.png')
pygame.display.set_icon(icon)

playerX = screenWidth / 2
playerY = screenHeight / 2
playerIcon = pygame.image.load('spaceship.png')

def player(x, y):
	screen.blit(playerIcon, (playerX, playerY))

running = True
while running:
	screen.fill((22, 73, 156))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	# If keystroke is pressed, check whether its <- or ->
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				print("Left arrow is pressed")
			if event.key == pygame.K_RIGHT:
				print("Right arrow is pressed")
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				print("Key has been released")
	
	player(playerX, playerY)
	
	pygame.display.update()
