class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # print(nums, target)
        min = 0
        max = len(nums) - 1
        while max >= min:
            middle = (min + max) // 2
            if target == nums[middle]:
                return middle
            elif target > nums[middle]:
                min = middle + 1
            else:
                max = middle - 1
        return -1

nums = [-1,0,3,5,9,12]
target = 9
# >>> 4

# nums = [-1,0,3,5,9,12]
# target = 2
# >>> -1

s = Solution()
print(s.search(nums, target))
