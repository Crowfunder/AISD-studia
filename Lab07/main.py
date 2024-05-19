def LoadPatternMatrix(matrix_size):
	"""
	Load the pattern matrix from a file.

	Parameters:
	matrix_size (int): The size of the matrix.

	Returns:
	list: The matrix as a list of strings.

	Raises:
	FileNotFoundError: If the pattern file does not exist.
	"""
	try:
		with open(f'./Lab07/patterns/{str(matrix_size)}_pattern.txt', 'r') as file:
			return file.readlines()

	except FileNotFoundError:
		print('Pattern does not exist!')
		raise


def PatternSearchNaive(data, pattern, matrix_size):
	"""
	Search for a pattern in a matrix using the naive approach.

	Parameters:
	data (list): The matrix data as a list of strings.
	pattern (str): The pattern to search for.
	matrix_size (int): The size of the matrix.

	Returns:
	list: A list of tuples representing the positions of the found patterns.

	"""
	patterns_found: list[tuple] = []
	ptrn_len = len(pattern)   # let's avoid multiple len() calls
	for y in range(0, matrix_size):
		for x in range(0, matrix_size):
			
			# This looks awful, but is very simple.
			# The first condition checks if this and next letters in row are the pattern.
			# The second condition does the same but it joins letters in column
			# which requires some list shenanigans.
			if (data[y][x : x+ptrn_len] == pattern and
					''.join([line[x] for line in data[y: y+ptrn_len]]) == pattern):
				patterns_found.append((y,x))

	return patterns_found


def PatternSearchRabinKarp(data, pattern, matrix_size, hasher: function):
	"""
	Search for a pattern in a matrix using the naive approach.

	Parameters:
	data (list): The matrix data as a list of strings.
	pattern (str): The pattern to search for.
	matrix_size (int): The size of the matrix.

	Returns:
	list: A list of tuples representing the positions of the found patterns.

	"""
	patterns_found: list[tuple] = []
	ptrn_len = len(pattern)   # let's avoid multiple len() calls
	for y in range(0, matrix_size):
		for x in range(0, matrix_size):
			
			# This looks awful, but is very simple.
			# The first condition checks if this and next letters in row are the pattern.
			# The second condition does the same but it joins letters in column
			# which requires some list shenanigans.
			if (data[y][x : x+ptrn_len] == pattern and
					''.join([line[x] for line in data[y: y+ptrn_len]]) == pattern):
				patterns_found.append((y,x))

	return patterns_found


def main():
	"""
	The main function of the program.
	"""
	data_len = 1000
	data = LoadPatternMatrix(data_len)
	print(PatternSearchNaive(data, 'ABC', data_len))


if __name__ == '__main__':
	main()

