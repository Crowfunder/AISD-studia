##################################################
# by Crowfunder
# 
# a very odd approach to a very simple task,
# somehow 4 times slower than the stupidest method
# method, why in the hell.
# I will blame it on function calls being slow.
# IT ITERATES OVER THE DATA ONLY 2 TIMES 
# VS LIKE 5 OR 6 ITERATIONS, AND IT'S STILL SLOWER
# I suck
##################################################

def ReadFileLines(fname, skip) -> list[str]:
	'''
	Read the contents of a file and return them as a list of lines.

	Parameters:
		fname (str): The name of the file to be read.
		skip (int): The number of lines to skip at the beginning of the file.

	Returns:
		list[str]: The contents of the file as a list of lines.
	'''
	with open(fname, 'r') as file:
		return file.readlines()[skip:]


def ASCIInihilator_splitter(sentnc):
	'''
	String splitting method.
	Anihilates words that start with two-letter prefix of ASCII table neighbors.

	Parameters:
		sentnc (str): Sentence string to be ASCIInihilated

	Returns:
		str: Sentence with all words matching the filter removed.
	'''
	output = ''
	sentnc = sentnc.strip('\n').split(' ')
	for word in sentnc:
		if len(word) <= 1:
			output += word + ' '
		else:
			if abs(ord(word[0]) - ord(word[1])) == 1:
				sentnc.remove(word)
			else:
				output += word + ' '
	return output
	


def ASCIInihilator_stringwalk(sentnc):
	'''
	String split-less method.
	Anihilates words that start with two-letter prefix of ASCII table neighbors.

	Parameters:
		sentnc (str): Sentence string to be ASCIInihilated

	Returns:
		str: Sentence with all words matching the filter removed.
	'''
	output = ''
	while sentnc.strip('\n'):
		match_pattern = abs(ord(sentnc[0]) - ord(sentnc[1])) == 1
		# Finalizing case when no more spaces remain
		next_space = sentnc.find(' ')
		if next_space == -1:
			word = sentnc
			sentnc = ''
		else:
			word = sentnc[:next_space+1]
			sentnc = sentnc[next_space+1:]
		if not match_pattern:
			output += word
	return output


def CSVParse(file_data) -> dict:
	'''
	Parse the two-column CSV file data into a dictionary.

	Parameters:
		file_data (str): The CSV file data as a string.

	Returns:
		dict: A dictionary containing the parsed CSV data.
	'''
	csv_dict = {}

	for line in file_data:
     
		# Find csv columns by first comma
  		# others are parts of data
		comma: int = line.find(',')
		item_id: str = line[:comma]
		item_id_int = int(item_id)
		item_data: str = line[comma+1:]
  
		# Filter out empty values
		if not item_data.strip('\n'):
			continue

		# Lowercase the item data according to task
		item_data = item_data.lower()
  
		# Remove words with two-letter prefix of
		# letters adjacent in ASCII table
		# Two methods of removing the prefixed words
		# Splitter seems to be faster?
		item_data = ASCIInihilator_splitter(item_data)
		#item_data = ASCIInihilator_stringwalk(item_data)

		# Handle duplicate ids by incrementing them
		try:
			while csv_dict[item_id]:
				item_id_int += 1
				item_id = str(item_id_int)

		except KeyError:
			csv_dict[item_id] = item_data

	return csv_dict


def FileCSVFromDict(fname, csv_dict):
	'''
	Convert a dictionary into a CSV file and save it.

	Parameters:
		fname (str): The name of the file to be created.
		csv_dict (dict): The dictionary to be converted into a CSV file.

	Returns:
		None
	'''
	with open(fname, 'w+') as file:

		# Necessary column names
		file.write('id, val\n')

		# We want the data to be sorted in output
		for item_id in sorted(list(csv_dict.keys()), key=int):
			line = f'{item_id}, {csv_dict[item_id]}\n'
			file.write(line)


def main():
	file_contents = ReadFileLines('Lab02/Zad02/zadanie2.csv', skip=1)
	csv_dict = CSVParse(file_contents)
	FileCSVFromDict('Lab02/Zad02/output.csv', csv_dict)


if __name__ == "__main__":
	import cProfile
	from pstats import SortKey, Stats
	with cProfile.Profile() as profile:
		main()
	(
		Stats(profile)
		.strip_dirs()
		.sort_stats(SortKey.TIME)
		.print_stats()
	)

