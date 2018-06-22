import pygame
from pygame.locals import *
import config
import sys
from events import EventListener


class GameOver:
	def __init__(self, screen, screen_size, events):
		self.screen = screen
		self.screen_size = screen_size
		self.events = events
		self.watch_game_events()
	def watch_game_events(self):
		self.events.on_game_over.add_listener(EventListener(self.game_over_handler))
	def game_over_handler(self, event_args):
		self.show()
	def show(self):
		print("Game Over")
		# Capture the screen as-is
		old_screen = pygame.Surface(self.screen_size)
		old_screen.blit(self.screen, (0,0))
		new_screen = pygame.Surface(self.screen_size)
		new_alpha = 0

		# Mini game loop
		clock = pygame.time.Clock()
		while (True):
			
			clock.tick(1000/30)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			keys = pygame.key.get_pressed()

			btn_escape = keys[K_ESCAPE]
			if (btn_escape):
				sys.exit()

			btn_space = keys[K_SPACE]
			if (btn_space):
				break

			# Compose new screen surface
			new_screen.fill([0,0,0])

			screen_width, screen_height = self.screen_size
			background = pygame.Surface(self.screen_size)
			background.fill([0,0,0])
			game_over_text = pygame.image.load(config.GameData.GRAPHICS_GAME_OVER_TEXT)
			x = int((screen_width - game_over_text.get_rect().width) / 2)
			#y = int((screen_height - text.get_rect().height) / 2)
			y = int(screen_height / 2) - game_over_text.get_rect().height
			new_screen.blit(game_over_text, (x, y))

			press_space_text = pygame.image.load(config.GameData.GRAPHICS_PRES_SPACE_TEXT)
			x = int((screen_width - press_space_text.get_rect().width) / 2)
			y = int((screen_height / 2) + 15)
			new_screen.blit(press_space_text, (x, y))

			if (new_alpha <= 255):
				new_alpha = new_alpha + 5
			else:
				new_alpha = 255

			new_screen.set_alpha(new_alpha)

			self.screen.blit(old_screen, (0,0))
			self.screen.blit(new_screen, (0,0))
			pygame.display.update()


