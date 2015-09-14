import random
from Queue import Queue
class Tree:

	def __init__(self, root):
		self.root = root

	def max_depth(self, node = None):
		if node == None:
			return 0
		return max(self.max_depth(node.left) + 1, self.max_depth(node.right) + 1)

	def min_depth(self, node = None):
		if node == None:
			return 0
		return min(self.max_depth(node.left) + 1, self.max_depth(node.right) + 1) 

	def print_tree(self):
		print 'not implemented yet'

	

		

class Node:
	def __init__(self, value, left = None, right = None):
		self.value = value
		self.left = left
		self.right = right



def build_test_tree():
	val = random.randint(0, 100)
	node = Node(val)
	tree = Tree(node)

	for i in range(0, 10):
		node.right = Node(random.randint(0, 100))
	return tree
	



# Create binary tree with minimal height
def create_min_height_tree(input_array = [1,2,3,4,5,6,7,8,9,10]):

	if len(input_array) == 0:
		return 
	if len(input_array) == 1:
		return Node(input_array[0])

	middle_index = len(input_array)//2
	middle = input_array[middle_index]
	left_array = input_array[0:middle_index]
	right_array = input_array[middle_index + 1:len(input_array)]

	root = Node(middle)
	root.left = create_min_height_tree(left_array)
	root.right = create_min_height_tree(right_array)
	return root

def print_bfs_tree(node): #level order traversal
	root = node
	level_q = Queue()
	next_level_q = Queue()
	level_q.put(root)
	while not level_q.empty():
		node = level_q.get()
		if node.left:
			next_level_q.put(node.left)
		if node.right:
			next_level_q.put(node.right)
		print node.value
		if level_q.empty():
			print '*'
			while not next_level_q.empty():
				level_q.put(next_level_q.get())
	print 'done'

def longest_path():
	print 'implementing...'



def print_inorder(node):
	if node.left != None:
		print_inorder(node.left)
	print node.value
	if node.right != None:
		print_inorder(node.right)

def print_postorder(node):
	if node != None:
		print_postorder(node.left)
		print_postorder(node.right)
		print node.value

def print_preorder(node):
	if node != None:
		print node.value
		print_preorder(node.left)
		print_preorder(node.right)
if __name__ == "__main__":
	test_tree = create_min_height_tree()
	print_preorder(test_tree)
	# tree = build_test_tree()
	# # MAX MIN Depth
	# print 'getting max depth'
	# print tree.max_depth(tree.root)

	# print 'getting min depth'
	# print tree.min_depth(tree.root)

	# root = create_min_height_tree()
	# print 'here is my min height tree'
	# print print_bfs_tree(root)

