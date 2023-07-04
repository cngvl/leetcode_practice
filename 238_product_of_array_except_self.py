# Constraints:
# 2 <= nums.length <= 10&5
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        print(nums)



nums = [1,2,3,4]
# >>> [24,12,8,6]

# nums = [-1,1,0,-3,3]
# >>> [0,0,9,0,0]

s = Solution()
s.productExceptSelf(nums)
