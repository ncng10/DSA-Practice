#   You're given the head of a Singly Linked List whose nodes are in sorted order
#   with respect to their values. Write a function that returns a modified version
#   of the Linked List that doesn't contain any nodes with duplicate values. The
#   Linked List should be modified in place (i.e., you shouldn't create a brand
#   new list), and the modified Linked List should still have its nodes sorted
#   with respect to their values.
#   Each <span>LinkedList</span> node has an integer <span>value</span> as well as
#   a <span>next</span> node pointing to the next node in the list or to
#   <span>None</span> / <span>null</span> if it's the tail of the list.

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    currNode = linkedList
    while currNode is not None:
        nextDistinctNode == currNode.next
        while nextDistinctNode is not None and nextDistinctNode.value == currNode:
            nextDistinctNode == nextDistinctNode.next
        currNode.next = nextDistinctNode
        currNode = nextDistinctNode
    return linkedList
