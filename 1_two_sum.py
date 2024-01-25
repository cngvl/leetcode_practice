# Constraints:
    # 2 <= nums.length <= 104
    # -109 <= nums[i] <= 109
    # -109 <= target <= 109
    # Only one valid answer exists.


# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seenHash = {}

        for pos in range(0, len(nums)):
            if target - nums[pos] in seenHash:
                # print([seenHash[target - nums[pos]], pos])
                return [seenHash[target - nums[pos]], pos]
            else:
                seenHash[nums[pos]] = pos

        # pass

# nums = [2,7,11,15]
# target = 9
# >>> [0,1]

# nums = [3,2,4]
# target = 6
# >>> [1,2]

nums = [3,3]
target = 6
# >>> [0,1]

sol = Solution()
sol.twoSum(nums, target)
