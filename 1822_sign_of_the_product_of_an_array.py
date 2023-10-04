class Solution:
    def arraySign(self, nums: list[int]) -> int:
        # print(nums)
        startNum = 1
        for num in nums:
            startNum * num

        if startNum > 0:
            return 1
        elif startNum == 0:
            return 0
        else:
            return -1




# nums = [-1,-2,-3,-4,3,2,1]
# >>> 1

nums = [1,5,0,2,-3]
# >>> 0

# nums = [-1,1,-1,1,-1]
#  >>> -1

s = Solution()
s.arraySign(nums)
