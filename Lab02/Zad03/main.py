##################################################
# by Crowfunder
# 
# utilizes indexing and preloading dict data
# to speed up search
##################################################
from time import time

def LoadDictionaryData(ifname):
	with open(ifname, 'r', encoding='utf-8') as file:
		return file.readlines()


def GenerateDictionaryIndex(dict_data, prefix_length):
	dict_index = {}
	prev_prefix = ''
	line_count = 0
	prev_line_count = 0
	file_length = len(dict_data)
	for line in dict_data:
		prefix = line[:prefix_length]
		if prefix != prev_prefix:
			dict_index[prefix] = (line_count, file_length)
			if prev_prefix != '':
				dict_index[prev_prefix] = (prev_line_count, line_count)
			prev_line_count = line_count
		line_count += 1
		prev_prefix = prefix
	return dict_index


def CheckInDictionary(word, dict_index, prefix_length, dict_data):
	index = word[:prefix_length]
	for i in range(dict_index[index][0], dict_index[index][1]):
		if dict_data[i][:-1] == word:
			return True
	return False


def GetInput(query):
	output = ' '
	while ' ' in output:
		output = (input(query)).lower()
	return output


def main():

	# Length of prefix in index, 1 means first letter
	# 2 means two first letters and so on, speeds up
	# locating the word exponentially without too much
	# indexing overhead
	# Be wary that setting over 2 is generally a bad idea
	# as it will not be able to handle 2-letter words.
	PREFIX_LENGTH = 1
	DICT_FILENAME = 'Lab02/Zad03/SJP.txt'

	print('Wczytywanie słownika...')
	start = time()
	dict_data = LoadDictionaryData(DICT_FILENAME)
	print('Generowanie indeksu słownika...')
	dict_index = GenerateDictionaryIndex(dict_data, PREFIX_LENGTH)
	print(f'Sukces w {round(time()-start,2)}s!')

	while True:
		word = GetInput('> Podaj pojedyńcze słowo: ')
		start = time()
		if CheckInDictionary(word, dict_index, PREFIX_LENGTH, dict_data):
			print(f'{word} jest prawidłowym słowem. ({round(time()-start,4)}s)')
		else:
			print(f'{word} nie jest prawidłowym słowem. ({round(time()-start,4)}s)')


if __name__ == '__main__':
	main()