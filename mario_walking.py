import pygame, sys
from player import *

# General Setup
pygame.init()
clock = pygame.time.Clock()


# Game Screen
mesurements = [400, 400]
screen = pygame.display.set_mode((mesurements[0], mesurements[1]))
pygame.display.set_caption(("Mario Walking"))

# Sprite Group
sprites = pygame.sprite.Group()
player = Player("walk", 200, 200)
sprites.add(player)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.quit()
				quit()
			
	screen.fill((0,0,0))
	sprites.draw(screen)
	sprites.update()
	pygame.display.update()
	clock.tick(60)
