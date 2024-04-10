# Constraints:
    # 1 <= nums.length <= 105
    # -109 <= nums[i] <= 109
    # 0 <= k <= 105

# Second attempt at this question - couldn't solve first time around but this question looks kind of straight forward?
# Don't think I've seen the solution for this question before but I at least don't remember it
# Looks like a sliding window question
# At the start, initialise two pointers and then create a 'window' of size k
# Once the window is of size k, slide the window across till the rightPointer reaches the end

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        pass

sol = Solution()
nums = [1,2,3,1]
k = 3
# >>> true
sol.containsNearbyDuplicate(nums, k)

# nums = [1,0,1,1]
# k = 1
# >>> true
# sol.containsNearbyDuplicate(nums, k)

# nums = [1,2,3,1,2,3]
# k = 2
# >>> false
# sol.containsNearbyDuplicate(nums, k)
