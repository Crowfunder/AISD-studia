from random import randint
from time import time

# https://www.youtube.com/watch?v=Q1JdRUh1_98
def InsertionSort(input_list):
	for i in range(1, len(input_list)):
		x = input_list[i]
		j = i-1
		while j >= 0 and input_list[j] > x:
			input_list[j+1] = input_list[j]
			j-=1
		input_list[j+1] = x
	return input_list


def MergeSort(input_list):
	pass	


def GenerateDataset(n_of_sets, items_per_set):
	dataset = []
	for _ in range(0, n_of_sets):
		single_set = []
		for _ in range(0, items_per_set):
			single_set.append(randint(1,items_per_set))
		dataset.append(single_set)
	return dataset


def sort_test():
	test_list = [5,2,6,3,7,1,4]
	print(f'Insertion: {InsertionSort(test_list)}')
	print(f'Merge: {MergeSort(test_list)}')


def main():
	dataset = GenerateDataset(1000, 100)

	insertion_time = []
	merge_time = []
	for single_set in dataset:

		start = time()
		InsertionSort(single_set)
		insertion_time.append(time()-start)
	
		start = time()
		MergeSort(single_set)
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
	sort_test()
	#main()