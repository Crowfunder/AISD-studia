######################################################
# by Crowfunder
#
# sometimes, the price you pay for pretty code
# is paid in sickly tears.
######################################################

import math

class TreeNode:
	"""
	Represents a node in a binary search tree.

	Attributes:
		value: The value stored in the node.
		left: The left child node.
		right: The right child node.
	"""

	def __init__(self, value=None):
		"""
		Initializes a new instance of the TreeNode class.

		Args:
			value: The value to be stored in the node.
		"""
		self.right = None
		self.left = None
		self.value = value


	def insert(self, input_val):
		"""
		Inserts a new value into the binary search tree.

		Args:
			input_val: The value to be inserted.
		"""
		if input_val == self.value:
			return
		
		if input_val > self.value:
			if self.right:
				self.right.insert(input_val)
				return
			self.right = TreeNode(input_val)
			return
		
		if self.left:
			self.left.insert(input_val)
			return
		
		self.left = TreeNode(input_val)


	def search(self, input_val):
		"""
		Searches for a value in the binary search tree.

		Args:
			input_val: The value to search for.

		Returns:
			True if the value is found, False otherwise.
		"""
		if input_val == self.value:
			return True
		
		if input_val > self.value:
			if self.right:
				return self.right.search(input_val)
			else:
				return False

		if self.left:
			return self.left.search(input_val)
		else:
			return False


	def visualize(self, depth=0):
		"""
		Visualizes the binary search tree.

		Args:
			depth: The current depth of the node (used for indentation).
		"""
		print(depth*'-', self.value, end='', sep='')
		depth += 1
		if self.left:
			self.left.visualize(depth)
		if self.right:
			if self.left:
				print('\n', ' '*3*depth, end='', sep='')
			self.right.visualize(depth)


	def minimum(self):
		"""
		Finds the minimum value in the binary search tree.

		Returns:
			The minimum value.
		"""
		if self.left:
			return self.left.minimum()
		return self.value


	def maximum(self):
		"""
		Finds the maximum value in the binary search tree.

		Returns:
			The maximum value.
		"""
		if self.right:
			return self.right.maximum()
		return self.value



class BSTrees:
	"""
	Binary Search Trees class.

	Attributes:
		root_dict (dict): A dictionary containing the root nodes of the binary search trees.
	"""

	def __init__(self, input_data=None):
		"""
		Initializes a new instance of the BSTrees class.

		Args:
			input_data (list[float], optional): A list of floating-point numbers to initialize the binary search trees.
		"""
		self.root_dict = {}
		if input_data:
			self.DataToTrees(input_data)


	def DataToTrees(self, input_data: list[float]):
		"""
		Converts the input data into binary search trees and append it to existing trees.
		WARNING: DOES NOT WORK IF INPUT DATA IS NOT SORTED

		Args:
			input_data (list[float]): A list of floating-point numbers to convert into binary search trees.
		"""
		output = self.root_dict
		done_list = []
		node_previous = TreeNode() 	# unnecessary line, it just makes linter feel good

		for number in input_data:
			index = math.floor(number) + 0.5
			if index not in done_list:
				done_list.append(index)
				node = TreeNode(index)
				output[index] = node
				node_previous = node

			node_previous.insert(number)

		self.root_dict = output


	def SearchTree(self, num: float):
		"""
		Searches for a number in the binary search trees.

		Args:
			num (float): The number to search for.

		Returns:
			bool: True if the number is found, False otherwise.
		"""
		num_index = math.floor(num) + 0.5
		try:
			root = self.root_dict[num_index]
			return root.search(num)
		except KeyError:
			return False


	def PrintTree(self):
		"""
		Prints the binary search trees.
		"""
		for root in self.root_dict.values():
			root.visualize()
			print('\n')


	def MinimumInTree(self, root_choice):
		"""
		Finds the minimum value in a specific binary search tree.

		Args:
			root_choice: The index of the root node of the binary search tree.

		Returns:
			float: The minimum value in the binary search tree.
		"""
		root_choice = math.floor(root_choice) + 0.5
		return self.root_dict[root_choice].minimum()


	def MaximumInTree(self, root_choice):
		"""
		Finds the maximum value in a specific binary search tree.

		Args:
			root_choice: The index of the root node of the binary search tree.

		Returns:
			float: The maximum value in the binary search tree.
		"""
		root_choice = math.floor(root_choice) + 0.5
		return self.root_dict[root_choice].maximum()
