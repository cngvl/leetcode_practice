# Custom Judge:
# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }

# Constraints:
# 1 <= nums.length <= 3 * 10^4
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        print(nums)

nums = [1,1,2]
# >>> 2, nums = [1,2,_]

# nums = [0,0,1,1,1,2,2,3,3,4]
# >>> 5, nums = [0,1,2,3,4,_,_,_,_,_]

s = Solution()
s.removeDuplicates(nums)
