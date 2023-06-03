# A python program to demonstrate find minimum on KD tree

# Number of dimensions
k = 2

class Node:
	def __init__(self, point):
		self.point = point
		self.left = None
		self.right = None

# A method to create a node of K D tree
def newNode(arr):
	temp = Node(arr)
	return temp

# Inserts a new node and returns root of modified tree
# The parameter depth is used to decide axis of comparison
def insertRec(root, point, depth):
	# Tree is empty?
	if root is None:
		return newNode(point)

	# Calculate current dimension (cd) of comparison
	cd = depth % k

	# Compare the new point with root on current dimension 'cd'
	# and decide the left or right subtree
	if point[cd] < root.point[cd]:
		root.left = insertRec(root.left, point, depth + 1)
	else:
		root.right = insertRec(root.right, point, depth + 1)

	return root

# Function to insert a new point with given point in
# KD Tree and return new root. It mainly uses above recursive
# function "insertRec()"
def insert(root, point):
	return insertRec(root, point, 0)

# A utility function to find minimum of three integers
def min_3(x, y, z):
	return min(x, y, z)

# Recursively finds minimum of d'th dimension in KD tree
# The parameter depth is used to determine current axis.
def findMinRec(root, d, depth):
	# Base cases
	if root is None:
		return float('inf')

	# Current dimension is computed using current depth and total
	# dimensions (k)
	cd = depth % k

	# Compare point with root with respect to cd (Current dimension)
	if cd == d:
		if root.left is None:
			return root.point[d]
		return min(root.point[d], findMinRec(root.left, d, depth + 1),findMinRec(root.right, d, depth + 1))

	# If current dimension is different then minimum can be anywhere
	# in this subtree
	return min_3(root.point[d], findMinRec(root.left, d, depth + 1), findMinRec(root.right, d, depth + 1))

# A wrapper over findMinRec(). Returns minimum of d'th dimension
def findMin(root, d):
	# Pass current level or depth as 0
	return findMinRec(root, d, 0)

# Driver program to test above functions
if __name__ == "__main__":
	root = None
	points = [ [30, 40], [5, 25], [70, 70], [10, 12], [50, 30], [35, 45] ]

	n = len(points)

	for i in range(n):
		root = insert(root, points[i])

	print("Minimum of 0'th dimension is", findMin(root, 0))
	print("Minimum of 1'th dimension is", findMin(root, 1))
	
# This code is contributed by Vikram_Shirsat
