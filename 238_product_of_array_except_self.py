# Constraints:
    # 2 <= nums.length <= 10&5
    # -30 <= nums[i] <= 30
    # The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
    # You must write an algorithm that runs in O(n) time and without using the division operation.

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

# My notes:
    # O(n) times makes me think that I should run some sort of HashMap solution?
        # I initially thought that I would do something like
        # hashMap[index] = everything but the index
        # hashMap[1] = 234
        # hashMap[2] = 134
    # Is there even a need to store the values in a hashmap?

import numpy

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # hashMap = {}
        answerArray = []
        # OriginalNums = nums[:]

        for pos in range(len(nums)):
            # print(nums[pos])
            baseNums = nums[:]
            baseNums.pop(pos)
            listProduct = numpy.prod(baseNums)
            answerArray.append(listProduct)
            # del baseNums[pos]

        return answerArray



nums = [1,2,3,4]
# >>> [24,12,8,6]

# nums = [-1,1,0,-3,3]
# >>> [0,0,9,0,0]

s = Solution()
s.productExceptSelf(nums)
