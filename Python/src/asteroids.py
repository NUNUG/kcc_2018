import pygame
import math
from random import random
from projectile import *
from cooldown import *
from config import *
from game_events import *
from events import *

class Asteroid(Projectile):
	def __init__(self, screen_size, level, image, direction, position, rotation_speed, angle):
		Projectile.__init__(self, image, direction, position)
		self.screen_size = screen_size
		self.rotation_speed = rotation_speed
		self.angle = angle
		self.level = level
		self.potential_damage = (level + 1.0) * 4
		self.total_endurance = level * 100 #(level + 0.01) * 100 - 1
		self.remaining_endurance = self.total_endurance
		self.rect_color = [0, 255, 0]
		self.frame_color = [0, 255, 255]
		self.collision_color = [0, 255, 0]
		# print("Created Asteroid: " + repr(self))
	def __del__(self):
		# print("Destroyed Asteroid: " + repr(self))
		pass
	def animate(self):
		Projectile.animate(self)
		self.angle = self.angle + self.rotation_speed
	def move(self):
		Projectile.move(self)
		px, py = self.position
		#dx, dy = self.direction
		sx, sy = self.screen_size
		if (px < 0): px = sx-1
		if (px > sx-1): px = 0
		if (py < 0): py = sy - 1
		if (py > sy-1): py = 0
		self.position = (px, py)
	def render(self, screen):
		# We have to override the render because rotating an image changes its size.
		newimage = pygame.transform.rotate(self.frames[self.frame_index], self.angle)
		newrect = newimage.get_rect()
		newrect = newimage.get_rect()

		# Position is the CENTER of the asteroid.  Offset x and y by minus half of height and width to draw it centered.
		px, py = self.position
		newposition = (px - newrect.width / 2, py - newrect.height / 2)
		


		screen.blit(newimage, newposition)
		# Draw a rectangle around the asteroid and paint a LEVEL badge
		if (GameData.debug_mode and True):
			npx, npy = newposition
			newrect.move_ip(npx, npy)
			pygame.draw.rect(screen, self.frame_color, newrect, 1)
			pygame.draw.rect(screen, self.rect_color, self.rect, 1)

		# Draw a level badge on the asteroid.
		if (GameData.debug_mode and True):
			level_badge_font = pygame.font.Font(None, 25)
			level_badge_surface = level_badge_font.render(str(self.level), False, [255, 0, 0])
			screen.blit(level_badge_surface, newposition)

		# Draw the remaining endurance on the asteroid.
		if (GameData.debug_mode and True):
			level_badge_font = pygame.font.Font(None, 25)
			level_badge_surface = level_badge_font.render(str(self.remaining_endurance), False, [255, 0, 0])
			screen.blit(level_badge_surface, (px + newrect.width / 2, py - newrect.height / 2))

	def take_damage(self, damage):
		self.remaining_endurance = self.remaining_endurance - damage

		# This downgrades the asteroid by several levels if the damage is great enough.
		# We don't want to do that anymore.  Every asteroid now shatters into a set of level 0 shards.
		# if (self.remaining_endurance < 0):
		# 	while (self.remaining_endurance < 0) and (self.level >= 0):
		# 		self.level = self.level - 1
		# 		self.remaining_endurance = self.remaining_endurance + self.level + 1
		# 	# To shatter, we still have to be destroyed but now we have the right level.
		# 	#self.level = self.level + 1	#compensate for the last decrement.
		# 	self.remaining_endurance = -1
	def is_destroyed(self):
		result = self.remaining_endurance <= 0.0
		return result


