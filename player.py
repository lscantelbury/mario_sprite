
import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self, type,  dx, dy):
		super().__init__()
		
		# Loading Sprites into a list
		self.type = type
		self.sprites = []
		if self.type == "jump":
			self.sprites.append(pygame.image.load('assets/jump/mario1.png'))
			self.sprites.append(pygame.image.load('assets/jump/mario2.png'))
			self.sprites.append(pygame.image.load('assets/jump/mario3.png'))
			self.sprites.append(pygame.image.load('assets/jump/mario4.png'))
			self.sprites.append(pygame.image.load('assets/jump/mario5.png'))
			self.sprites.append(pygame.image.load('assets/jump/mario6.png'))
			self.sprites.append(pygame.image.load('assets/jump/mario7.png'))
			self.sprites.append(pygame.image.load('assets/jump/mario8.png'))
			self.sprites.append(pygame.image.load('assets/jump/mario9.png'))
			self.sprites.append(pygame.image.load('assets/jump/mario10.png'))
		
		if self.type == "walk" or self.type == "run":
			self.sprites.append(pygame.image.load('assets/walking/mario1.png'))
			self.sprites.append(pygame.image.load('assets/walking/mario2.png'))
			self.sprites.append(pygame.image.load('assets/walking/mario3.png'))
	
		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]

		self.rect = self.image.get_rect()
		self.rect.center = [dx, dy]

	def update(self):

		if self.type == "run":
			self.current_sprite += 0.5
		else:
			self.current_sprite += 0.2

		if self.current_sprite >= len(self.sprites):
			self.current_sprite = 0

		self.image = self.sprites[int(self.current_sprite)]
