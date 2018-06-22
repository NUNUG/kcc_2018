###############################################################################
# STEP 6 - Keyboard states
###############################################################################
# Read key states from the keyboard.
# Fire a weapon while a key is pressed.
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

		# Watch for mouse movement.  Tell the earth where the mouse is pointing.
		if event.type == pygame.MOUSEMOTION:
			mousepos = pygame.mouse.get_pos()
			a = directions.angle_of_point(mousepos, g.earth.origin)
			g.earth.set_angle(a)

	# Check the keyboard for button states. (These buttons can be held down.)
	keys = pygame.key.get_pressed()
	btn_f = keys[K_f]

	# Fire weapons (for these weapons, you can hold down the button).
	if (btn_f):
		g.weapons.fire_gun(g.earth.angle, g.earth.launch_position)

	# Draw the sky.
	g.sky.render(g.screen)

	# Draw the earth
	g.earth.render(g.screen)

	# Move and animate weapons
	g.weapons.move_weapons()

	# Draw weapons
	g.weapons.render(g.screen)

	# Create new asteroids if needed
	g.field.create_asteroids()
	# Move and animate asteroids
	g.field.move_asteroids()
	# Draw asteroids
	g.field.render(g.screen)

	# Put the scene on the monitor.
	pygame.display.update()

# End of game loop.
