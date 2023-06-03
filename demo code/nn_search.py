import numpy as np

class KDNode:
    def __init__(self, point, split_dim, left=None, right=None):
        self.point = point
        self.split_dim = split_dim
        self.left = left
        self.right = right

def build_kdtree(points, depth=0):
    if not points:
        return None
    
    k = len(points[0])
    split_dim = depth % k
    
    points.sort(key=lambda x: x[split_dim])
    median = len(points) // 2
    
    return KDNode(
        point=points[median],
        split_dim=split_dim,
        left=build_kdtree(points[:median], depth + 1),
        right=build_kdtree(points[median + 1:], depth + 1)
    )

def distance(point1, point2):
    return np.sqrt(np.sum((np.array(point1) - np.array(point2)) ** 2))

def nearest_neighbor_search(root, query_point):
    best_dist = float('inf')
    best_point = None
    
    def search(node, point, depth=0):
        nonlocal best_dist, best_point
        
        if node is None:
            return
        
        if node.point != point and distance(node.point, point) < best_dist:
            best_dist = distance(node.point, point)
            best_point = node.point
        
        split_dim = node.split_dim
        if point[split_dim] < node.point[split_dim]:
            search(node.left, point, depth + 1)
        else:
            search(node.right, point, depth + 1)
        
        if abs(point[split_dim] - node.point[split_dim]) < best_dist:
            if point[split_dim] < node.point[split_dim]:
                search(node.right, point, depth + 1)
            else:
                search(node.left, point, depth + 1)
    
    search(root, query_point)
    return best_point

# Example usage
points = [[2, 3], [5, 4], [9, 6], [4, 7], [8, 1], [7, 2]]
query = [6, 5]

kdtree = build_kdtree(points)
nearest = nearest_neighbor_search(kdtree, query)

print("Nearest neighbor:", nearest)
