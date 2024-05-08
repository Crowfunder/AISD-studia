from time import time
import copy

# Uncomment to get verbose output (each disk move)
def MoveLog(num, sour, dest, moves):
	#print(f'Moved {num} from {sour} to {dest} [Move no. {moves}]')
	pass


# I hate this thing
# I know this isn't the right way to handle recursion variables
# I'm just too tired, even Pylance thinks it's a mistake but it IS in fact valid python
# Also it may be broken as it was not supposed to even operate on lists, but rather on raw prints
# and realised way too late
# https://stackoverflow.com/questions/14513717/tracking-the-number-of-recursive-calls-without-using-global-variables-in-python
def HanoiRecursive(n, sour, dest, buff):
	# it doesn't even know how to return properly so I have to set these
	# god-awful failsafes everywhere, this is raw insanity
	if not HanoiRecursive.hanoi_data[sour]:
		return
	if n == 1:
		MoveLog(n, sour, dest, HanoiRecursive.count)
		HanoiRecursive.hanoi_data[dest].append(HanoiRecursive.hanoi_data[sour].pop())
		HanoiRecursive.count+=1
		return HanoiRecursive.hanoi_data
	HanoiRecursive(n-1, sour, buff, dest)
	if not HanoiRecursive.hanoi_data[sour]:
		return
	MoveLog(n, sour, dest, HanoiRecursive.count)
	HanoiRecursive.hanoi_data[dest].append(HanoiRecursive.hanoi_data[sour].pop())
	HanoiRecursive.count+=1
	HanoiRecursive(n-1, buff, dest, sour)


def MoveBetweenStacks(sour, dest, hanoi_data, i):

	# Empty dest stack, can move freely
	if not hanoi_data[dest]:
		hanoi_data[dest].append(hanoi_data[sour].pop())
		MoveLog(hanoi_data[dest][-1], sour, dest, i)
		return hanoi_data

	# Empty sour stack, can move freely
	if not hanoi_data[sour]:
		hanoi_data[sour].append(hanoi_data[dest].pop())
		MoveLog(hanoi_data[sour][-1], dest, sour, i)
		return hanoi_data

	sour_disc = hanoi_data[sour][-1]
	dest_disc = hanoi_data[dest][-1]
		
	if sour_disc < dest_disc:
		hanoi_data[dest].append(hanoi_data[sour].pop())
		MoveLog(hanoi_data[dest][-1], sour, dest, i)
		return hanoi_data
	
	else:
		hanoi_data[sour].append(hanoi_data[dest].pop())
		MoveLog(hanoi_data[sour][-1], dest, sour, i)
		return hanoi_data


def HanoiIter(n, sour, dest, buff, hanoi_data):
	moves = pow(2, n)-1
	if n%2 == 0:
		buff, dest = dest, buff
	for i in range(1,moves+1):
		if i % 3 == 1:
			hanoi_data = MoveBetweenStacks(sour, dest, hanoi_data, i)
		elif i % 3 == 2:
			hanoi_data = MoveBetweenStacks(sour, buff, hanoi_data, i)
		elif i % 3 == 0:
			hanoi_data = MoveBetweenStacks(buff, dest, hanoi_data, i)

	return hanoi_data


def main():
	
	recursive_time = []
	iterative_time = []
	stakes = 3
	hanoi_data = {'SOUR': [3,2,1], 'DEST' : [], 'BUFF' : []}
	for _ in range(0,1000):
		HanoiRecursive.hanoi_data = copy.deepcopy(hanoi_data)
		HanoiRecursive.count = 0
		start = time()
		HanoiRecursive(stakes, 'SOUR', 'DEST', 'BUFF')
		recursive_time.append(time()-start)

	for _ in range(0,1000):
		hanoi_data_copy = copy.deepcopy(hanoi_data)
		start = time()
		HanoiIter(stakes, 'SOUR', 'DEST', 'BUFF', hanoi_data_copy)
		iterative_time.append(time()-start)

	print('\nRecursive Hanoi\n-----------------')
	print(f'Total: {sum(recursive_time)}')
	print(f'Minimum time: {min(recursive_time)}')
	print(f'Maximum time: {max(recursive_time)}')
	print(f'Average time: {sum(recursive_time)/len(recursive_time)}')
	print('\nIterative Hanoi\n-----------------')
	print(f'Total: {sum(iterative_time)}')
	print(f'Minimum time: {min(iterative_time)}')
	print(f'Maximum time: {max(iterative_time)}')
	print(f'Average time: {sum(iterative_time)/len(iterative_time)}')


if __name__ == '__main__':
	main()
