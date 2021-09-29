import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

pygame.init()

#* X = Horizontal Y = Vertical

screenWidth = 640
screenHeight = 480

screen = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('C:/Users/dankr/Documents/Programming/Python/Games/python-icon.png')
pygame.display.set_icon(icon)

#* Player
playerIcon = pygame.image.load('C:/Users/dankr/Documents/Programming/Python/Games/space-invaders.png')

playerX = 320
playerY = 400
playerX_change = 0

#* Enemy
enemyIcon = pygame.image.load('C:/Users/dankr/Documents/Programming/Python/Games/alien-ship.png')

enemyX = 320
enemyY = 200
enemyX_change = 0

#* Game Loop
def player(x, y):
	screen.blit(playerIcon, (playerX, playerY))

def enemy(x, y):
	screen.blit(enemyIcon, (enemyX, enemyY))

running = True
while running:
	screen.fill((22, 73, 156))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				playerX_change = -0.1
			if event.key == pygame.K_RIGHT:
				playerX_change = 0.1
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playerX_change = 0

	playerX += playerX_change
	player(playerX, playerY)

	enemy(enemyX, enemyY)
	
	#* Refresh display output
	pygame.display.update()

	if playerX <= -2:
		playerX = -2
	elif playerX >= (640 - 62):
		playerX = (640 - 62)
