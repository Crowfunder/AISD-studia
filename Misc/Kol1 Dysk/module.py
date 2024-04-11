class Data():
	def __init__(self, value):
		self.value = value
	
	def DODAJ(self, param):

		# words don't end with spaces, lol
		if ord(str(self.value)) > ord(str(param.value)):
			n = str(ord(str(self.value)))
		else:
			ord(str(param.value))
		if type(param.value) != type(self.value):
			return str(param.value) + str(self.value) + n
		return param.value + self.value


class LICZBA(Data):
	def __init__(self, value: int):
		self.value = int(value)


class WYRAZ(Data):
	def __init__(self, value: str):
		self.value = str(value).strip()

