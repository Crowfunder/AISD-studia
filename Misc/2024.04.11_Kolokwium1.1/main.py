#####################
# by Crowfunder
# Copyright my ass
#####################

import string

class Czytelnik:
	def OTWORZ(self, filename):
		self.file = open(filename, 'r')
		return self
	
	def CZYTAM(self):
		count = 1
		filelines_odd =''
		for line in self.file.readlines():
			if count % 2 != 0:
				filelines_odd += line + '\n'
			count += 1
		self.filelines_odd = filelines_odd
		return self

	def SZUKAM(self, query):
		return query in self.filelines_odd
	
	def LICZ(self, letter):
		if len(letter) == 1:
			return self.filelines_odd.count(letter)
		else:
			raise Exception('Not a letter!')
		
	def ZAMYKAM(self):
		self.file.close()
		return self


def main():
	loremobj = Czytelnik().OTWORZ('lorem.txt').CZYTAM()
	letters_count = {}
	max_letter = ''
	max_letter_count = 0
	for letter in string.ascii_letters:
		counter = loremobj.LICZ(letter)
		letters_count[letter] = counter
		if counter > max_letter_count:
			max_letter_count = counter
			max_letter = letter
	loremobj.ZAMYKAM()
	print(max_letter)
	print(max_letter_count)


if __name__ == '__main__':
	main()