class AsteroidFactory:
	def __init__(self, screen_size):
		self.screen_size = screen_size
		self.rotation_speed = 4.0
		self._load_images()
	def _load_images(self):
		self.images = []
		original_image = pygame.transform.scale(pygame.image.load(GameData.GRAPHICS_ASTEROID_FILENAME), (50, 50))
		original_rect = original_image.get_rect()
		self.images.append(pygame.transform.scale(original_image, (int(original_rect.width / 5), int(original_rect.height / 5))))
		self.images.append(pygame.transform.scale(original_image, (int(original_rect.width / 4), int(original_rect.height / 4))))
		self.images.append(pygame.transform.scale(original_image, (int(original_rect.width / 3), int(original_rect.height / 3))))
		self.images.append(pygame.transform.scale(original_image, (int(original_rect.width / 2), int(original_rect.height / 2))))
		self.images.append(original_image)
	def CreateAsteroid(self, level = None, position = None):
		# Random level (weighted)
		# level1 = random() * 25
		# level2 = random() * 16
		# level3 = random() * 9
		# level4 = random() * 4
		# level5 = random() * 1

		# At the beginning, we really want mostly big ones.  They'll break down into little ones during gameplay.
		if level == None:
			level0_roll = int(random() * (1 + GameData.ASTEROID_LEVEL0_PROBABILITY))
			level1_roll = int(random() * (1 + GameData.ASTEROID_LEVEL1_PROBABILITY))
			level2_roll = int(random() * (1 + GameData.ASTEROID_LEVEL2_PROBABILITY))
			level3_roll = int(random() * (1 + GameData.ASTEROID_LEVEL3_PROBABILITY))
			level4_roll = int(random() * (1 + GameData.ASTEROID_LEVEL4_PROBABILITY))

			level_rolls = [level0_roll, level1_roll, level2_roll, level3_roll, level4_roll]
			highest_roll = level0_roll
			level = 0
			for i in range(5):
				if level_rolls[i] > highest_roll: 
					level = i
					highest_roll = level_rolls[i]
			# Level is 0 to 4 inclusive.

		# Constant speed
		speed = 1.0

		# Random location, random direction
		# It starts on either the top edge of the left edge, not the right or the bottom.
		# Since they border wrap, the direction may send them immediately to the right or bottom border.
		if (position == None):
			sx, sy = self.screen_size
			orientation = random()
			if (orientation < 0.5):
				x = 0
				y = random() * sy
			else:
				x = random() * sx
				y = 0
			position = (x, y)

		angle = random() * 360
		dx = math.cos(math.radians(angle)) * speed
		dy = math.sin(math.radians(angle)) * speed
		direction = (dx, dy)

		# Create and return a random asteroid.
		asteroid = Asteroid(self.screen_size, level, [self.images[level]], direction, position, self.rotation_speed, angle)
		return asteroid


class AsteroidField():
	def __init__(self, screen_size, events):
		self.screen_size = screen_size
		self.asteroid_factory = AsteroidFactory(self.screen_size)
		self.cooldown = Cooldown(GameData.NEW_ASTEROID_FREQUENCY)
		self.asteroids = []
		self.events = events
		self.watch_game_events()
		self.max_asteroids = GameData.MAX_ASTEROIDS 	# for performance. :(  Not tuned yet.
	def watch_game_events(self):
		self.events.on_earth_collision.add_listener(EventListener(self.destroy_asteroid))
		self.events.on_weapon_collision.add_listener(EventListener(self.weapon_collision_handler))
		self.events.on_game_over.add_listener(EventListener(self.game_over_handler))
	def weapon_collision_handler(self, event_args):
		weapon = event_args.data.weapon
		asteroid = event_args.data.asteroid
		asteroid.take_damage(weapon.damage)
		if asteroid.is_destroyed():
			self.destroy_asteroid(event_args)
	def create_asteroids(self):
		isready = self.cooldown.calculate() and (len(self.asteroids) < self.max_asteroids)
		if isready:
			if len(self.asteroids) < self.max_asteroids:
				self.cooldown.fire()
				new_asteroid = self.asteroid_factory.CreateAsteroid()
				self.asteroids.append(new_asteroid)
	def move_asteroids(self):
		for asteroid in self.asteroids:
			asteroid.animate()
			asteroid.move()
	def render(self, screen):
		for asteroid in self.asteroids:
			asteroid.render(screen)
	def destroy_asteroid(self, event_args):
		asteroid = event_args.data.asteroid
		if(asteroid.level > 0):
			# If this was a larger asteroid, it broke up into a bunch of smaller pieces.
			# We used to break up into a few shards of the next smaller level but not anymore.
			# Now we break up into several level 0 shards.

			# old_position = asteroid.position
			# old_level = asteroid.level
			# breakdown_table  = {1:0, 2:2, 3:1, 4:1, 5:1}
			# new_count = breakdown_table[old_level]
			# new_level = old_level - 1
			# for j in range(new_count):
			# 	new_asteroid = self.asteroid_factory.CreateAsteroid(new_level, old_position)
			# 	self.asteroids.append(new_asteroid)

			old_position = asteroid.position
			old_level = asteroid.level
			new_count = (int(old_level * GameData.ASTEROID_SHARD_MULTIPLIER))
			new_level = 0
			#print("Sharding into " +str(new_count)+ " pieces.");
			for j in range(new_count):
				new_asteroid = self.asteroid_factory.CreateAsteroid(new_level, old_position)
				self.asteroids.append(new_asteroid)
			self.events.asteroid_breakup(self)

		# Destroy this asteroid.
		if asteroid in self.asteroids:
			self.asteroids.remove(asteroid)
	def game_over_handler(self, event_args):
		for asteroid in self.asteroids:
			asteroid.position = (0,0)
			asteroid.direction = (0.0, 0.0)
		self.asteroids.clear()

	