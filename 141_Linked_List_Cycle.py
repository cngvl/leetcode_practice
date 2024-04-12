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
    # The number of the nodes in the list is in the range [0, 104].
    # -105 <= Node.val <= 105
    # pos is -1 or a valid index in the linked-list.

# Follow up: Can you solve it using O(1) (i.e. constant) memory?

# Not even sure how to set up test cases for this to try out my code
# pos is NOT passed as a parameter
# First thought would be to see if there's an infinite loop?
    # Would this need some sort of counter¿? - there's a constraint to how many nodes there are in the LList but it's 10^4
    # This runs in O(n) but sounds a bit silly - it does satisfy the constant memory follow up Q but
# How does the constraint of 'pos is -1 or avalid index in the linked-list' change anything
    # I don't even know what it means to be honest bruvs

# The solution worked¿?¿?
# Question is listed as HashMap, LList and TwoPointers
    # The faster solutions used the fast + slow pointer method but I don't actually get the logic

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        numberNodesSeen = 0

        if not head:
            return False

        curr = head.next
        while curr:
            numberNodesSeen += 1
            if numberNodesSeen > 10_000:
                return True

            curr = curr.next

        return False

    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

sol = Solution()

# head = [3,2,0,-4], pos = 1
# >>> true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# head = [1,2], pos = 0
# >>> true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

# head = [1], pos = -1
# >>> false
# Explanation: There is no cycle in the linked list.
