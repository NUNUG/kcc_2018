import pygame
import math

class Projectile(pygame.sprite.Sprite):
	def __init__(self, frames, direction, position):
		pygame.sprite.Sprite.__init__(self)
		self.frame_index = 0
		self.frame_count = len(frames)
		self.frames = frames
		self.original_image = frames[0]
		self.original_rect = self.original_image.get_rect()
		self.image = self.frames[0]
		self.rect = self.image.get_rect()
		self.direction = direction
		self.position = position
		self.acceleration = 0
		self.max_speed  = 0
	def __del__(self):
		#print("Destroyed Projectile: " + repr(self))
		pass
	def animate(self):
		self.frame_index = (self.frame_index + 1) % self.frame_count
		self.image = self.frames[self.frame_index]
	def move(self):
		if (self.acceleration != 0):
			self.accelerate()
		px, py = self.position 
		dx, dy = self.direction
		x = px + dx
		y = py + dy
		self.position = (x, y)
		#self.rect = self.rect.move([dx, dy])
		self.rect.x = x - self.rect.width / 2
		self.rect.y = y - self.rect.height / 2
	def render(self, screen):
		x, y = self.position
		#upperleft_pos = (x - (self.rect.width / 2), y - (self.rect.height / 2))
		upperleft_pos = (self.rect.left, self.rect.top)
		screen.blit(self.frames[self.frame_index], upperleft_pos)		
	def accelerate(self):
		(x, y) = self.direction
		x = x * self.acceleration
		y = y * self.acceleration
		speed = math.sqrt(x*x + y*y)
		if (speed <= self.max_speed):
			self.direction = (x,y)
