import sys

import pygame


class AlienInvasion:
	"""Overall class to manage game assets and behavior"""

	def __init__(self):
		"""Initialize the game and create game resources"""
		pygame.init()

		self.screen = pygame.display.set_mode((1200, 900))
		pygame.display.set_caption("Alien Invasion")

		# set the backround color
		self.bg_color = (200, 245, 200)



	def run_game(self):
		"""Start the main loop for the game"""
		while True:
		 # Watch for keyboard and mouse movements 
		 for event in pygame.event.get():
		 	if event.type == pygame.QUIT:
		 		sys.exit()
		 # redraw the screen during pass through each loop
		 self.screen.fill(self.bg_color)

		 # Make the most recently drawn screen visible
		 pygame.display.flip()


if __name__ == '__main__':
	# make the game instance and run the game
	ai = AlienInvasion()	
	ai.run_game()

