# Instructions
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
    # Does this imply theres only ONE majority element? - no, read the instructions bruv

# Test Cases
# nums = [3,2,3] - 3 nums
# >>> 3

# nums = [2,2,1,1,1,2,2] - 7 nums
# >>> 2

import math

# class Solution:
# def majorityElement(self, nums: List[int]) -> int:
def majorityElement(nums):
    # Make a hash?
    # hashSet = set()
    # for num in nums:
    #     print(num)
    #     if num in hashSet:
    #         print('New')
    #     else:
    #         print('Old')
    # Does the array only have 2 vals?
    nums.sort()
    # middle_value = math.floor(len(nums) / 2)
    return nums[math.floor(len(nums) / 2)]


nums = [2,2,1,1,1,2,2]
print(f'{majorityElement(nums)}')
# majorityElement(nums)
