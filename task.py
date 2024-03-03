class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.value < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def tree_height(node):
    ######         Write your program here       ######
    ###                                             ###
    ###                                             ###
    ###                                             ###
    ###                                             ###
    ###                                             ###
    ###                                             ###
    ###                                             ###
    ###                                             ###
    ###################################################
# Input string

input_str = input()
# Convert input string to a list of numbers
numbers = [int(n) for n in input_str.split()]

# Building the BST
root = None
for number in numbers:
    root = insert(root, number)

# Calculating the height of the BST
height = tree_height(root)
print(f"The height of the tree is: {height}")
