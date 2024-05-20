#####################
# by crowfunder,
# unfortunately.
#####################
from time import time


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
	Search for a pattern in a 2D matrix using the naive approach.

	Parameters:
		data (list[str]): The matrix data as a list of strings.
		pattern (str): The pattern to search for.
		matrix_size (int): The size of the matrix.

	Returns:
		list[tuple[int]]: A list of tuples representing the positions of the found patterns.

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


def PatternSearchRabinKarp(data, pattern, matrix_size):
	"""
	Search for a pattern in a 2D matrix using the Rabin-Karp algorithm.

	Parameters:
		data (list[str]): The matrix of characters to search in.
		pattern (str): The pattern to search for.
		matrix_size (int): The size of the matrix.

	Returns:
		list[tuple[int]]: A list of tuples representing the coordinates of the found patterns.

	"""
	patterns_found: list[tuple] = []
	ptrn_len = len(pattern)   # let's avoid multiple len() calls
	hash_ptrn = 0
	h = 1       # ??? some funky math stuff ig
	d = 16      # 16 digits in base16, or maybe 17 idk it works either way
	q = 101     # why the hell is it 101 I have genuinely no idea, just some prime number

	# more funky math stuff
	for i in range(ptrn_len-1):
		h = (h*d) % q

	# Calculate pattern hash
	for i in range(ptrn_len):
		hash_ptrn = (d*hash_ptrn + ord(pattern[i])) % q

	for y in range(0, matrix_size-ptrn_len+1):
		x_text = data[y]
		y_text = ''.join([line[0] for line in data[y: y+ptrn_len]])

		# Calculate first hash values in row and column
		# column "y" hashes are often zeroed out so we need to zero-out 
		# the row "x" hash at least once per row so that they align
		# look, I have no idea why, it just works like that
		hash_text_x = 0
		hash_text_y = 0
		for i in range(ptrn_len):
			hash_text_x = (d*hash_text_x + ord(x_text[i])) % q
			hash_text_y = (d*hash_text_y + ord(y_text[i])) % q

		for x in range(0, matrix_size-ptrn_len+1):
			y_text = ''.join([line[x] for line in data[y: y+ptrn_len]])

			# Yes, this does not implement a rolling hash to y_text
			# but it's not viable as we move along x axis and it would be insustainable to 
			# store all rolling hashes and roll them, matrix_size values in a single array
			# I have a nightmare-scenario collection this week and overengineering this crap
			# is most certainly the last thing I want to do right now
			hash_text_y = 0
			if y < matrix_size-ptrn_len:
				for i in range(ptrn_len):
					hash_text_y = (d*hash_text_y + ord(y_text[i])) % q

			if hash_ptrn == hash_text_x and hash_ptrn == hash_text_y:

				# Final sanity checks if the hashes had not somehow collided
				# which is literally the naive string comparison
				for j in range(ptrn_len):
					if x_text[x+j] != pattern[j] or y_text[0+j] != pattern[j]:
						break

				j += 1
				if j == ptrn_len and y < matrix_size-ptrn_len:
					patterns_found.append((y,x))

			# Roll the row hash to the next position before proceeding
			if x < matrix_size-ptrn_len:
				hash_text_x = (d*(hash_text_x-ord(x_text[x])*h) + ord(x_text[x+ptrn_len])) % q
				if hash_text_x < 0:
					hash_text_x = hash_text_x+q

	return patterns_found


def Test(data_lengths: list[int]):
	SEPARATOR = '########################'
	for data_len in data_lengths:
		data = LoadPatternMatrix(data_len)
		print(f'Dataset: {data_len}')
		print(SEPARATOR)

		start = time()
		PatternSearchNaive(data, 'ABC', data_len)
		print(f'Naive: {round(time()-start,2)}s')

		start = time()
		PatternSearchRabinKarp(data, 'ABC', data_len)
		print(f'Rabin-Karp: {round(time()-start,2)}s')

		print('\n')


def main():
	"""
	The main function of the program.
	"""
	data_lens = [1000,2000,3000,4000,5000]
	Test(data_lens)



if __name__ == '__main__':
	main()

