# Constraints:
    # 1 <= nums.length <= 3 * 104
    # -3 * 104 <= nums[i] <= 3 * 104
    # Each element in the array appears twice except for one element which appears only once.

# "You must implement a solution with a linear runtime complexity and use only constant extra space."
# Is the biggest hurdle in this question
# Can't use a stack to append/pop either because I can't assume the numbers will be adjacent with eachother
    # can sort before any testing
# can do some twopointer comparison but not sure how to handle out of index errors
    # [1,1,3]


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        nums.sort()
        for pos in range(0,len(nums)-1,2):
            # print(pos)
            if nums[pos] != nums[pos + 1]:
                # print(pos)
                return nums[pos]

        return nums[-1]

nums = [2,2,1]
# >>> 1

# nums = [4,1,2,1,2]
# >>> 4

# nums = [1]
# >>> 1

# nums = [1,1,2,2,3,3,4,4,5,5,6,6,7]
# >>> 7

sol = Solution()
print(sol.singleNumber(nums))
