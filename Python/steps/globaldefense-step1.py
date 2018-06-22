###############################################################################
# STEP 1 - Game Loop
###############################################################################
# Create a blank window with a game loop.
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


# End of game loop.
