# A Python program to demonstrate operations of KD tree
import sys

# Number of dimensions
k = 2

# A structure to represent node of kd tree
class Node:
	def __init__(self, point):
		self.point = point
		self.left = None
		self.right = None

# A method to create a node of K D tree
def newNode(point):
	return Node(point)

# Inserts a new node and returns root of modified tree
# The parameter depth is used to decide axis of comparison
def insertRec(root, point, depth):
	# Tree is empty?
	if not root:
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

# A utility method to determine if two Points are same
# in K Dimensional space
def arePointsSame(point1, point2):
	# Compare individual coordinate values
	for i in range(k):
		if point1[i] != point2[i]:
			return False

	return True

# Searches a Point represented by "point[]" in the K D tree.
# The parameter depth is used to determine current axis.
def searchRec(root, point, depth):
	# Base cases
	if not root:
		return False
	if arePointsSame(root.point, point):
		return True

	# Current dimension is computed using current depth and total
	# dimensions (k)
	cd = depth % k

	# Compare point with root with respect to cd (Current dimension)
	if point[cd] < root.point[cd]:
		return searchRec(root.left, point, depth + 1)

	return searchRec(root.right, point, depth + 1)

# Searches a Point in the K D tree. It mainly uses
# searchRec()
def search(root, point):
	# Pass current depth as 0
	return searchRec(root, point, 0)

# Driver program to test above functions
if __name__ == '__main__':
	root = None
	points = [[3, 6], [17, 15], [13, 15], [6, 12], [9, 1], [2, 7], [10, 19]]

	n = len(points)

	for i in range(n):
		root = insert(root, points[i])

	point1 = [10, 19]
	if search(root, point1):
		print("Found")
	else:
		print("Not Found")

	point2 = [12, 19]
	if search(root, point2):
		print("Found")
	else:
		print("Not Found")
		
# This code is contributed by Prajwal Kandekar
