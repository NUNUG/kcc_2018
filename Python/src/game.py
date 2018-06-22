import pygame
import pygame.mouse
from pygame.locals import *
import sys
import sky
import earth
import weapons
import asteroids
import directions
import score
import collisions
import sounds
import hud
import game_events
import gameover
import config

class Game:
	def __init__(self, screen_size, screen):
		self.events = game_events.GameEvents()
		self.screen = screen
		self.clock = pygame.time.Clock()
		self.sky = sky.Sky(screen_size)
		self.earth = earth.Earth(screen_size, self.events)
		self.weapons = weapons.WeaponSystem(screen_size, self.earth, self.events)
		self.field = asteroids.AsteroidField(screen_size, self.events)
		self.score = score.Score(self.events)
		self.collision_handler = collisions.CollisionHandler(self.screen, self.score, self.events)
		self.hud = hud.HUD(screen_size, self.field, self.earth, self.score, self.weapons, self.events)
		self.game_over = gameover.GameOver(self.screen, screen_size, self.events)
		self.sound_system = sounds.Sounds(self.events)
		self.game_data = config.GameData