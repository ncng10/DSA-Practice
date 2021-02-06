# Write a function that takes in a Binary Search Tree (BST) and a target integer
# value and returns the closest value to that target value contained in the BST.
# You can assume that there will only be one closest value.

def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, tree.value)


# Create helper to keep track of value
def findClosestValueInBstHelper(tree, target, closest):
    currNode = tree
    while currNode is not None:
        if abs(target - currNode.value) < abs(closest - target):
            closest = currNode.value
        if target > currNode.value:
            currNode = currNode.right
        elif target < currNode.value:
            currNode = currNode.left
        else:
            break
    return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
