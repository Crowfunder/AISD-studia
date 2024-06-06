######################
# by Crowfunder
# with love
######################

import numpy as np

class Package:
	def __init__(self, id, width, height, value):
		"""
		Initialize a package object.

		Parameters:
		id (int): Package ID.
		width (int): Package width.
		height (int): Package height.
		value (int): Package value.
		"""
		self.id = id
		self.width = width
		self.height = height
		self.volume = width*height
		self.value = value
		self.gain = value/self.volume

	def rotate(self):
		"""
		Rotate the package by swapping its width and height.

		Returns:
		Package: The rotated package object.
		"""
		self.width, self.height = self.height, self.width
		return self


class Backpack:
	def __init__(self, size):
		"""
		Initialize a backpack object.

		Parameters:
		size (int): Size of the backpack.
		"""
		self.size = int(size)
		self.matrix = np.zeros((self.size, self.size), dtype=int)
		self.total_value = 0
		self.gains = 0
		self.prev_state = None

	def __str__(self):
		"""
		If backpack object gets printed, print its matrix.

		Returns:
		str: String representation of the backpack matrix.
		"""
		return str(self.matrix)

	def _calculate_gains(self):
		"""
		Helper function to calculate the total_value/occupied ratio of the backpack.

		Returns:
		Backpack: The backpack object with updated gains.
		"""
		occupied = np.count_nonzero(self.matrix)
		self.gains = self.total_value/occupied
		return self

	# Memento pattern, we can save the previous state of the object
	# so that we can go back in time (undo) in case we need it
	def save_state(self):
		"""
		Save the current state of the backpack.

		Returns:
		Backpack: The previous state of the backpack.
		"""
		prev_state = Backpack(self.size)
		prev_state.matrix = self.matrix.copy()	# Normally it's passed as reference, we don't want that
		prev_state.total_value = self.total_value
		prev_state.prev_state = self.prev_state
		self.prev_state = prev_state
		return self
	
	def restore_state(self):
		"""
		Restore the previous state of the backpack.

		Returns:
		Backpack: The restored backpack object.
		"""
		if not self.prev_state:
			self.prev_state = Backpack(self.size)
		self.matrix = self.prev_state.matrix.copy()  # Normally it's passed as reference, we don't want that
		self.total_value = self.prev_state.total_value
		self.prev_state = self.prev_state.prev_state
		return self

	def insert_package(self, package_obj):
		"""
		Insert a package into the backpack.

		Parameters:
		package_obj (Package): The package object to be inserted.

		Returns:
		bool: True if the package was successfully inserted, False otherwise.
		"""
		# We cannot get the return value of the first _insert call
		# so we return True manually if it succeeds
		if not self._insert(package_obj):
			return self._insert(package_obj.rotate())
		return True

	def _insert(self, package_obj):
		"""
		Helper function to insert a package into the backpack.

		Parameters:
		package_obj (Package): The package object to be inserted.

		Returns:
		bool: True if the package was successfully inserted, False otherwise.
		"""
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
					self._calculate_gains()
					return True
		return False