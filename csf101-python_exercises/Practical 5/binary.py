#importing deque
from collections import deque

#defining node class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
#implementing binary search tree class
class BinarySearchTree:
    def __init__(self):
        self.root = None
#implementing insertion method
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)
    def _insert(self, root, value):
        if value < root.value:
            if root.left is None:
                root.left = Node(value)
            else:
                self._insert(root.left, value)
        else:
            if root.right is None:
                root.right = Node(value)
            else:
                self._insert(root.right, value)
    def find_max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.value
#adding count_nodes method
    def count_nodes(self):
        return self._count_nodes(self.root)
    def _count_nodes(self, root):
        if root is None:
            return 0
        return 1 + self._count_nodes(root.left) + self._count_nodes(root.right) 
# implementing level order traveral
    def level_order_traversal(self):
        if self.root is None:
            return []
        result = []
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result
#implementing height method
    def find_height (self):
        return self._find_height(self.root)
    def _find_height(self, root):
        if root is None:
            return -1
        left_height = self._find_height(root.left)
        right_height = self._find_height(root.right)
        return 1 + max(left_height, right_height) 
#valid tree or not
    def is_valid_bst(self):
        return self._is_valid_bst(self.root, float('-inf'), float('inf'))
    def _is_valid_bst(self, node, min_val, max_val):
        if node is None:
            return True
        if not(min_val<node.value<max_val):
            return False
        return(self._is_valid_bst(node.left, min_val, node.value) and self._is_valid_bst(node.right, node.value, max_val))
bst = BinarySearchTree()
bst.insert(10)
bst.insert(20)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
print("Maximunm value in BinarySearchTree:",bst.find_max())
print("Total number of nodes:", bst.count_nodes())
print("level-order traversal:", bst.level_order_traversal())
print("The height of BinarySearchTree:", bst.find_height())
print("Is valid BinarySearchTree?:", bst.is_valid_bst())



 