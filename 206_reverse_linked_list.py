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

# I have no clue how to solve this question
    # Initially I was thinking of looping till you you hit None but then how do I replace that node with the FIRST node, and then keep looping to reverse ALL the nodes?
        # Maybe do some counter and then stop at the midway point?
            # Might not work without the use of a length function
        # "Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?"
        # I thought about the possibility of doing this recursively but I'm still not confident in recursive functions so I'll stick with iteratively for now

    # ChatGPT response shows a different method:
        # To traverse the input LinkedList while storing the values in an array
        # Using the array, create a LinkedList with the values but in reverse order
        # Return the newly created LinkedList

# This is passed the HEAD node, NOT the whole LinkedList
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        LinkedListVals = []
        current_node = head
        while current_node:
            LinkedListVals.append(current_node.val)
            current_node = current_node.next

        # print(current_node)
        newHead = ListNode()
        current = newHead
        for nodeVal in reversed(LinkedListVals):
            current.next = ListNode(nodeVal)
            current = current.next

        return newHead.next

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
