################################################################################
# Weapons system.
# The weapons system has the following weapons:
#
# - Gun.  A rapid-fire stream of artillery bullets that do minimal damage.  Each is a circle.
#   One bullet is just powerful enough to take one of the smallest asteroid shards.
#
# - Shrapnel MultiGun.  A burst of garbage is shot into space.  
#   Each piece is actually a bullet.  They fan out in a wide angle.
#
# - Missile. A single-shot rocket that can do massive damage.  
#   Four shots from this will break up the largest asteroid.
#
# - MultiMissile array. Several weaker, slower missiles launch together in formation.
# - Cluster. A missile which explodes into 20 missiles upon impact
#
################################################################################

import pygame
import math
from random import random
from directions import Directions
from projectile import *
from cooldown import * 
from sounds import Sounds
from events import EventListener
from config import *
from game_events import GameEvents, WeaponFireEventData, RequestScoreEventData

class Weapon(Projectile):
	def __init__(self, images, direction, position, damage):
		Projectile.__init__(self, images, direction, position)
		self.damage = damage
		self.acceleration = 0.0
	def damage_asteroid(self, asteroid):
		asteroid.take_damage(self.damage)
	def detonate(self):
		pass
	def weapon_name(self):
		return "Unknown Weapon"
	def upgrade(self):
		pass

class GunWeapon(Weapon):
	def __init__(self, images, direction, position, damage):
		Weapon.__init__(self, images, direction, position, damage)
	def detonate(self):
		pass
	def weapon_name(self):
		return "Gun"
class MissileWeapon(Weapon):
	def __init__(self, images, direction, position, damage, acceleration, max_speed):
		Weapon.__init__(self, images, direction, position, damage)
		self.acceleration = acceleration
		self.max_speed = max_speed
	def detonate(self):
		pass
	def weapon_name(self):
		return("Missile")

class GunFactory():
	"""Creates instances of the GUN weapon."""
	def __init__(self, directions):
		self.directions = directions
		self.radius = 3
		self.image = pygame.surface.Surface((self.radius, self.radius))
		pygame.draw.circle(self.image, (255, 255, 255), (int(self.radius / 2.0), int(self.radius / 2.0)), self.radius, 0)
		self.speed = GameData.WEAPON_GUN_SPEED
		self.level = 0
		self.gun_damage = GameData.WEAPON_GUN_DAMAGE
		self.multigun_damage = GameData.WEAPON_MULTIGUN_DAMAGE
		self.shot_count = GameData.WEAPON_MULTIGUN_SHOT_COUNT
		self.spread = GameData.WEAPON_MULTIGUN_SPREAD
		self.fan = GameData.WEAPON_MULTIGUN_FAN
		self.multigun_speed = self.speed * GameData.WEAPON_MULTIGUN_SPEED_MULTIPLIER
	def create_multishot(self, angle, position):
		result = []
		for j in range(self.shot_count):
			xoffset = random() * self.spread + 1
			xoffset = xoffset - (xoffset / 2)
			yoffset = random() * self.spread + 1
			yoffset = yoffset - (yoffset / 2)
			px, py = position
			newpos = (px + xoffset, py + yoffset)
			weapon = self.create_weapon_with_detail(int(angle - j * self.fan), newpos, self.multigun_speed, self.multigun_damage)
			result.append(weapon)
			weapon = self.create_weapon_with_detail(int(angle + j * self.fan), newpos, self.multigun_speed, self.multigun_damage)
			result.append(weapon)
		return result
	def create_weapon_with_detail(self, angle, position, speed, damage):
		x, y = self.directions[angle % 360]
		x2 = x * speed
		y2 = y * speed
		vector = (x2, y2)
		gun = GunWeapon([self.image], vector, position, damage)
		for j in range(self.level):
			gun.upgrade()
		return gun
	def create_weapon(self, angle, position):
		gun = self.create_weapon_with_detail(angle, position, self.speed, self.gun_damage)
		return gun
	def upgrade(self):
		print("Upgrading to level " + str(self.level + 1))
		self.level = self.level + 1
		self.speed = self.speed + 2.0
		self.gun_damage = self.gun_damage + 2.0
		self.spread = self.spread + 5
		self.shot_count = self.shot_count + 1

