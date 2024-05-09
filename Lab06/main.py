import math

class TreeNode:
	def __init__(self, value=None):
		self.right = None
		self.left = None
		self.value = value


	def add_to_tree(self, input_val):
		if input_val == self.value:
			return
		
		if input_val > self.value:
			if self.right:
				self.right.add_to_tree(input_val)
				return
			self.right = TreeNode(input_val)
			return
		
		if self.left:
			self.left.add_to_tree(input_val)
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

	def visualize(self, prev='', depth=0):




def DataToTree(input_list: list[float]):
	output = {}
	done_list = []
	node_previous = TreeNode()

	for number in input_list:
		index = math.floor(number) + 0.5
		if index not in done_list:

			done_list.append(index)
			node = TreeNode(index)
			output[index] = node
			node_previous = node

		node_previous.add_to_tree(number)
	
	return output


def SearchTree(root_list: dict, num: float):
	num_index = math.floor(num) + 0.5
	try:
		root = root_list[num_index]
		return root.search(num)
	except KeyError:
		return False
	



sample_data = [1.3, 1.6, 3.7, 4.0, 4.99, 7.3, 7.8, 7.7, 7.9, 7.6, 9.3]
ret = DataToTree(sample_data)
print(SearchTree(ret, 9.3))
