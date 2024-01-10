# Constraints:
    # The number of nodes in the list is in the range [0, 300].
    # -100 <= Node.val <= 100
    # The list is guaranteed to be sorted in ascending order.

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

# Thought about the question throughout the days I didn't actively work on it
    # the issue currently being faced is how to deal with the final nodes
    # can do a current and current.next loop?
        # can't do next and nextnext?¿
            # Would break with head = [1,2,2]
        # I need? access to three nodes at one time?

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current.next:
            if current.val == current.next.val:
                # Erase the current node and replace it with the next node
                current.next = current.next.next
            else:
                current = current.next

        return head

# head = [1,1,2]
# >>> [1,2]

# head = [1,2,2]
# >>> [1,2]

# head = [1,1,2,3,3]
# >>> [1,2,3]

LList1 = LinkedList()
LList1.append(1)
LList1.append(1)
LList1.append(2)
LList1.display()

sol = Solution()
sol.deleteDuplicates(LList1.head)
LList1.display()
