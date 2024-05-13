# Constraints:
    # 0 <= nums.length <= 100
    # 0 <= nums[i] <= 50
    # 0 <= val <= 100

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        print('x')

sol = Solution()
nums = [3,2,2,3]
val = 3
sol.removeElement(nums, val)
# >>> 2, nums = [2,2,_,_]

# nums = [0,1,2,2,3,0,4,2]
# val = 2
# >>> 5, nums = [0,1,4,0,3,_,_,_]
