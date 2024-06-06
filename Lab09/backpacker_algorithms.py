######################
# by Crowfunder
# with love
######################

import random
from backpacker_classes import Backpack

def BackpackerGreedy(packages_list, size):
	"""
	Greedy algorithm for packing packages into a backpack.
	Sort all packages based on value to size ratio and insert them in that order

	Parameters:
	size (int): Size of the backpack.
	packages_list (list): List of package objects.

	Returns:
	Backpack: The backpack object after packing the packages.
	"""
	packages_list.sort(key=lambda x: x.gain, reverse=True)
	backpack = Backpack(size)
	for package_obj in packages_list:
		backpack.insert_package(package_obj)

	return backpack


def BackpackerGambler(packages_list, size, iterations):
	"""
	Gambler algorithm for packing packages into a backpack.
	Shuffle packages, insert them in that order {iterations} times
	and pick the best result.

	Parameters:
	size (int): Size of the backpack.
	packages_list (list): List of package objects.
	iterations (int): Number of iterations for the gambler algorithm.

	Returns:
	Backpack: The backpack object after packing the packages.
	"""
	backpack = Backpack(size)
	for _ in range(iterations):
		backpack.save_state()
		random.shuffle(packages_list)
		for package_obj in packages_list:
			backpack.insert_package(package_obj)

		if backpack.total_value < backpack.prev_state.total_value:
			backpack.restore_state()

	return backpack


def BackpackerULTRAGREED(packages_list, size):
	"""
	ULTRAGREED algorithm for packing packages into a backpack.
	Get gains from all possible moves and pick the best one

	Parameters:
	size (int): Size of the backpack.
	packages_list (list): List of package objects.

	Returns:
	Backpack: The backpack object after packing the packages.
	"""
	# We will be removing elements from this list, so we don't want it 
	# as reference, but rather as a copy
	packages_list = packages_list.copy()
	backpack = Backpack(size)

	while True:
		packages_gains = {}
		for package_obj in packages_list:
			backpack.save_state()
			if backpack.insert_package(package_obj):
				packages_gains[package_obj] = backpack.gains
				backpack.restore_state()

		# Get all choices with biggest gain
		best_choices = [pkg for pkg in packages_gains if packages_gains[pkg] == max(packages_gains.values())]

		# Break the loop if out of choices
		if not best_choices:
			break

		package_best = best_choices[0]
		backpack.save_state()
		backpack.insert_package(package_best)
		packages_list.remove(package_best)

	return backpack