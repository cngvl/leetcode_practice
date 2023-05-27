# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """

# Can't do any intial sorting because the question specifies to keep the relative order of the non-zero elements
# Two pointer question
    # Can make two pointers, both starting at the intial position
    # One stays at the zeros, while the other

def moveZeroes(nums):
    print(nums)



nums = [0]
# >>> [0]

nums = [0,1,0,3,12]

# 1 0 0 3 12
# 1 3 0 0 12
# 1 3 12 0 0
# >>> [1,3,12,0,0]

moveZeroes(nums)
