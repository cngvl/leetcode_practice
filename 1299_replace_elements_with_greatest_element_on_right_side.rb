require 'pry-byebug'

# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
# Explanation:
# - index 0 --> the greatest element to the right of index 0 is index 1 (18).
# - index 1 --> the greatest element to the right of index 1 is index 4 (6).
# - index 2 --> the greatest element to the right of index 2 is index 4 (6).
# - index 3 --> the greatest element to the right of index 3 is index 4 (6).
# - index 4 --> the greatest element to the right of index 4 is index 5 (1).
# - index 5 --> there are no elements to the right of index 5, so we put -1.

# def replace_elements(arr)
#   # hash = {element, index}
#   # Need to interate over every element in the array (with index?)
#   arr.each_with_index do |e, i|
#     # byebug
#     if (arr[i] < arr[i + 1])
#       arr[i] = arr[i + 1]
#     end
#   end
#   arr[-1] = -1
# end

def replace_elements(arr)
  array = []
  while arr.length != 1
    arr.slice!(0)
    array << arr.max
  end
  p array << -1
end

# def replace_elements(arr)
#   return arr if arr.nil?

#   i = arr.count - 2

#   greatest_element_so_far = arr[i + 1]
#   arr[i + 1] = -1
#   while i >= 0
#     temp = arr[i]
#     # p greatest_element_so_far
#     arr[i] = greatest_element_so_far
#     greatest_element_so_far = temp if temp > greatest_element_so_far
#     i -= 1
#   end
#   arr
# end

arr = [17, 18, 5, 4, 6, 1]
# arr [0, 1, 2, 3, 4, 5]
p replace_elements(arr)
