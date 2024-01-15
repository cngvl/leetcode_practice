# Constraints:
    # 0 <= nums.length <= 20
    # -231 <= nums[i] <= 231 - 1
    # All the values of nums are unique.
    # nums is sorted in ascending order.

class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        pass

nums = [0,1,2,4,5,7]
# >>> ["0->2","4->5","7"]

# nums = [0,2,3,4,6,8,9]
# >>> ["0","2->4","6","8->9"]

sol = Solution()
sol.summaryRanges(nums)
