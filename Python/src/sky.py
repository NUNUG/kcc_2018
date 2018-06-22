import pygame
from pygame.locals import *
from config import *

class Sky(pygame.sprite.Sprite):
	def __init__(self, screen_size):
		print("screen_size: " + repr(screen_size))
		self.image = pygame.transform.scale(pygame.image.load(GameData.GRAPHICS_SKY_FILENAME), screen_size)
		print("Backround rect: " + repr(self.image.get_rect()))
	def render(self, screen):
		screen.blit(self.image, [0,0])
