from BSTree import BSTrees
import numpy as np
from time import time
import random

SEPARATOR = '\n############################'

def GenerateAllDatasets(lengths: list[int]):
	output = {}
	for length in lengths:
		output[length] = GenerateOneDataset(length, length/10)
	return output


def GenerateOneDataset(length, max_float):
	return sorted(list(np.random.uniform(low=0.01, high=max_float, size=(length,)).round(2)))


def main():
	# sample_data = [1.3, 1.6, 3.7, 4.0, 4.99, 7.3, 7.8, 7.7, 7.9, 7.6, 9.3]
	# sample_trees = BSTrees(sample_data)
	# # sample_trees.PrintTree()
	# sample_trees.DataToTrees([6.99, 21.37, 21.33])
	# # sample_trees.PrintTree()
	# print(sample_trees.MaximumInTree(4))

	operation_iterations = 10000

	samples_dict = GenerateAllDatasets([25, 50, 100, 500, 1000])

	for length in samples_dict.keys():
		print(SEPARATOR)

		print(f'Dataset of {length} values in range (0.01, {length/10})')
		start = time()
		for _ in range(0,operation_iterations//100):
			test_trees = BSTrees(samples_dict[length])
		print(f'Insertion of values into BST: {(time()-start)/(length*operation_iterations)}s/sample')

		searched_float = samples_dict[length][length//2] # pick middle element from dataset
		start = time()
		for _ in range(0,operation_iterations):
			test = test_trees.SearchTree(searched_float)
		print(f'Search for value in BST: {(time()-start)/(length*operation_iterations)}s/sample')

		chosen_tree_id = random.choice(list(test_trees.root_dict.keys())) # pick random tree to search through
		start = time()
		for _ in range(0,operation_iterations):
			test = test_trees.MaximumInTree(chosen_tree_id)
		print(f'Maximum value in selected BST tree: {(time()-start)/(length*operation_iterations)}s/sample')
		
		start = time()
		for _ in range(0,operation_iterations):
			test = test_trees.MinimumInTree(chosen_tree_id)
		print(f'Minimum value in selected BST tree: {(time()-start)/(length*operation_iterations)}s/sample')





if __name__ == '__main__':
	main()