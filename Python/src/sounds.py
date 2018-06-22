import pygame
from config import *

class WeaponFireSoundListener:
	def __init__(self, sounds):
		self.sounds = sounds
		self.sound_map = {"Gun": self.sounds.play_gun, "Missile": self.sounds.play_missile}
	def trigger(self, event_args):
		weapon_name = event_args.data.weapon.weapon_name()
		f = self.sound_map[weapon_name]
		f()


class WeaponCollisionSoundListener:
	def __init__(self, sounds):
		self.sounds = sounds
	def trigger(self, event_args):
		weapon_collision_data = event_args.data
		asteroid = weapon_collision_data.asteroid
		self.sounds.play_asteroid_collision(asteroid.level)


class EarthCollisionSoundListener:
	def __init__(self, sounds):
		self.sounds = sounds
	def trigger(self, event_args):
		earth_collision_data = event_args.data
		asteroid = earth_collision_data.asteroid
		earth = earth_collision_data.earth
		self.sounds.play_earth_collision(earth, asteroid)

class AsteroidBreakupListener:
	def __init__(self, sounds):
		self.sounds = sounds
	def trigger(self, event_args):
		self.sounds.play_asteroid_breakup()


class Sounds:
	def __init__(self, events):
		self.sound_gun = pygame.mixer.Sound(GameData.SOUND_GUN_FILENAME)
		self.sound_missile = pygame.mixer.Sound(GameData.SOUND_MISSILE_FILENAME)
		self.sound_multimissile = pygame.mixer.Sound(GameData.SOUND_MULTIMISSILE_FILENAME)
		self.sound_asteroid_collision = pygame.mixer.Sound(GameData.SOUND_ASTEROID_COLLISION_FILENAME)
		self.sound_earth_collision = [
			pygame.mixer.Sound(GameData.SOUND_EARTH_COLLISION0_FILENAME),
			pygame.mixer.Sound(GameData.SOUND_EARTH_COLLISION1_FILENAME),
			pygame.mixer.Sound(GameData.SOUND_EARTH_COLLISION2_FILENAME),
			pygame.mixer.Sound(GameData.SOUND_EARTH_COLLISION3_FILENAME),
			pygame.mixer.Sound(GameData.SOUND_EARTH_COLLISION4_FILENAME)
		]
		self.sound_asteroid_breakup = pygame.mixer.Sound(GameData.SOUND_ASTEROID_BREAKUP_FILENAME)
		self.events = events
		if (GameData.SOUND_ON):
			self.watch_game_events(self.events)
	def watch_game_events(self, game_events):
		game_events.on_play_fire.add_listener(WeaponFireSoundListener(self))
		game_events.on_play_earth_collision.add_listener(EarthCollisionSoundListener(self))
		game_events.on_play_weapon_collision.add_listener(WeaponCollisionSoundListener(self))

		game_events.on_fire.add_listener(WeaponFireSoundListener(self))
		game_events.on_earth_collision.add_listener(EarthCollisionSoundListener(self))
		game_events.on_weapon_collision.add_listener(WeaponCollisionSoundListener(self))
		game_events.on_asteroid_breakup.add_listener(AsteroidBreakupListener(self))
	def play_gun(self):
		self.sound_gun.stop()
		self.sound_gun.play()
	def play_missile(self):
		self.sound_missile.stop()
		self.sound_missile.play()
	def play_asteroid_collision(self, level):
		self.sound_asteroid_collision.play()
	def play_earth_collision(self, earth, asteroid):
		self.sound_earth_collision[asteroid.level].play()
	def play_background(self):
		pygame.mixer.music.load(GameData.SOUND_BACKGROUND_FILENAME)
		pygame.mixer.music.set_volume(0.4)
		pygame.mixer.music.play(-1)
	def play_asteroid_breakup(self):
		self.sound_asteroid_breakup.stop()
		self.sound_asteroid_breakup.play()
