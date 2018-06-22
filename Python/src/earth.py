import pygame
import math
from config import *
from events import EventListener

# def translate_rotation(originalsurface, rotatedsurface):
# 	oldrect = originalsurface.get_rect()
# 	newrect = rotatedsurface.get_rect()
# 	xoffset = (newrect.width - oldrect.width) / 2
# 	yoffset = (newrect.height - oldrect.height) / 2
# 	newrect = (oldrect.width + xoffset, oldrect.height + yoffset)
# 	return newrect
# 		r_earth = pygame.transform.rotate(self.earth_image, self.angle)
# 		r_earth_rect = r_earth.get_rect()
# 		width_offset = (r_earth_rect.width - self.earth_rect.width)  / 2
# 		height_offset = (r_earth_rect.height - self.earth_rect.height) / 2



class Earth(pygame.sprite.Sprite):
	def __init__(self, screen_size, events):
		self.earth_size = (100, 100)
		self.earth_radius = self.earth_size[0]/2
		self.events = events
		self.watch_game_events()
		# self.sounds = sounds
		# Set origin
		width, height = screen_size
		self.origin_x = width / 2
		self.origin_y = height / 2
		self.origin = (self.origin_x, self.origin_y)
		self.pointer_radius = 5
		# Load Earth image
		self.earth_image = pygame.transform.scale(pygame.image.load(GameData.GRAPHICS_EARTH_FILENAME), self.earth_size)
		#self.earth_rect = self.earth_image.get_rect()
		self.rect = self.earth_image.get_rect()
		self.rect.centerx = self.origin_x
		self.rect.centery = self.origin_y
		# Create the pointer image
		self.launcher_image = pygame.surface.Surface((self.pointer_radius * 2, self.pointer_radius * 2))
		pygame.draw.circle(self.launcher_image, (255, 0, 0), (self.pointer_radius, self.pointer_radius), self.pointer_radius, 0)
		# Precalculate launcher orbit
		self._precalculate_pointer_location_offset_array(self.earth_radius)
		self.set_angle(0)
		# Endurance
		self.total_endurance = 100.0
		self.remaining_endurance = self.total_endurance
	def watch_game_events(self):
		self.events.on_earth_collision.add_listener(EventListener(self.earth_collision_handler))
		self.events.on_game_start.add_listener(EventListener(self.game_start_handler))
	def game_start_handler(self, event_args):
		self.remaining_endurance = self.total_endurance
	def earth_collision_handler(self, event_args):
		# The asteroid which we currently reference does not get destroyed when we restart the game.  We need to drop it so it gets released.
		asteroid = event_args.data.asteroid
		asteroid_field = event_args.data.asteroid_field
		self.take_damage(asteroid)
		
	def _precalculate_pointer_location_offset_array(self, earth_radius):
		# Go through 360 angles and calculate the x,y offset from an origin for each.
		self.launch_positions = []
		for angle in range(360):
			x = math.cos(math.radians(angle)) * self.earth_radius
			y = math.sin(math.radians(angle)) * self.earth_radius
			vector = (x, y)
			self.launch_positions.append(vector)
	def set_origin(self, origin):
		self.origin = origin
	def set_angle(self, angle):
		self.angle = angle % 360
		x, y = self.origin
		ox, oy = self.launch_positions[int(self.angle)]
		self.launch_position = (x + ox, y + oy)
	def change_angle(self, angledelta):
		#self.angle = (self.angle + angledelta) % 360
		self.set_angle(self.angle + angledelta)
	def render(self, screen):
		x, y = self.origin
		# Blit the launcher
		ox, oy = self.launch_positions[int(self.angle)]
		screen.blit(self.launcher_image, (x + ox - self.pointer_radius, y + oy - self.pointer_radius))
		
		# Stationary blit of earth
		screen.blit(self.earth_image, (x - self.earth_radius, y - self.earth_radius))
		if (GameData.debug_mode and False):
			pygame.draw.rect(screen, [255, 0, 255], self.rect, 4)
		
		
		# Rotated blit of earth (works)
		# r_earth = pygame.transform.rotate(self.earth_image, self.angle)
		# r_earth_rect = r_earth.get_rect()
		# width_offset = (r_earth_rect.width - self.earth_rect.width)  / 2
		# height_offset = (r_earth_rect.height - self.earth_rect.height) / 2
		# screen.blit(r_earth, (x - self.earth_radius - width_offset, y - self.earth_radius - height_offset))
	def take_damage(self, asteroid):
		#self.remaining_endurance = self.remaining_endurance - asteroid.remaining_endurance
		self.remaining_endurance = self.remaining_endurance - asteroid.potential_damage
		if (self.remaining_endurance < 1.0):
			self.remaining_endurance = 0
	def is_destroyed(self):
		return self.remaining_endurance < 1.0		
		
	
