# Constraints:
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.

# Looks like basic stack / counting question using if else

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        maxConsec = 0
        currStreak = 0

        for num in nums:
            if num == 1:
                currStreak += 1
                maxConsec = max(currStreak, maxConsec)
            elif num == 0:
                currStreak = 0

        print(maxConsec)

        return maxConsec




# nums = [1,1,0,1,1,1]
# >>> 3

nums = [1,0,1,1,0,1]
# >>> 2

nums = [0]
# >>> 0

nums = [1]
# >>> 1

sol = Solution()
sol.findMaxConsecutiveOnes(nums)
