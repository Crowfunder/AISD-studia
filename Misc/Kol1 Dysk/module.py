class Data():
	def __init__(self, value):
		self.value = value
	
	def DODAJ(self, param):

		# words don't end with spaces, lol
		n = ''
		if type(self.value) is str:
			n = str(ord(str(self.value)[-1]))
		elif type(param.value) is str:
			n = str(ord(str(param.value)[-1]))
		if type(param.value) != type(self.value):
			return str(self.value) + str(param.value) + n
		return self.value + param.value 


class LICZBA(Data):
	def __init__(self, value: int):
		self.value = int(value)


class WYRAZ(Data):
	def __init__(self, value: str):
		self.value = str(value).strip()