class MissileFactory():
	"""Creates instances of the Missile weapon."""
	def __init__(self, directions):
		self.directions = directions
		self.radius = 3
		#self.image = pygame.surface.Surface((self.radius, self.radius))
		self.images = []
		self.images.append(pygame.image.load(GameData.GRAPHICS_MISSILE1_FILENAME))
		self.images.append(pygame.image.load(GameData.GRAPHICS_MISSILE2_FILENAME))
		self.damage = GameData.WEAPON_MISSILE_DAMAGE
		self.speed = GameData.WEAPON_MISSILE_SPEED
		self.acceleration = GameData.WEAPON_MISSILE_ACCELERATION
		self.max_speed = GameData.WEAPON_MISSILE_MAX_SPEED
	def create_weapon(self, angle, position):
		x, y = self.directions[angle % 360]
		x2 = x * self.speed
		y2 = y * self.speed
		vector = (x2, y2)
		image1 = pygame.transform.rotate(self.images[0], 360 - ((90 + angle) % 360))
		image2 = pygame.transform.rotate(self.images[1], 360 - ((90 + angle) % 360))
		return MissileWeapon([image1, image2], vector, position, self.damage, self.acceleration, self.max_speed)
	def upgrade(self):
		self.speed = self.speed + 3
		

class MultiMissileFactory(MissileFactory):
	"""Creates instances of the Missile weapon."""
	def __init__(self, directions):
		self.directions = directions
		self.radius = 3
		#self.image = pygame.surface.Surface((self.radius, self.radius))
		self.images = []
		self.images.append(pygame.image.load(GameData.GRAPHICS_MISSILE1_FILENAME))
		self.images.append(pygame.image.load(GameData.GRAPHICS_MISSILE2_FILENAME))
		self.damage = GameData.WEAPON_MULTIMISSILE_DAMAGE
		self.speed = GameData.WEAPON_MULTIMISSILE_SPEED
		self.acceleration = GameData.WEAPON_MULTIMISSILE_ACCELERATION
		self.max_speed = GameData.WEAPON_MULTIMISSILE_MAX_SPEED
		self.shot_count = GameData.WEAPON_MULTIMISSILE_SHOT_COUNT
		self.fan = GameData.WEAPON_MULTIMISSILE_FAN
	def create_weapon(self, angle, position):
		result = []
		leftmost_angle = angle - self.fan * (self.shot_count / 2 + 1)
		for j in range(1, self.shot_count):
			newangle = int(leftmost_angle + j * self.fan)
			x, y = self.directions[newangle % 360]
			x2 = x * self.speed
			y2 = y * self.speed
			vector = (x2, y2)
			image1 = pygame.transform.rotate(self.images[0], 360 - ((90 + newangle) % 360))
			image2 = pygame.transform.rotate(self.images[1], 360 - ((90 + newangle) % 360))
			missile = MissileWeapon([image1, image2], vector, position, self.damage, self.acceleration, self.max_speed)
			result.append(missile)
		return result
	def upgrade(self):
		self.speed = self.speed + 3
		

# class weapons_set():
# 	def __init__(self, directions):
# 		self.directions = directions
# 		self.gun_factory = GunFactory(directions)
# 		self.gun_cooldown = Cooldown(100)

