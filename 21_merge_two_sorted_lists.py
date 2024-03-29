# Constraints:
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2

        if list2 == None:
            return list1

        # Do I need to make a new node?
        newHead = ListNode()
        current = newHead

        while list1 and list2:
            List1Val = list1.val
            List2Val = list2.val
            if list1.val <= list2.val:
                # newNode = ListNode(val= list1.val)
                # current = newNode
                current.next = list1
                list1 = list1.next
            else:
                # newNode = ListNode(val= list2.val)
                # current = newNode
                current.next = list2
                list2 = list2.next

            current = current.next

        # if list1.next == None:
        #     while list1.next != None:
        #         current.next = ListNode(val= list1.val)
        #         list1 = list1.next

        # if list2.next == None:
        #     while list2.next != None:
        #         current.next = ListNode(val= list2.val)
        #         list2 = list2.next

        # Append any remaining nodes from list1 or list2 to the merged list
        current.next = list1 if list1 else list2

        return newHead.next

LList1 = LinkedList()
LList1.append(1)
LList1.append(2)
LList1.append(4)
LList1.display()

LList2 = LinkedList()
LList2.append(1)
LList2.append(3)
LList2.append(4)
LList2.display()

sol = Solution()
sol.mergeTwoLists(LList1.head.next, LList2.head.next)


# list1 = [1,2,4]
# list2 = [1,3,4]
# >>> [1,1,2,3,4,4]
# list1 = []
# list2 = []
# >>> []
# list1 = []
# list2 = [0]
# >>> [0]
