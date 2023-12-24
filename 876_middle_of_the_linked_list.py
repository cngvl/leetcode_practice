# Constraints:
# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100

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

# I have no clue how to even attempt this
    # Maybe I can do a double counter? Fast + slow
        # If the Fast breaks then take the slow value¿¿
    # Is the simple counter just too easy¿? // 2 - misunderstood the question
        # Need to return all the nodes downstream of the middle


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slowNode = head
        fastNode = slowNode

        while fastNode and fastNode.next:
            slowNode = slowNode.next
            fastNode = fastNode.next.next

        return slowNode

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)
ll.display()

sol = Solution()
sol.middleNode(ll.head.next)

# head = [1,2,3,4,5]
# >>> [3,4,5]

# head = [1,2,3,4,5,6]
# >>> [4,5,6]