class WeaponSystem():
	"""Creates, tracks, animates and destroys all weapons and destructions."""
	def __init__(self, screen_size, earth, events):
		self.screen_size = screen_size
		self.earth_origin = earth.origin
		self.earth_radius = earth.earth_radius
		self.weapons = []
		# Gun parts
		self.gun_cooldown = Cooldown(GameData.WEAPON_GUN_COOLDOWN)
		self.multigun_cooldown = Cooldown(GameData.WEAPON_MULTIGUN_COOLDOWN)
		self.gun_factory = GunFactory(Directions(1.0))
		self.missile_cooldown = Cooldown(GameData.WEAPON_MISSILE_COOLDOWN)
		self.missile_factory = MissileFactory(Directions(1.0))
		self.multimissile_cooldown = Cooldown(GameData.WEAPON_MULTIMISSILE_COOLDOWN)
		self.multimissile_factory = MultiMissileFactory(Directions(1.0))
		#Events
		self.events = events
		self.watch_game_events()
		#self.on_fire = Event("on_fire")
	# def _precalc_directions(self):
	# 	self.directions = []
	# 	r = 1.0	# Default radius should be the slowest that anything goes.
	# 	for angle in range(360):
	# 		x = math.cos(math.radians(angle)) * r
	# 		y = math.sin(math.radians(angle)) * r
	# 		vector = (x, y)
	# 		self.directions.append(vector)
	def watch_game_events(self):
		self.events.on_game_over.add_listener(EventListener(self.game_over_handler))
		self.events.on_weapon_collision.add_listener(EventListener(self.weapon_collision_handler))
	def game_over_handler(self, event_args):
		self.weapons.clear()
	def weapon_collision_handler(self, event_args):
		weapon = event_args.data.weapon
		#if (weapon.weapon_name() == "Gun"):
			#self.remove_weapon(weapon)
		# Remove all weapons upon collision.
		# if (weapon.weapon_name() == "Missile"):
		# 	print("Removing missile... " + str(weapon))
		self.remove_weapon(weapon)
	# def upgrade_weapons(self):
	# 	print("Attempt to retrieve score.")
	# 	score_data = RequestScoreEventData()
	# 	self.events.request_score(self, score_data)
	# 	score = score_data.get_score()
	# 	print("Score: " + str(score))
	# 	if (score > 1):
	# 		print("Upgrading factory")
	# 		self.gun_factory.upgrade()
	# 		self.events.upgrade_weapons(self)
	def fire_gun(self, angle, position):
		# Check cooldown
		isready = self.gun_cooldown.calculate()
		if isready:
			# Create a bullet
			newgun = self.gun_factory.create_weapon(angle, position)
			self.gun_cooldown.fire()
			# Add the bullet to the weapons list
			self.weapons.append(newgun)
			## Play the sound
			#self.sounds.play_gun()
			#self.events.on_fire.trigger(self, "gun")
			#self.events.on_fire.trigger(self, WeaponFireEventData(newgun))
			self.events.fire(self, newgun)
	def fire_multigun(self, angle, position):
		# Check cooldown
		isready = self.multigun_cooldown.calculate()
		if isready:
			# Create a bullet
			newguns = self.gun_factory.create_multishot(angle, position)
			self.multigun_cooldown.fire()
			for newgun in newguns:
				# Add the bullet to the weapons list
				self.weapons.append(newgun)
				## Play the sound
				#self.sounds.play_gun()
				#self.events.on_fire.trigger(self, "gun")
				#self.events.on_fire.trigger(self, WeaponFireEventData(newgun))
				self.events.fire(self, newgun)
	def fire_missile(self, angle, position):
		isready = self.missile_cooldown.calculate()
		if isready:
			newmissile = self.missile_factory.create_weapon(angle, position)
			self.missile_cooldown.fire()
			self.weapons.append(newmissile)
			self.events.fire(self, newmissile)
	def fire_multimissile(self, angle, position):
		isready = self.multimissile_cooldown.calculate()
		if isready:
			missiles = self.multimissile_factory.create_weapon(angle, position)
			self.multimissile_cooldown.fire()
			for missile in missiles:
				self.weapons.append(missile)
				self.events.fire(self, missile)
	def move_weapons(self):
		# Go through each weapon in the weapons list, move it and animate it.
		for weapon in self.weapons:
			weapon.animate()
			weapon.move()
		# Remove runaway weapons
		c = len(self.weapons)
		sx, sy = self.screen_size
		for j in range(c):
			i = c - j - 1	# count backward
			w = self.weapons[i]
			px, py = w.position
			if (px < 0) or (px > sx) or (py < 0) or (py > sy):
				del self.weapons[i]
	def render(self, screen):
		for weapon in self.weapons:
			weapon.render(screen)
	def remove_weapon(self, weapon):
		if weapon in self.weapons:
			self.weapons.remove(weapon)
