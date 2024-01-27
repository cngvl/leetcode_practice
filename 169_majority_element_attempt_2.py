# Constraints:
    # n == nums.length
    # 1 <= n <= 5 * 104
    # -109 <= nums[i] <= 109

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
            # nums.sort()
            # return nums[math.floor(len(nums) / 2)]
        pass


# nums = [3,2,3]
# >>> 3

nums = [2,2,1,1,1,2,2]
# >>> 2

sol = Solution()
sol.majorityElement(nums)
