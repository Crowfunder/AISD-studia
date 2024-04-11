####################
# by Crowfunder
# copyright my ass
####################

from random import randint

class Lotto:
	def __init__(self, n_of_rolls):
		if n_of_rolls not in [5,6]:
			raise Exception("Improper number of rolls, choose 5 or 6.")
		rolls = []
		for _ in range(0,n_of_rolls):
			rolls.append(randint(0,48))
		self.rolls = rolls
	
	# overrides object rolls to desired
	def override(self, rolls):
		self.rolls = rolls
		return self


def SPRAWDZ(lotto_obj1, lotto_obj2):
	return sorted(lotto_obj1.rolls) == sorted(lotto_obj2.rolls)


def GRAJ(all_games, winning_game_obj):
	wins = 0
	for game_obj in all_games:
		if SPRAWDZ(winning_game_obj, game_obj):
			wins += 1
	return wins


def GRAJ_alt(game, winning_game_obj):
	'''
	Instructions were unclear, no idea if we're supposed to count number of winning games
	or count number of hits in an individual game, made two functions since idc not a single one is used
	'''
	difference = set(sorted(game.rolls)) - set(sorted(winning_game_obj))
	return len(game)-len(difference)


def main():
	all_games = []
	for _ in range(0,1000):
		all_games.append(Lotto(6))

	games_count = {}
	for game in all_games:
		try: 
			games_count[str(sorted(game.rolls))] += 1
		except:
			games_count[str(sorted(game.rolls))] = 1
	
	sorted_results = sorted(games_count.items(), key=lambda item: item[1])
	filename = (sorted_results[0][0] + sorted_results[1][0]).replace('][', '').replace(', ', '').strip('[]')
	with open(filename, 'w') as file:
		for result in sorted_results:
			file.write(str(result) + '\n')


if __name__ == '__main__':
	main()