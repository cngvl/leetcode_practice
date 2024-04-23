# Constraints:
    # 3 <= nums.length <= 3000
    # -105 <= nums[i] <= 105
    # return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0

# Read the first hint already and it mentioned something along the lines of take out the first number and then the latter two numbers can be treated like Leetcode Q1 ( Two Sum )
    # TwoSum solution was to
        # iterate through the array once, and store each number into a HashMap, ( storing val and index )
        # For each iteration, check if the compliment of the CURRENT ITERATION's number has been seen before


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        returnList = []
        for firstNum in range(len(nums) - 2):
            # print(f'First num: {nums[firstNum]}')
            secondAndThirdHash = {}
            smallReturnList = []
            # print(nums[firstNum])
            for secondNum in range(firstNum + 1,len(nums) - 1):
                if secondNum not in secondAndThirdHash:
                    secondAndThirdHash[nums[secondNum]] = 1
                if (0 - (nums[firstNum] + nums[secondNum])) in secondAndThirdHash:
                    # print(nums[firstNum])
                    # print(0 - (nums[firstNum] + nums[secondNum]))
                    # print(nums[secondNum])
                    smallReturnList = [nums[firstNum], (0 - (nums[firstNum] + nums[secondNum])), nums[secondNum]]
                    print(smallReturnList)


            # print('x')


sol = Solution()
nums = [-1,0,1,2,-1,-4]
sol.threeSum(nums)
# >>> [[-1,-1,2],[-1,0,1]]

# nums = [0,1,1]
# sol.threeSum(nums)
# >>> []

# nums = [0,0,0]
# sol.threeSum(nums)
# >>> [[0,0,0]]
