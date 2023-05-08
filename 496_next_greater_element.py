
# nums1 = [4,1,2]
# nums2 = [1,3,4,2]
# >>> [-1,3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
# - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

# nums1 = [2,4]
# nums2 = [1,2,3,4]
# >>> [3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
# - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.

# Need to worry about duplicate values? - conditions state all values will be UNIQUE

# Need to loop through num1
# Get the index of num1 values in num2
# Create an inner loop? - O(n2) time complexity
# Check nums2.index(nums1_value) +

# while - while loop can probably work? but might make an infinite loop
# for - for loop is too much? I don't need to loop through every single element every time, just need those downstream
# for with range - still have similar issue to above

def nextGreaterElement(nums1, nums2):
    return_array = []
    for nums1_value in nums1:
        # print(nums1_value)
        # Do I even need the index?
        # nums1_index_in_nums2 = nums2.index(nums1_value)
        # print(nums1_index_in_nums2)
        # for nums2_value in nums2:
            # print(nums2[nums1_index_in_nums2])
        next_biggest_element = next((nums2_value for nums2_value in nums2 if nums2_value > nums1_value and nums2.index(nums2_value) > nums2.index(nums1_value) ), -1)
        # This loops through nums2, need to add second conditon to if statement to ensure the index values are higher
        # print(next_biggest_element)
        return_array.append(next_biggest_element)
    return return_array

# nums1 = [4,1,2]
# nums2 = [1,3,4,2]
nums1 = [2,4]
nums2 = [1,2,3,4]
# >>> [-1,3,-1]
print(nextGreaterElement(nums1, nums2))

# yb big stinker
