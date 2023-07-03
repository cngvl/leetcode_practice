# Constraints:
    # 1 <= nums.length <= 10^5
    # -10^4 <= nums[i] <= 10^4
    # k is in the range [1, the number of unique elements in the array].
    # It is guaranteed that the answer is unique.

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        print(list, k)

nums = [1,1,1,2,2,3]
k = 2
# >>> [1,2]

# nums = [1]
# k = 1
# >>> [1]

s = Solution()
s.topKFrequent(nums, k)
