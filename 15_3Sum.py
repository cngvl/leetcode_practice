# Constraints:
    # 3 <= nums.length <= 3000
    # -105 <= nums[i] <= 105
    # return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0

# Read the first hint already and it mentioned something along the lines of take out the first number and then the latter two numbers can be treated like Leetcode Q1 ( Two Sum )
    # TwoSum solution was to
        # iterate through the array once, and store each number into a HashMap, ( storing val and index )
        # For each iteration, check if the compliment of the CURRENT ITERATION's number has been seen before

# Coming back to finish off the question
    # Issue with first iteration of the solution
    # Would use the most recently added num to create a solution ( same indexed val )
    # e.g. 2 -1 and then the same -1

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        returnList = []
        for firstNum in range(len(nums) - 2):
            # print(f'First num: {nums[firstNum]}')
            smallReturnList = []
            # print(nums[firstNum])
            # print('start of secondNum loop')
            secondAndThirdHash = {}
            for secondNum in range(firstNum + 1,len(nums)):
                # print(nums[secondNum])
                target = (0 - (nums[firstNum] + nums[secondNum]))
                # if ((0 - (nums[firstNum] + nums[secondNum])) in secondAndThirdHash) and (secondAndThirdHash[nums[secondNum]] != secondNum):
                if target in secondAndThirdHash:
                    # print(nums[firstNum])
                    # print(0 - (nums[firstNum] + nums[secondNum]))
                    # print(nums[secondNum])
                    smallReturnList = [nums[firstNum], target, nums[secondNum]]
                    smallReturnList.sort()
                    # print(smallReturnList)

                    if smallReturnList not in returnList:
                        returnList.append(smallReturnList)

                if secondNum not in secondAndThirdHash:
                    secondAndThirdHash[nums[secondNum]] = secondNum

            # print('End of secondNum loop')
        print(returnList)


    def threeSumNeetCode(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            l , r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res


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

# Failed test case
# nums = [34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49]
# sol.threeSum(nums)
