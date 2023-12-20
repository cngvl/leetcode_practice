# Constraints:
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = ListNode()

    def append(self, val):
        new_node = ListNode(val)
        current = self.head
        while current.next != None:
            current = current.next

        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current.next != None:
            current = current.next
            elements.append(current.val)
        print(elements)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Your code here
        pass


node = LinkedList()
node.append(1)
node.append(2)
node.append(3)
node.append(4)
node.append(5)
node.display()


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Input: head = [1,2]
# Output: [2,1]

# Input: head = []
# Output: []
