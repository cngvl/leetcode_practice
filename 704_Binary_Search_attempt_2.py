# Constraints:
    # 1 <= nums.length <= 104
    # -104 < nums[i], target < 104
    # All the integers in nums are unique.
    # nums is sorted in ascending order.

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            ifCheck = (target == nums[mid])
            numsCheck = nums[mid]
            elifCheck = (target > nums[mid])

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return -1

sol = Solution()

nums = [-1,0,3,5,9,12]
target = 9
# >>> 4
print(sol.search(nums, target))

nums = [-1,0,3,5,9,12]
target = 2
# >>> -1
print(sol.search(nums, target))
