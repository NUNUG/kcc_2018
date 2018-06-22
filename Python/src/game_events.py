from events import Event

class WeaponFireEventData:
	def __init__(self, weapon):
		self.weapon = weapon

class WeaponCollisionEventData:
	def __init__(self, weapon, asteroid, weapon_system,  asteroid_field):
		self.weapon = weapon
		self.asteroid = asteroid
		self.weapon_system = weapon_system
		self.asteroid_field = asteroid_field

class EarthCollisionEventData:
	def __init__(self, earth, asteroid, asteroid_field):
		self.earth = earth
		self.asteroid = asteroid
		self.asteroid_field = asteroid_field

class RequestScoreEventData:
	def __init__(self):
		self.score = 0
	def set_score(self, value):
		self.score = value
	def get_score(self):
		return self.score

class GameEvents:
	def __init__(self):
		self.on_fire = Event("event_fire")
		self.on_earth_collision = Event("event_earth_collision")
		self.on_weapon_collision = Event("event_weapon_collision")
		self.on_game_over = Event("event_game_over")
		self.on_game_start = Event("event_game_start")
		self.on_score_changed = Event("event_score_changed")
		self.on_asteroid_destroyed = Event("event_asteroid_destroyed")
		self.on_asteroid_breakup = Event("event_asteroid_breakup")
		self.on_upgrade_weapons = Event("event_upgrade_weapons")
		self.on_request_score = Event("event_request_score")
		self.on_play_fire = Event("event_play_fire")
		self.on_play_earth_collision = Event("event_play_earth_collision")
		self.on_play_weapon_collision = Event("event_play_weapon_collision")
	def game_start(self, invoker, data):
		self.on_game_start.trigger(invoker, data)
	def game_over(self, invoker, data):
		self.on_game_over.trigger(invoker, data)
	def fire(self, invoker, weapon):
		self.on_fire.trigger(invoker, WeaponFireEventData(weapon))
	def weapon_collision(self, invoker, weapon, asteroid, weapon_system, asteroid_field):
		self.on_weapon_collision.trigger(invoker, WeaponCollisionEventData(weapon, asteroid, weapon_system, asteroid_field))
	def earth_collision(self, invoker, earth, asteroid, asteroid_field):
		self.on_earth_collision.trigger(invoker, EarthCollisionEventData(earth, asteroid, asteroid_field))
	def upgrade_weapons(self, invoker):
		self.on_upgrade_weapons.trigger(invoker, None)
	def request_score(self, invoker, request_score_event_args):
		self.on_request_score.trigger(invoker, request_score_event_args)
	def play_fire(self, invoker, weapon):
		self.on_play_fire.trigger(invoker, WeaponFireEventData(weapon))
	def play_weapon_collision(self, invoker, weapon, asteroid, weapon_system, asteroid_field):
		self.on_play_weapon_collision.trigger(invoker, WeaponCollisionEventData(weapon, asteroid, weapon_system, asteroid_field))
	def play_earth_collision(self, invoker, earth, asteroid, asteroid_field):
		self.on_play_earth_collision.trigger(invoker, EarthCollisionEventData(earth, asteroid, asteroid_field))		
	def asteroid_breakup(self, invoker):
		self.on_asteroid_breakup.trigger(invoker, None)
