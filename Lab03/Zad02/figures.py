import math

class Figure:
	def __init__(self, dimensions: list[float]):
		if any(number <= 0 for number in dimensions):
			raise Exception('Length 0 or less.')
		self.dimensions = sorted(dimensions)
		if not self.dimensions_check():
			raise Exception('Wrong number of dimensions or impossible dimensions')

	def dimensions_check(self) -> bool:
		return True

	def surface(self):
		return 0.0
	
	def circumference(self):
		return sum(self.dimensions)
	

class Triangle(Figure):
	'''
	Takes 3 floats/ints as arguments
	'''
	def dimensions_check(self):
		if len(self.dimensions) != 3:
			return False
		if self.dimensions[0] + self.dimensions[1] < self.dimensions[2]:
			return False
		return True

	def surface(self):
		p = sum(self.dimensions)/2
		a = self.dimensions[0]
		b = self.dimensions[1]
		c = self.dimensions[2]
		return math.sqrt(p*(p-a)*(p-b)*(p-c))


class Circle(Figure):
	"""
	Takes 1 float/int as arguments
	"""
	def dimensions_check(self):
		if len(self.dimensions) != 1:
			return False
		return True
	
	def surface(self):
		return math.pi*(self.dimensions[0]**2)
	
	def circumference(self):
		return 2*(math.pi)*(self.dimensions[0])


class Square(Figure):
	"""
	Takes 1 float/int as arguments
	"""
	def dimensions_check(self) -> bool:
		if len(self.dimensions) != 1:
			return False
		return True

	def surface(self):
		return self.dimensions[0]**2
	
	def circumference(self):
		return 4*self.dimensions[0]

# pitagoras = Triangle([3,4,5])
# print(pitagoras.surface())
# circa = Circle([1])
# print(circa.surface())
# squaredy_cat = Square([2])
# print(squaredy_cat.circumference())