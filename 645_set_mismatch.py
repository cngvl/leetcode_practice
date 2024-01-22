# Constraints:
# 2 <= nums.length <= 104
# 1 <= nums[i] <= 104

# Will probably need some counter with hash
# Not sure how to find the missing val
# Can probably figure out 1 to n using range + len(nums)
# Might be able to remove one loop
# Can start off using a range loop rather than just looping through nums

class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        seenHash = {}
        dupeVal = 0
        missingVal = 0

        for num in nums:
            if num not in seenHash:
                seenHash[num] = 1
            else:
                seenHash[num] += 1

        for pos in range(1, len(nums) + 1):
            ifCheck = pos not in seenHash
            if pos not in seenHash:
                missingVal = pos

            elif seenHash[pos] == 2:
                dupeVal = pos

        returnList = [dupeVal, missingVal]
        print(returnList)

        return returnList


# nums = [1,2,2,4]
# >>> [2,3]

# nums = [1,1]
# >>> [1,2]

nums = [1,2,3,4,5,6,7,8,9,10,10]
# >>> [10, 11]

sol = Solution()
sol.findErrorNums(nums)
