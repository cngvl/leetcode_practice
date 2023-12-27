# Constraints:
# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9

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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        pass


LList = LinkedList()
LList.append(1)
LList.append(2)
LList.append(2)
LList.append(1)
LList.display()

sol = Solution()
sol.isPalindrome()


# head = [1,2,2,1]
# >>> true

# head = [1,2]
# >>> false
