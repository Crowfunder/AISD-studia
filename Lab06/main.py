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


	def exists(self, input_val):
		if input_val == self.value:
			return True
		
		if input_val > self.value:
			if self.right:
				self.right.exists(input_val)
			else:
				return False

		if self.left:
			self.left.exists(input_val)
		else:
			return False


def DataToTree(input_list: list[float]):
	output = []
	done_list = []
	node_previous = TreeNode()

	for number in input_list:
		index = math.floor(number) + 0.5
		if index not in done_list:

			done_list.append(index)
			node = TreeNode(index)
			output.append(node)
			node_previous = node

		node_previous.insert(number)
	
	return output


sample_data = [1.3, 1.6, 3.7, 4.0, 4.99, 7.3, 7.8, 7.7, 7.9, 7.6, 9.3]
ret = DataToTree(sample_data)
print(ret)
