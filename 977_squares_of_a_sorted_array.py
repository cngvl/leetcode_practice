# Constraints:
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in non-decreasing order.

# find an O(n) solution using a different approach?

# The point of the question is v straightforward but there's a lot of optimisations that are possible?
# Try to find some solution that runs O(n)
    # Selection sort
    # Insertion sort
    # Binary sorting? - Binary SEARCH (Might not be applicable)
        # The question was listed under the binary search category but we'll see

# Do I need to make a seperate ans array? (Might be easier but costs mem)

# This solution WORKS - but uses inbuilt methods which might be cheating
# class Solution:
#     def sortedSquares(self, nums: list[int]) -> list[int]:
#         squaredNums = []
#         for num in nums:
#             squaredNum = num ** 2
#             squaredNums.append(squaredNum)

#         squaredNums.sort()

#         return squaredNums


# class Solution:
#     def sortedSquares(self, nums: list[int]) -> list[int]:
#         squaredNums = []
#         for num in nums:
#             squaredNum = num ** 2
#             squaredNums.append(squaredNum)
#             # I shouldn't append the nums straight away, should do the insertion sort check here

#         for step in range(1, len(squaredNums)):
#             # print(value)
#             key = squaredNums[step]
#             j = step - 1

#             while j >= 0 and key < squaredNums[j]:
#                 squaredNums[j + 1] = squaredNums[j]
#                 j = j - 1

#             squaredNums[j + 1] = key

#         return squaredNums

# Time: O(n), one pass using two pointers.
# Space: O(1), output array is not considered for space complexity.

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0] * n
        l, r = 0, n - 1

        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])
            if left > right:
                res[r - l] = left * left
                l += 1
            else:
                res[r - l] = right * right
                r -= 1
        return res

nums = [-4,-1,0,3,10]
# >>> [0,1,9,16,100]

# [16, 1, 0, 9, 100]

# nums = [-7,-3,2,3,11]
# >>> [4,9,9,49,121]

s = Solution()
print(s.sortedSquares(nums))
