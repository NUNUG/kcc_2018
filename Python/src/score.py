from events import EventListener
from game_events import *

class Score:
	def __init__(self, events):
		self.events = events
		self.hit_score = 10
		self.reset(None)
		self.watch_game_events()
	def watch_game_events(self):
		self.events.on_game_start.add_listener(EventListener(self.reset))
		self.events.on_weapon_collision.add_listener(EventListener(self.asteroid_destroyed))
		self.events.on_upgrade_weapons.add_listener(EventListener(self.weapon_upgrade))
		self.events.on_request_score.add_listener(EventListener(self.score_requested))
	def reset(self, event_args):
		self.score = 0
	def screen_cleared(self):
		self.score = self.score * 2
	def asteroid_destroyed(self, event_args):
		asteroid = event_args.data.asteroid
		self.score = self.score + self.hit_score * (asteroid.level + 1)
	def weapon_upgrade(self, data):
		self.score = self.score - 10000
		if (self.score < 0):
			self.score = 0
	def asteroid_hit(self, asteroid):
		self.score = self.score + self.hit_score
	def score_requested(self, event_args):
		score_data = event_args.data
		print("Score request detected.  Current score: " + str(self.score))
		#score_data.score = self.score
		print("Score arg type: " + repr(score_data))
		event_args.data.set_score(self.score)
		print("Set result to: " + str(score_data.score))