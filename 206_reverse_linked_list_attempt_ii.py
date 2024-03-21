
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

# First attempt at this question I did a 'cheater' method
    # I transversed through the input LList and stored the vals in an array
    # Flipped and went through the array and made a new LList to return

# Intended method was to transverse through the list and flip each of the direction of the next pointer?

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            print(curr.val)
            # temp = curr
            # nextNode = curr.next
            # nextNode.next = temp
            # curr = curr.next
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        return prev

node = LinkedList()
node.append(1)
node.append(2)
node.append(3)
node.append(4)
node.append(5)
print('Display BEFORE:')
node.display()

sol = Solution()
sol.reverseList(node.head.next)
print('Display AFTER:')
node.display()

# node.display()

# head = [1,2,3,4,5]
# >>> [5,4,3,2,1]

# head = [1,2]
# >>> [2,1]

# head = []
# >>> []
