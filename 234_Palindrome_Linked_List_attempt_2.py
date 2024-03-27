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

# First attempt was kind of cheater method
    # Used an array to store the values seen and checked if reversed array was == to seen array

# Creating another flipped LList seems like a harder way to solve the Q
    # No access to prev element?¿
    # There's definitely a smarter way to do it because the followup prompt asks for it
    # Question is listed as TwoPointer, Stack and Recursion

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = head
        slow = head

        # find the middle (slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        # check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

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
print(sol.isPalindrome(LList1.head.next))

LList2 = LinkedList()
LList2.append(1)
LList2.append(3)
LList2.display()
sol.isPalindrome(LList2.head.next)
