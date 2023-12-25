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

# LeetCode solution
# Time Complexity :  O(n)
# Space Complexity : O(1)
class Solution(object):
    def middleNode(self, head):
        # We need two pointers, one is head with one step each iteration, and the other is tmp with two steps each iteration.
        temp = head
        while temp and temp.next:
            # In each iteration, we move head one node forward and we move temp two nodes forward...
            head = head.next
            temp = temp.next.next
        # When temp reaches the last node, head will be exactly at the middle point...
        return head


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
