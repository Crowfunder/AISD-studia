
def MoveLog(num, sour, dest, moves):
	print(f'Moved {num} from {sour} to {dest} [Move no. {moves}]')

# I hate this thing
def HanoiRecursive(n, sour, dest, buff):
	if n == 1:
		MoveLog(n, sour, dest, HanoiRecursive.count)
		HanoiRecursive.count+=1
		return 
	HanoiRecursive(n-1, sour, buff, dest)
	MoveLog(n, sour, dest, HanoiRecursive.count)
	HanoiRecursive.count+=1
	HanoiRecursive(n-1, buff, dest, sour)


def HanoiIter(n, sour, dest, buff, hanoi_data):
	moves = 1
	while hanoi_data[sour] or hanoi_data[buff]:
		for i in range(1,n):
			if i%3 == 1:
				MoveLog(i, sour, dest, moves)
				hanoi_data[dest].append(hanoi_data[sour].pop())
				moves += 1
			if i%3 == 2:
				MoveLog(i, sour, buff, moves)
				hanoi_data[dest].append(hanoi_data[sour].pop())
				moves += 1
			if i%3 == 0:
				MoveLog(i, buff, dest, moves)
				hanoi_data[dest].append(hanoi_data[sour].pop())
				moves += 1


def main():

	# yes, this is cursed, leave me alone, even the linter hates it, I know
	# https://stackoverflow.com/questions/14513717/tracking-the-number-of-recursive-calls-without-using-global-variables-in-python
	HanoiRecursive.count = 0
	HanoiRecursive(4, 'SOUR', 'DEST', 'BUFF')
	
	hanoi_data = {'SOUR': [3,2,1], 'DEST' : [], 'BUFF' : []}
	HanoiIter(3, 'SOUR', 'DEST', 'BUFF', hanoi_data)

if __name__ == '__main__':
	main()
