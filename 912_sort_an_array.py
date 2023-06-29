# Constraints:
# 1 <= nums.length <= 5 * 10^4
# -5 * 10^4 <= nums[i] <= 5 * 10^4

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        print(nums)



nums = [5, 2, 3, 1]
# >>> [1, 2, 3, 5]

nums = [5, 1, 1, 2, 0, 0]
# >>> [0, 0, 1, 1, 2, 5]

s = Solution()
s.sortArray(nums)
