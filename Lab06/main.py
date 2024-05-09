import math

class TreeNode:
	def __init__(self, value=None):
		self.right = None
		self.left = None
		self.value = value

	def insert(self, input_val):
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
		print(depth*'-', self.value, end='', sep='')
		depth += 1
		if self.left:
			self.left.visualize(depth)
		if self.right:
			if self.left:
				print('\n', ' '*3*depth, end='', sep='')
			self.right.visualize(depth)

	def minimum(self):
		if self.left:
			return self.left.minimum()
		return self.value

	def maximum(self):
		if self.right:
			return self.right.maximum()
		return self.value



def DataToTree(input_list: list[float]):
	output = {}
	done_list = []
	node_previous = TreeNode() 	# unnecessary line, it just makes linter feel good

	for number in input_list:
		index = math.floor(number) + 0.5
		if index not in done_list:

			done_list.append(index)
			node = TreeNode(index)
			output[index] = node
			node_previous = node

		node_previous.insert(number)
	
	return output


def SearchTree(root_list: dict, num: float):
	num_index = math.floor(num) + 0.5
	try:
		root = root_list[num_index]
		return root.search(num)
	except KeyError:
		return False


def PrintTree(root_list: dict):
	for root in root_list.values():
		root.visualize()
		print('\n')

def MinimumInTree(root_list: dict, root_choice):
	root_choice = math.floor(root_choice) + 0.5
	return root_list[root_choice].minimum()


def MaximumInTree(root_list: dict, root_choice):
	root_choice = math.floor(root_choice) + 0.5
	return root_list[root_choice].maximum()


sample_data = [1.3, 1.6, 3.7, 4.0, 4.99, 7.3, 7.8, 7.7, 7.9, 7.6, 9.3]
ret = DataToTree(sample_data)
PrintTree(ret)
print(MaximumInTree(ret, 7))
