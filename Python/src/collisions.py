import math
import pygame
from asteroids import Asteroid, AsteroidField
from weapons import WeaponSystem
from config import *
from events import *



class CollisionHandler():
	def __init__(self, screen, score, events):
		self.screen = screen
		self.score = score
		#self.on_earth_collision = Event("on_earth_collision")
		#self.on_weapon_collision = Event("on_weapon_collision")
		self.events = events
		self.watch_game_events()
	def watch_game_events(self):
		pass
	def get_weapon_collisions(self, asteroid_field, weapon_system):
		result = []
		for asteroid in asteroid_field.asteroids:
			for weapon in weapon_system.weapons:
				if (self.is_weapon_collision(asteroid, weapon)):
					result.append((asteroid, weapon))
		return result
	def is_weapon_collision(self, asteroid, weapon):
		result = weapon.rect.colliderect(asteroid.rect)
		return result
	def handle_weapon_collision(self, asteroid, weapon, asteroid_field, weapon_system):
		self.events.weapon_collision(self, weapon, asteroid, weapon_system, asteroid_field)
		#self.score.asteroid_hit(asteroid)
		#weapon.damage_asteroid(asteroid)
		#if asteroid.is_destroyed():
			#asteroid_field.destroy_asteroid(asteroid)
			#self.score.asteroid_destroyed(asteroid)
			#TODO: Replace the above with this.
			#self.events.weapon_collision(this, weapon, asteroid, weapon_system);
		#weapon.detonate()
		#weapon_system.remove_weapon(weapon)
	def get_earth_collisions(self, asteroid_field, earth):
		result = []
		for asteroid in asteroid_field.asteroids:
			if (self.is_earth_collision(asteroid, earth)):
				result.append((asteroid, earth))
		return result
	def is_earth_collision(self, asteroid, earth):
		result = False
		within_bounds = earth.rect.colliderect(asteroid.rect)
		
		
		if (within_bounds and GameData.debug_mode):
			asteroid.collision_color = [255, 0, 0]
			px, py = asteroid.position
			p = (int(px), int(py))
			if (GameData.debug_mode):
				for r in range(10):
					pygame.draw.circle(self.screen, [0, 255, 255], p, int(r * 5 + 1), 1)
			
		# Earth is round, so do a special collision test for more accuracy:
		if (within_bounds):			
			# Find proximity of asteroid rect border to center of earth.
			asteroid_radius = int(asteroid.rect.width / 2)
			#cx, cy = asteroid.rect.center	# This is the center of the rect, relative to width / height, not x,y
			x, y = asteroid.position
			# cx = x + asteroid.rect.width
			# cy = y + asteroid.rect.height
			cx, cy = abs(x - earth.origin_x), abs(y - earth.origin_y)
			# We know that this is 0, 0, so omit the offset math for performance.
			#ex, ey = earth.earth_origin
			distance_from_center_to_center = math.sqrt( (cx * cx) + (cy * cy) )
			distance_from_center_to_earth_surface = distance_from_center_to_center - earth.earth_radius
			distance_from_asteroid_surface_to_earth_surface = distance_from_center_to_earth_surface - asteroid_radius
			if (distance_from_asteroid_surface_to_earth_surface <= 0.0):
				result = True
				# print("Collided with earth! ------------------------ ")
				# print("  x, y: " + str(x) + ",  " + str(y))
				# print("  cx, cy: " + str(cx)+", " +str(cy))
				# print("  asteroid_radius: " + str(asteroid_radius))
				# print("  distance_from_center_to_center: " + str(distance_from_center_to_center))
				# print("  distance_from_center_to_earth_surface: " + str(distance_from_center_to_earth_surface))
				# print("  distance_from_asteroid_surface_to_earth_surface: " + str(distance_from_asteroid_surface_to_earth_surface))
		return result
	def handle_earth_collisions(self, asteroid_field, asteroid, earth):
		# TODO: Trigger the game event for earth collisions here, then move these lines to the earth listener and asteroid listener
		#earth.take_damage(asteroid.remaining_endurance, asteroid.level)
		#asteroid_field.destroy_asteroid(asteroid)
		self.events.earth_collision(self, earth, asteroid, asteroid_field)
		if (earth.is_destroyed()):
			self.events.game_over(self, None)
			self.events.game_start(self, None)
		
		# if not earth.is_destroyed:
		# 	print("Earth is not destroyed.")
		# 	self.events.play_earth_collision(self, earth, asteroid, asteroid_field)
		
