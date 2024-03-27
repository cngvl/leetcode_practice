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

# Constraints:
    # The number of nodes in the list is in the range [1, 105].
    # 0 <= Node.val <= 9

# Follow up: Could you do it in O(n) time and O(1) space?

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        return

# head = [1,2,2,1]
# >>> true

# head = [1,2]
# >>> false

sol = Solution()
LList1 = LinkedList()
LList1.append(1)
LList1.append(2)
LList1.append(2)
LList1.append(1)
LList1.display()
sol.isPalindrome(LList1.head.next)

LList2 = LinkedList()
LList2.append(1)
LList2.append(3)
LList2.display()
sol.isPalindrome(LList2.head.next)
