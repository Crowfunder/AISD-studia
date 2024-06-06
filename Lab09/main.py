######################
# by Crowfunder
# with love
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
		self.volume = width*height
		self.value = value
		self.gain = value/self.volume

	def rotate(self):
		self.width, self.height = self.height, self.width
		return self


class Backpack:
	def __init__(self, size):
		self.size = int(size)
		self.matrix = np.zeros((self.size, self.size), dtype=int)
		self.total_value = 0
		self.prev_state = None

	# If this object gets printed, print its matrix
	def __str__(self):
		return str(self.matrix)

	# Memento pattern, we can save the previous state of the object
	# so that we can go back in time (undo) in case we need it
	def save_state(self):
		prev_state = Backpack(self.size)
		prev_state.matrix = self.matrix
		prev_state.total_value = self.total_value
		prev_state.prev_state = self.prev_state
		self.prev_state = prev_state
		return self
	
	def restore_state(self):
		if not self.prev_state:
			self.prev_state = Backpack(self.size)
		self.matrix = self.prev_state.matrix
		self.total_value = self.prev_state.total_value
		self.prev_state = self.prev_state.prev_state
		return self

	# We cannot get the return value of the first _insert call
	# so we return True manually if it succeeds
	def insert_package(self, package_obj):
		if not self._insert(package_obj):
			return self._insert(package_obj.rotate())
		return True

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


# Sort all packages based on value to size ratio and insert them in that order
def BackpackerGreedy(size, packages_list):

	packages_list.sort(key=lambda x: x.gain, reverse=True)
	backpack = Backpack(size)
	for package_obj in packages_list:
		backpack.insert_package(package_obj)

	print(backpack.total_value)
	print(backpack)
	return backpack


def BackpackerGambler(size, packages_list, iterations):
	backpack = Backpack(size)
	for _ in range(iterations):
		backpack.save_state()
		random.shuffle(packages_list)
		for package_obj in packages_list:
			backpack.insert_package(package_obj)

		# If what we gambled is worse than previously, go back in time and keep gambling
		if backpack.total_value < backpack.prev_state.total_value:
			backpack.restore_state()

	print(backpack.total_value)
	print(backpack)
	return backpack


def BackpackerULTRAGREED(size, packages_list):
	packages_list.sort(key=lambda x: x.value, reverse=True)
	backpack = Backpack(size)
	for package_obj in packages_list:
		backpack.insert_package(package_obj)

	print(backpack.total_value)
	print(backpack)
	return backpack


def main():
	packages = PackageFileParser([20])
	#BackpackerGreedy(20, packages[20])
	# BackpackerGambler(20, packages[20], 1)
	# BackpackerGambler(20, packages[20], 15)
	BackpackerULTRAGREED(20, packages[20])

if __name__ == '__main__':
	main()