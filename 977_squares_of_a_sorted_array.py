# Constraints:
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in non-decreasing order.

# find an O(n) solution using a different approach?


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        print(nums)

nums = [-4,-1,0,3,10]
# >>> [0,1,9,16,100]

# nums = [-7,-3,2,3,11]
# >>> [4,9,9,49,121]

s = Solution()
s.sortedSquares(nums)
