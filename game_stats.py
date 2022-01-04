import json


class GameStats:
	""" Track stats for alien invasion"""

	def __init__(self, ai_game):
		"""initialize statistics"""
		self.settings = ai_game.settings
		self.reset_stats()

		# Start game in an inactive state
		self.game_active = False

		self.high_score = self.get_saved_high_score()

	def get_saved_high_score(self):
		"""Get high score from file, if not it exits"""
		try:
			with open('high_score.json') as f:
				return json.load(f)
		except FileNotFoundError:
			return 0

	def reset_stats(self):
		"""initialize stats that can change during the game"""
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1
