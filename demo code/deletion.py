from typing import List

# Set the number of dimensions for each point
k = 2

# Define a class for each node in the K-Dimensional Tree
class Node:
	def __init__(self, point: List[int]):
		# The point in the tree is stored in this node
		self.point = point
		# The left child node
		self.left = None
		# The right child node
		self.right = None

# Function to insert a new point into the tree
def insert(root, point: List[int]):
	# If the tree is empty, return a new node with the point
	if not root:
		return Node(point)

	# Start from the root node
	current_node = root
	# Find the correct leaf node to insert the new point
	while current_node:
		# If the new point is smaller than the current node's point in the current dimension, go to the left child node
		next_node = current_node.left if point[k-1] < current_node.point[k-1] else current_node.right
		# If the next node doesn't exist, we have found the correct leaf node to insert the new point
		if not next_node:
			break
		# If the next node exists, continue searching in the tree
		current_node = next_node

	# Insert the new point as a left or right child node of the correct leaf node
	if point[k-1] < current_node.point[k-1]:
		current_node.left = Node(point)
	else:
		current_node.right = Node(point)
	return root

# Function to copy the values of one point to another
def copyPoint(p1, p2):
	for i in range(k):
		p1[i] = p2[i]

# Function to find the node with the minimum value in a subtree
def minValueNode(node):
	current_node = node
	# Go to the leftmost leaf node in the subtree
	while current_node.left:
		current_node = current_node.left
	return current_node

# Recursive function to delete a node from the tree
def deleteNodeRec(root, point, depth):
	# If the tree is empty or the node is not found, return None
	if not root:
		return None

	# Calculate the current dimension based on the depth
	current_depth = depth % k
	# If the point to be deleted is smaller than the current node's point in the current dimension, go to the left subtree
	if point[current_depth] < root.point[current_depth]:
		root.left = deleteNodeRec(root.left, point, depth + 1)
	# If the point to be deleted is larger than the current node's point in the current dimension, go to the right subtree
	elif point[current_depth] > root.point[current_depth]:
		root.right = deleteNodeRec(root.right, point, depth + 1)
	# If the point to be deleted is equal to the current node's point, delete the node
	else:
		# If the node has no left child, return its right child
		if not root.left:
			return root.right
		elif not root.right:
			return root.left
		else:
			temp = minValueNode(root.right)
			copyPoint(root.point, temp.point)
			root.right = deleteNodeRec(root.right, temp.point, depth + 1)
	return root

def deleteNode(root, point):
	return deleteNodeRec(root, point, 0)

# Driver program to test above functions
if __name__ == "__main__":
	root = None
	points = [[30, 40], [5, 25], [70, 70], [10, 12], [50, 30], [35, 45]]
	n = len(points)

	for i in range(n):
		root = insert(root, points[i])

	# Delete (30, 40)
	root = deleteNode(root, points[0])

	print("Root after deletion of (30, 40)")
	print(root.point[0], root.point[1])

# This code is contributed by Vikram_Shirsat
