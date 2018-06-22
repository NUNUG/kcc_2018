import pygame

class Cooldown():
	def __init__(self, cooldown_time):
		self.cooldown_time = cooldown_time
		self.reset()
	def reset(self):
		self.last_fire = 0
		self.calculate()
	def calculate(self):
		elapsed = pygame.time.get_ticks() - self.last_fire
		self.remaining = self.cooldown_time - elapsed
		if (self.remaining < 0):
			self.remaining = 0
		self.ready = self.remaining == 0
		return self.ready
	def fire(self):
		self.last_fire = pygame.time.get_ticks()
