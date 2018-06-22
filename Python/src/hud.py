import pygame


class HUD:
	def __init__(self, screen_size, asteroid_field, earth, score, weapon_system, events):
		self.screen_size = screen_size
		self.asteroid_field = asteroid_field
		self.earth = earth
		self.score = score
		self.weapon_system = weapon_system
		self.life_font = pygame.font.Font(None, 50)
		self.score_font = pygame.font.SysFont("Courier New", 32, 1, 0)

		self.green_surface = pygame.Surface((24, 24))
		self.green_surface.fill([0, 255, 0])
		self.red_surface = pygame.Surface((24, 24))
		self.red_surface.fill([255, 0,0])

		w, h = screen_size
		self.background_surface = pygame.Surface((w, 35))
		self.background_surface.set_alpha(128)
		self.events = events
	def render(self, screen):
		self._render_background(screen)
		self._render_score(screen)
		self._render_life(screen)
		self._render_cooldowns(screen)
		#screen.blit(self.background_surface, (0, 0))
	def _render_background(self, screen):
		self.background_surface.fill([128,128,128])
		screen.blit(self.background_surface, (0, 0))
	def _render_score(self, screen):
		text = str(self.score.score)
		score_surface = self.score_font.render(text, False, [255, 255, 0])
		#self.background_surface.blit(score_surface, (0, 0))
		screen.blit(score_surface, (0, 0))
	def _render_life(self, screen):
		if (self.earth.remaining_endurance == self.earth.total_endurance):
			percentage = 100
		else:
			percentage = int(self.earth.remaining_endurance * 100 / (self.earth.total_endurance + 0.00001))
		text = str(percentage) + "%"
		life_color = int(percentage * 2.55)
		life_surface = self.life_font.render(text, False, [255, life_color, life_color])
		#self.background_surface.blit(life_surface, (200, 0))
		screen.blit(life_surface, (200, 0))
	def _render_cooldowns(self, screen):
		w,h = self.screen_size

		cooldowns = [ \
			self.weapon_system.gun_cooldown, \
			self.weapon_system.multigun_cooldown, \
			self.weapon_system.missile_cooldown, \
			self.weapon_system.multimissile_cooldown \
		]

		for i in range(4):
			xoffset = w - 32 * (1+i)
			yoffset = 4
			cooldowns[i-1].calculate()
			# Cooldown 0 (gun) is always green.  Its cooldown is so short, it's not worth calculating or showing a red.
			if (i == 0) or (cooldowns[i].ready):
				screen.blit(self.green_surface, (xoffset, yoffset))
			else:
				screen.blit(self.red_surface, (xoffset, yoffset))

