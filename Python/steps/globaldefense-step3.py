###############################################################################
# STEP 3 - Asteroids
###############################################################################
# Draw the asteroid field on the screen.
###############################################################################

import pygame
import pygame.mouse
from pygame.locals import *
import sys
import directions
import game


pygame.mixer.pre_init(22050, -16, 2, 256)
pygame.init()
pygame.mixer.init()

screen_size = (640, 480) 
screen = pygame.display.set_mode([screen_size[0] - 1, screen_size[1] - 1])
g = game.Game(screen_size, screen)

while True:
	g.clock.tick(1000/30)

	for event in pygame.event.get():
		# Pay attention if the user clicks the X to quit.
		if event.type == pygame.QUIT:
			sys.exit()

	# Draw the sky.
	g.sky.render(g.screen)

	# Create new asteroids if needed
	g.field.create_asteroids()
	# Move and animate asteroids
	g.field.move_asteroids()
	# Draw asteroids
	g.field.render(g.screen)

	# Put the scene on the monitor.
	pygame.display.update()

# End of game loop.
