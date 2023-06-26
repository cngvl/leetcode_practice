class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        print(nums)


s = Solution()
s.nums = [1,7,3,6,5,6]
# >>> 3
# 1 8 11 17 22 28

# nums = [1,2,3]
# >>> -1

# nums = [2,1,-1]
# >>> 0


# def pivotIndex(nums):
#     # Alternative method is to loop through the array
#     # At each step, calculate what is the sum of everything before and after the pointer, as two seperate sums
#     # 0 .. pointer
#     # pointer .. -1
#     position = 0
#     for position in range(len(nums) + 1):
#         print('Left loop values:')
#         left_sum = 0
#         for i in nums[0:position]:
#             print(i)
#             left_sum += i
#         print('Right loop values:')
#         right_sum = 0
#         for j in nums[position:-1]:
#             print(j)
#             right_sum += j


pivotIndex(nums)
