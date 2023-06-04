# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
# I think this is like a two step program
# Need to first filter out any elements that have duplicates
# And then return if there are any two values that subtract to be <= k

# The question its just fuckin worded like dogshit
# K refers to the size of the sliding window

# One option is to remove all the unique elements?
    # Then I'll be left with only sets of dupes, which can then be sorted - this fails ex3 though

def containsNearbyDuplicate(nums, k):
    print(nums)


nums = [1,2,3,1]
k = 3
# >>> true
# Only one set of dupes

nums = [1,0,1,1]
k = 1
# >>> true
# Also only one set of dupes

nums = [1,2,3,1,2,3]
k = 2
# >>> false
# Is this because there are MULTIPLE sets of duplicates?

containsNearbyDuplicate(nums, k)
