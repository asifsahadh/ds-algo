# binary search tree

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        
class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, root, value):
        if root is None:
            return Node(value)
        if value < root.value:
            root.left = self.insert(root.left, value)
        elif value > root.value:
            root.right = self.insert(root.right, value)
        return root
        
    def search(self, root, value):
        if root is None or root.value == value:
            return root
        if value < root.value:
            return self.search(root.left, value)
        return self.search(root.right, value)
        
    def find_min(self, root):
        if root is None:
            return root
        temp = root
        while temp and temp.left is not None:
            temp = temp.left
        return temp
        
    def find_max(self, root):
        if root is None:
            return root
        temp = root
        while temp and temp.right is not None:
            temp = temp.right
        return temp

    def delete(self, root, value):
        if root is None:
            return root
        if value < root.value:
            root.left = self.delete(root.left, value)
        elif value > root.value:
            root.right = self.delete(root.right, value)
        else: # here, we found the node to delete
            # leaf
            if root.left is None and root.right is None: 
                return None
            # one child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # two children
            successor = self.find_min(root.right)
            root.key = successor.key
            root.right = self.delete(root.right, successor.key)
        return root