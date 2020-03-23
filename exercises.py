from typing import List

class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def inorder(root: Node) -> List:
    values = []

    def _traverse(root: Node) -> None:
        if root:
            _traverse(root.left)
            values.append(root.value)
            _traverse(root.right)
    
    _traverse(root)
    return values

def is_unival_tree(root: Node) -> bool:
    if root.left is None or (root.value == root.left.value and is_unival_tree(root.left)):
        left_unival = True
    else:
        left_unival = False

    if root.right is None or (root.value == root.right.value and is_unival_tree(root.right)):
        right_unival = True
    else:
        right_unival = False

    return left_unival and right_unival 

print(is_unival_tree(Node(2, Node(2, Node(2), Node(2)), Node(2))))