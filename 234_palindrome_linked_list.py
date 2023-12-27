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


# Once again, I have no clue how to solve this
    # Doing the seen value array method seems so cheat

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        seenValues = []
        currentNode = head
        while currentNode:
            seenValues.append(currentNode.val)
            currentNode = currentNode.next

        return seenValues == seenValues[::-1]

    # NeetCode solution
    def isPalindrome2(self, head: ListNode) -> bool:
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


LList = LinkedList()
LList.append(1)
LList.append(2)
# LList.append(2)
# LList.append(1)
LList.display()

sol = Solution()
sol.isPalindrome(LList.head.next)


# head = [1,2,2,1]
# >>> true

# head = [1,2]
# >>> false
