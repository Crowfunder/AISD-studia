######################
# by Crowfunder
######################

import numpy as np
import random

def PackageFileParser(list_of_sizes):
	packages = {}
	
	for size in list_of_sizes:
		packages[size] = []
		with open(f'Lab09/packages/packages{size}.txt') as file:
			for line in file.readlines():
				data = line.strip().split(',')

				# Skip headers
				if not data[0].isnumeric():
					continue

				package_obj = Package(int(data[0]), int(data[1]), int(data[2]), int(data[3]))
				packages[size].append(package_obj)

	return packages


class Package:
	def __init__(self, id, width, height, value):
		self.id = id
		self.width = width
		self.height = height
		self.value = value
		self.gain = value/(width*height)

	# # If the object gets printed, print just its id
	# def __str__(self):
	# 	return str(self.id)

	def rotate(self):
		self.width, self.height = self.height, self.width
		return self


class Backpack:
	def __init__(self, size):
		self.size = int(size)
		self.matrix = np.zeros((self.size, self.size), dtype=int)
		self.prev_matrix = self.matrix
		self.total_value = 0

	def render(self):
		print(self.matrix)

	def insert_package(self, package_obj):
		if not self._insert(package_obj):
			self._insert(package_obj.rotate())

	def _insert(self, package_obj):
		for x in range(self.size - package_obj.width+1):
			for y in range(self.size - package_obj.height+1):
				package_fits = True

				for x_pkg in range(package_obj.width):
					for y_pkg in range(package_obj.height):
						if self.matrix[x+x_pkg][y+y_pkg]:
							package_fits = False
							break
					if not package_fits:
						break

				if package_fits:
					for x_pkg in range(x, x+package_obj.width):
						for y_pkg in range(y, y+package_obj.height):
							self.matrix[x_pkg, y_pkg] = package_obj.id

					self.total_value += package_obj.value
					return True
		return False


def BackpackerGreedy(size, packages_list):

	# Sort all packages based on value to size ratio
	packages_list.sort(key=lambda x: x.gain, reverse=True)
	backpack = Backpack(size)
	for package_obj in packages_list:
		backpack.insert_package(package_obj)

	print(backpack.total_value)
	backpack.render()
	return backpack


def BackpackerGambler(size, packages_list):
	backpack = Backpack(size)
	random.shuffle(packages_list)
	for package_obj in packages_list:
		backpack.insert_package(package_obj)

	print(backpack.total_value)
	backpack.render()
	return backpack

def main():
	packages = PackageFileParser([20])
	BackpackerGreedy(20, packages[20])
	BackpackerGambler(20, packages[20])

if __name__ == '__main__':
	main()