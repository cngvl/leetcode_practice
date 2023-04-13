require 'pry-byebug'

# Definition for singly-linked list.
class ListNode
    attr_accessor :val, :next
    def initialize(val = 0, _next = nil)
        @val = val
        @next = _next
    end
end

list2 = ListNode.new
list1 = ListNode.new
# list1 = [1,2,4]
list1.val = 1
list1.next = list2
list1.next.val = 2
# list2.val = 3

# list1.append(4)

# list2 = [1,3,4]
# list2.append(1)
# list2.append(3)
# list2.append(4)

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Input: list1 = [], list2 = []
# Output: []

# Input: list1 = [], list2 = [0]
# Output: [0]


def merge_two_lists(list1, list2)
  result = ListNode.new
  current = result
  # Check if both lists have a linkedlist, if one doesn't exist, return the other
  return list2 if list1 == nil
  return list1 if list2 == nil
  # Run this if both of the lists 'exist'
  # This compares each linked list with eachother by comparing individual nodes
  while list1 != nil && list2 != nil
    # Where does the #val come from?
    if list1.val < list2.val
      current.next = list1
      list1 = list1.next
    else
      current.next = list2
      list2 = list2.next
    end
    current = current.next;
  end
  # This catches any nodes 'left over'
  if list1 != nil
    current.next = list1
    list1 = list1.next
  end

  if list2 != nil
    current.next = list2
    list2 = list2.next
  end

  result.next
end

merge_two_lists(list1, list2)
