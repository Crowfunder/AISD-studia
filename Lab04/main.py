##############################################
# by Crowfunder
# my hatred towards mergesort is immeasurable
# and my day is ruined
##############################################

from random import randint
from time import time

# https://www.youtube.com/watch?v=Q1JdRUh1_98
def InsertionSort(input_list):
	"""
	Sorts a list in ascending order using the Insertion Sort algorithm.

	Parameters:
	input_list (list): The list to be sorted.

	Returns:
	list: The sorted list.
	"""
	for i in range(1, len(input_list)):
		x = input_list[i]
		j = i-1
		while j >= 0 and input_list[j] > x:
			input_list[j+1] = input_list[j]
			j -= 1
		input_list[j+1] = x
	return input_list


def MergeSort(input_list, list_start, list_end):
	"""
	Sorts the input list using the Merge Sort algorithm.

	Parameters:
	input_list (list): The list to be sorted.
	list_start (int): The starting index of the sublist to be sorted.
	list_end (int): The ending index of the sublist to be sorted.

	Returns:
	list: The sorted list.

	"""
	if list_end - list_start >= 2:
		list_mid = (list_start+list_end)//2
		input_list = MergeSort(input_list, list_start, list_mid)
		input_list = MergeSort(input_list, list_mid, list_end)
		input_list = Merge(input_list, list_start, list_mid, list_end)
	return input_list


# TODO: understand why it works
def Merge(input_list, list_start, list_mid, list_end):
	"""
	Merge two sorted subarrays of `input_list` into a single sorted subarray.

	Args:
		input_list (list): The input list containing the subarrays to be merged.
		list_start (int): The starting index of the first subarray.
		list_mid (int): The ending index of the first subarray and the starting index of the second subarray.
		list_end (int): The ending index of the second subarray.

	Returns:
		list: The input list with the merged subarrays.

	"""
	nstart = list_mid - list_start
	nend = list_end - list_mid
	temp = [0] * (nstart + nend)
	ilower, iupper, k = list_start, list_mid, 0

	while ilower < list_mid and iupper < list_end:
		if input_list[ilower] <= input_list[iupper]:
			temp[k] = input_list[ilower]
			ilower += 1
			k += 1
		else:
			temp[k] = input_list[iupper]
			iupper += 1
			k += 1
	if ilower == list_mid:
		temp[k:] = input_list[iupper:list_end]
	else:
		temp[k:] = input_list[ilower:list_mid]
	input_list[list_start : list_end] = temp
	return input_list


def GenerateDataset(n_of_sets, items_per_set):
	'''
	Generate a dataset with random numbers.

	Parameters:
	n_of_sets (int): The number of sets to generate.
	items_per_set (int): The number of items per set.

	Returns:
	list: A list of lists representing the generated dataset.
	'''

	dataset = []
	for _ in range(n_of_sets):
		single_set = []
		for _ in range(items_per_set):
			single_set.append(randint(1, items_per_set))
		dataset.append(single_set)
	return dataset


def sort_test():
	'''
	Entry point for testing functions
	'''
	test_list = [5,2,6,3,7,1,4]
	print(f'Insertion: {InsertionSort(test_list)}')
	test_list = [5,2,6,3,7,1,4]
	print(f'Merge: {MergeSort(test_list, 0, len(test_list))}')


def main():
	dataset = GenerateDataset(1000, 10)
	dataset_insert= dataset[:]
	dataset_merge = dataset[:]

	insertion_time = []
	merge_time = []

	for single_set in dataset_insert:
		start = time()
		InsertionSort(single_set)
		insertion_time.append(time()-start)

	for single_set in dataset_merge:
		start = time()
		MergeSort(single_set, 0, len(single_set))
		merge_time.append(time()-start)

	print('\nINSERTION SORT\n-----------------')
	print(f'Total: {sum(insertion_time)}')
	print(f'Minimum time: {min(insertion_time)}')
	print(f'Maximum time: {max(insertion_time)}')
	print(f'Average time: {sum(insertion_time)/len(insertion_time)}')
	print('\nMERGE SORT\n-----------------')
	print(f'Total: {sum(merge_time)}')
	print(f'Minimum time: {min(merge_time)}')
	print(f'Maximum time: {max(merge_time)}')
	print(f'Average time: {sum(merge_time)/len(merge_time)}')




if __name__ == '__main__':
	#sort_test()
	main()