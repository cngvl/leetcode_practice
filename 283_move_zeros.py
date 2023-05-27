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
    pointer1 = 0
    pointer2 = 1
    while pointer2 < len(nums):
        if nums[pointer1] == 0 and nums[pointer2] != 0:
            nums[pointer1] = nums[pointer2]
            nums[pointer2] = 0
            pointer1 += 1
        elif nums[pointer1] != 0:
            pointer1 += 1
        pointer2 += 1

    print(nums)

nums = [0]
# >>> [0]

# nums = [0,1,0,3,12]

# 1 0 0 3 12
# 1 3 0 0 12
# 1 3 12 0 0
# >>> [1,3,12,0,0]


# nums = [1,0]
# >>> [1,0]

# nums = [2,1]
# >>> [2,1]

moveZeroes(nums)
