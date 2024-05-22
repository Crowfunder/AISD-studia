####################
# by Crowfunder
# with love.
####################

import math
import random


def ParseTSPFile(fname):
	"""
	Parses a TSP file and returns a dictionary containing the TSP data.

	Args:
		fname (str): The filename of the TSP file.

	Returns:
		dict: A dictionary containing the TSP data, where the keys are the IDs and the values are tuples of (x, y) coordinates.
	"""
	TSP_data = {}
	with open(fname, 'r') as file:
		for line in file.readlines():
			line_data = line.split()
			TSP_data[int(line_data[0])] = (float(line_data[1]), float(line_data[2]))   # ID, x, y
	return TSP_data


def PointDistance(TSP_data, start_id, end_id):
	"""
	Calculates the Euclidean distance between two points in the TSP data.

	Args:
		TSP_data (dict): A dictionary containing the TSP data.
		start_id (int): The ID of the starting point.
		end_id (int): The ID of the ending point.

	Returns:
		float: The Euclidean distance between the two points.
	"""
	start = TSP_data[start_id]
	end = TSP_data[end_id]
	return math.sqrt((pow(start[0] - end[0], 2) + pow(start[1] - end[1], 2)))


def CalculatePathLength(TSP_data, id_visited: list[int]):
	"""
	Calculates the total length of a path given a list of visited point IDs.

	Args:
		TSP_data (dict): A dictionary containing the TSP data.
		id_visited (list[int]): A list of visited point IDs.

	Returns:
		float: The total length of the path.
	"""
	path_sum = 0
	path_len = len(id_visited)
	for i in range(path_len):
		if i != path_len - 1:
			path_sum += PointDistance(TSP_data, id_visited[i], id_visited[i + 1])

	return path_sum


def RandomizePath(TSP_data, start_id, end_id):
	"""
	Randomizes a path between two points in the TSP data.

	Args:
		TSP_data (dict): A dictionary containing the TSP data.
		start_id (int): The ID of the starting point.
		end_id (int): The ID of the ending point.

	Returns:
		list[int]: A list of point IDs representing the randomized path.
	"""
	path_ids = list(TSP_data.keys())

	path_ids.remove(start_id)
	path_ids.remove(end_id)

	random.shuffle(path_ids)

	path_ids.insert(0, start_id)
	path_ids.append(end_id)

	return path_ids