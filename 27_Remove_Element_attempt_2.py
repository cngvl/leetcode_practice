# Constraints:
    # 0 <= nums.length <= 100
    # 0 <= nums[i] <= 50
    # 0 <= val <= 100

# Will need to consider what happens when nums length is 0
# What happens if the only value in nums is the target val?
# Does sorting the input nums help with anything? - Brings all the vals together?

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        print(nums)

        # if len(nums) == 0:
        #     return 0

        # while nums[rightPointer] == val:
        #     rightPointer -= 1

        # while leftPointer < len(nums):
        #     if nums[leftPointer] == val:
        #         temp = nums[leftPointer]
        #         nums[leftPointer] = nums[rightPointer]
        #         nums[rightPointer] = temp
        #         rightPointer -= 1
        #     leftPointer += 1
        left_pointer = 0

        for right_pointer in range(len(nums)):
            if nums[right_pointer] != val:
                nums[left_pointer] = nums[right_pointer]
                left_pointer += 1

        print(nums)



sol = Solution()
# nums = [3,2,2,3]
# val = 3
# sol.removeElement(nums, val)
# >>> 2, nums = [2,2,_,_]

nums = [0,1,2,2,3,0,4,2]
val = 2
sol.removeElement(nums, val)
# >>> 5, nums = [0,1,4,0,3,_,_,_]

# Failed test case
# nums = []
# val = 0
# sol.removeElement(nums, val)
# >>> 0?

# Fails because the initial while loop results in the index error
# nums = [1]
# val = 1
# sol.removeElement(nums, val)
