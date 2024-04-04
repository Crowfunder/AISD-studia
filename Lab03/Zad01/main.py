#####################
# by Crowfunder
# copyright my ass
#####################
import os
from string import ascii_uppercase


FILES_DIR = "./Lab03/Zad01/files"
OUTPUT_DIR = "./Lab03/Zad01/output"


def PrepareDirs():
	try:
		os.mkdir(OUTPUT_DIR)
		os.mkdir(FILES_DIR)
	except:
		pass
	try:
		for letter in ascii_uppercase:
			os.mkdir(OUTPUT_DIR+'/'+letter)
	except:
		pass


def SortFile(file_path, output_path):
	first_letter_up = file_path.split('/')[-1][0].upper()
	file_name = file_path.split('/')[-1]
	os.rename(file_path, OUTPUT_DIR+'/'+first_letter_up+'/'+file_name)


def main():
	PrepareDirs()
	for file_name in os.listdir(FILES_DIR):
		file_path = FILES_DIR + '/' + file_name
		SortFile(file_path, OUTPUT_DIR)


if __name__ == "__main__": 
	main()