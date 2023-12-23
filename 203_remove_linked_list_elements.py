# Constraints:
# The number of nodes in the list is in the range [0, 104].
# 1 <= Node.val <= 50
# 0 <= val <= 50

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

# Thought about this question briefly before
    # Need to consider if the node is in the LAST position and if the whole LinkedList is filled with nodes of the same target val
    # I could just do the same method as q206
        # Run through the input LinkedList and append the values into an array
        # Create a new LinkedList with the values from the array
    # Will attempt to change the LinkedList in place rather than create a new one
        # Might just cheese it to start and then attempt the "better" method after

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        seenValues = []
        currentNode = head
        while currentNode:
            if currentNode.val != val : seenValues.append(currentNode.val)
            currentNode = currentNode.next

        newHead = ListNode()
        newCurrent = newHead
        for value in seenValues:
            newCurrent.next = ListNode(value)
            newCurrent = newCurrent.next

        return newHead.next

    def removeElements2(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        currentNode = head
        nextNode = currentNode.next
        while nextNode:
            if currentNode.val == val:
                print('x')
        return head

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(6)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)
ll.display()

sol = Solution()
sol.removeElements2(ll.head.next, 6)

# head = [1,2,6,3,4,5,6]
# val = 6
# >>> [1,2,3,4,5]
# head = []
# val = 1
# >>> []
# head = [7,7,7,7]
# val = 7
# >>> []
