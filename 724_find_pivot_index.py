# Constraints:
# 1 <= nums.length <= 10^4
# -1000 <= nums[i] <= 1000

# One thing I missed out the first time I did this question was that I needed to find the LEFTMOST index

# Initially thought to use two loops, one going leftwards and the other going rightwards

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        for position in range(0, len(nums)):
            leftTotal = sum(nums[position::])
            rightTotal = sum(nums[position::-1])
            if leftTotal == rightTotal:
                return position
        return -1

# def pivotIndex(nums):
#     # Alternative method is to loop through the array
#     # At each step, calculate what is the sum of everything before and after the pointer, as two seperate sums
#     # 0 .. pointer
#     # pointer .. -1
#     position = 0
#     for position in range(len(nums) + 1):
#         print('Left loop values:')
#         left_sum = 0
#         for i in nums[0:position]:
#             print(i)
#             left_sum += i
#         print('Right loop values:')
#         right_sum = 0
#         for j in nums[position:-1]:
#             print(j)
#             right_sum += j

nums = [1,7,3,6,5,6]
# >>> 3
# 1 8 11 17 22 28

# nums = [1,2,3]
# >>> -1

# nums = [2,1,-1]
# >>> 0

s = Solution()
s.pivotIndex(nums)
