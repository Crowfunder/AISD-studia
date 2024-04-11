class Abc:
	def OTWIERAM(self, filename):
		self.file = open(filename, 'r')
		return self

	def CZYTAJ(self):
		iteration = 0
		even_lines = ''
		for line in self.file.readlines():
			iteration+=1
			if iteration % 2 == 0:
				even_lines += line + '\n'
		self.even_lines = even_lines
		return self

	def POKAZ(self):
		words = self.even_lines.split()
		words_unique = set(words)
		output = []
		for word in words_unique:
			if words.count(word) > 1:
				output.append(word)
		return output
	
	def LICZ(self, word):
		vowels = ['a', 'e', 'i', 'y', 'o', 'u']
		num_of_vowels = 0
		for letter in word:
			if letter in vowels:
				num_of_vowels += 1
		return num_of_vowels
	
	def ZAMKNIJ(self):
		self.file.close()
		return self


def main():
	lorem = Abc().OTWIERAM('lorem.txt').CZYTAJ()
	word_index = {}
	max_word = ''
	max_word_count = 0
	for duplicate_word in lorem.POKAZ():
		duplicate_word_count = lorem.LICZ(duplicate_word)
		word_index[duplicate_word] = duplicate_word_count
		if duplicate_word_count > max_word_count:
			max_word = duplicate_word
			max_word_count = duplicate_word_count

	print('OUTPUT: ')
	print(max_word)
	print(max_word_count)

if __name__ == '__main__':
	main()