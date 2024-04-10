# Constraints:
    # 1 <= nums.length <= 105
    # -109 <= nums[i] <= 109
    # 0 <= k <= 105

# Second attempt at this question - couldn't solve first time around but this question looks kind of straight forward?
# Don't think I've seen the solution for this question before but I at least don't remember it
# Looks like a sliding window question
# At the start, initialise two pointers and then create a 'window' of size k
# Once the window is of size k, slide the window across till the rightPointer reaches the end
# Need to consider what happens if len(nums) is small


# Issues I didn't initially think about
# It ends 'early'
    # Starts off fine by starting off by creating a window of maximum size and then iterating till rightPointer reaches the end
    # Doesn't consider the case when the 'window' is less than k at the END of the array. e.g. the last two elements of the array are dupes
    # Can fix this by adding another loop at the end?
        # I'd assume theres a cleaner way of doing this in a single loop but fk it

# Doesn't consider if the window is in the middle AND it's smaller than k
# A 'brute force' method of checking k sized windows for every leftPoiner iteration would be O(n2)?
# Hint: Topics include Array, HashMap and Sliding Window
# I get the sliding window part but not sure how to incorp hashMap into this
# Can add a hashMap for each value rightPointer comes across
    # Store the val and index for each number crossed
    # After BOTH while loops are done I can loop through the hashMap and see if the val has multiple indexes - This might make the while loops redundant
        # If so, check if any of the index differences are <= k - This gets really weird when there's a long list of indexes seen

# After watching NeetCode solution:
    # My logic was MOSTLY okay
        # Error was trying to keep my initial solution and then add parts to account for the cases I didn't initially predict
        # Dupe vals should already give off the hint that HashMaps can be used
        # Can create a window of max size and then shift the window down
            # The window should contain all of the elements inside

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        numsHash = {}
        leftPointer = 0

        for rightPointer in range(len(nums)):
            # print(rightPointer)

            if rightPointer - leftPointer > k:
                # numsHash[nums[leftPointer]] = True
                del numsHash[nums[leftPointer]]
                leftPointer += 1
            if nums[rightPointer] in numsHash:
                print('True')
                # return True

            numsHash[nums[rightPointer]] = rightPointer

        print('False')
        # return False


sol = Solution()
# nums = [1,2,3,1]
# k = 3
# # >>> true
# sol.containsNearbyDuplicate(nums, k)

# nums = [1,0,1,1]
# k = 1
# >>> true
# sol.containsNearbyDuplicate(nums, k)

# nums = [1,2,3,1,2,3]
# k = 2
# >>> false
# sol.containsNearbyDuplicate(nums, k)

nums = [0,1,2,3,2,5]
k = 3
# >>> true
sol.containsNearbyDuplicate(nums, k)
