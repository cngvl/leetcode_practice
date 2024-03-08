# Constraints:
    # 1 <= nums.length <= 100
    # 1 <= nums[i] <= 100

# HashMap iteration question?
    # Create a hashmap
    # Loop through that hashmap and create a counter
        # Might be a way to check for max and then add to counter all in one?
    # Return countertotal

class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        numsHash = {}
        max = 0
        totalFreq = 0

        for num in nums:
            if num not in numsHash:
                numsHash[num] = 1
            else:
                numsHash[num] += 1

        # print(numsHash)

        for num in nums:
            if max < numsHash[num]:
                max = numsHash[num]
                totalFreq = 1
            elif max == numsHash[num]:
                totalFreq += 1

        print(f'max = {max}')

        print(f'totalFreq = {totalFreq}')






# nums = [1,2,2,3,1,4]
# >>> 4

nums = [1,2,3,4,5]
# Output: 5

sol = Solution()
sol.maxFrequencyElements(nums)
