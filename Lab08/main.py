####################
# by Crowfunder
# with love.
####################

from TSP_utils import ParseTSPFile, CalculatePathLength
from TSP_algorithms import PathFinderGreedy, PathFinderIterRoulette, PathFinderSimple
from TSP_tests import RouletteIterTester


def main():
	TSP_data = ParseTSPFile('Lab08/TSP.txt')

	# start_id = 36
	# end_id = 14

	# path_simple = PathFinderSimple(TSP_data, start_id, end_id)
	# path_greedy = PathFinderGreedy(TSP_data, start_id, end_id)
	# path_random_iter = PathFinderIterRoulette(TSP_data, start_id, end_id, 1)
	# print(CalculatePathLength(TSP_data, path_simple))
	# print(CalculatePathLength(TSP_data, path_greedy))
	# print(CalculatePathLength(TSP_data, path_random_iter))
	RouletteIterTester(TSP_data, 'roulette.csv', 300, repetitions=20)

if __name__ == '__main__':
	main()