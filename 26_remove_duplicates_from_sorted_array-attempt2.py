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


# Not sure why I can't do a standard loop
# But I can potentially use some two pointer method?

# First solution
while False:
    class Solution:
        def removeDuplicates(self, nums: list[int]) -> int:
            pointer1 = 0
            pointer2 = 1

            while pointer2 < len(nums):
                if nums[pointer1] == nums[pointer2]:
                    pointer2 += 1
                elif nums[pointer1] < nums[pointer2]:
                    nums[pointer1 + 1] = nums[pointer2]
                    pointer1 += 1
                    pointer2 += 1

            return nums

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        pointer1 = 1
        print(nums)

        for pointer2 in range(1, len(nums)):
            if nums[pointer2] != nums[pointer2 - 1]:
                nums[pointer1] = nums[pointer2]
                pointer1 += 1

        return pointer1

# nums = [1,1,2]
# >>> 2, nums = [1,2,_]

nums = [0,0,1,1,1,2,2,3,3,4]
# >>> 5, nums = [0,1,2,3,4,_,_,_,_,_]

# nums = [0,1,2,3,4,5]
# >>> 6

s = Solution()
s.removeDuplicates(nums)
