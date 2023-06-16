class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        # min, max = 0, len(nums) - 1
        min, max = 0, len(nums)
        while min < max:
            # mid = (min + max) // 2
            mid = min +(max - min) // 2
            # if target == nums[mid]:
            #     print("If")
            #     return mid
            if target > nums[mid]:
                print("Elif")
                min = mid + 1
            else:
                print("Else")
                max = mid
        return min

# nums = [1,3,5,6]
# target = 5
# >>> 2

# nums = [1,3,5,6]
# target = 2
# >>> 1

nums = [1,3,5,6]
target = 7
# >>> 4

# nums = [1,2,3,4,5,6,7,8,9,10,11,12]
# target = 6
# >>> 5

# nums = [1,2,3,4,5,6,7,8,9,10,11,12]
# target = 2
# >>> 1

s = Solution()
print(s.searchInsert(nums, target))
