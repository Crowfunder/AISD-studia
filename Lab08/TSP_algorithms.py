####################
# by Crowfunder
# with love.
####################

import math
from TSP_utils import PointDistance, RandomizePath, CalculatePathLength


def PathFinderSimple(TSP_data, start_id, end_id):
	"""
	Finds a simple path from start_id to end_id in the TSP_data.

	Args:
		TSP_data (dict): A dictionary containing the TSP data.
		start_id (int): The starting point ID.
		end_id (int): The ending point ID.

	Returns:
		list: A list of point IDs representing the path from start_id to end_id.
	"""
	path_ids = list(TSP_data.keys())
	for _ in range(start_id-1):
		path_ids.append(path_ids.pop(0))

	path_ids.remove(end_id)
	path_ids.append(end_id)

	return path_ids


def PathFinderGreedy(TSP_data, start_id, end_id):
	"""
	Finds a greedy path from start_id to end_id in the TSP_data.

	Args:
		TSP_data (dict): A dictionary containing the TSP data.
		start_id (int): The starting point ID.
		end_id (int): The ending point ID.

	Returns:
		list: A list of point IDs representing the path from start_id to end_id.
	"""
	ids_unvisited = list(TSP_data.keys())
	ids_visited = []
	ids_unvisited.remove(end_id)

	while ids_unvisited:
		ids_visited.append(start_id)
		ids_unvisited.remove(start_id)

		best_len = math.inf
		best_id = 0

		for new_id in ids_unvisited:
			new_len = PointDistance(TSP_data, start_id, new_id)
			if new_len < best_len:
				best_len = new_len
				best_id = new_id
		
		start_id = best_id

	ids_visited.append(end_id)
	return ids_visited


def PathFinderIterRoulette(TSP_data, start_id, end_id, iterations):
	"""
	Finds the best path from start_id to end_id in the TSP_data using the roulette algorithm.
	Randomize the path "iterations" times and pick the one with shortest length.

	Args:
		TSP_data (dict): A dictionary containing the TSP data.
		start_id (int): The starting point ID.
		end_id (int): The ending point ID.
		iterations (int): The number of iterations to perform.

	Returns:
		list: A list of point IDs representing the best path from start_id to end_id.
	"""
	path_best_ids = []
	path_best_len = math.inf

	for _ in range(iterations):
		path_new_ids = RandomizePath(TSP_data, start_id, end_id)
		path_new_len = CalculatePathLength(TSP_data, path_new_ids)
		if path_new_len < path_best_len:
			path_best_ids = path_new_ids
			path_best_len = path_new_len

	return path_best_ids