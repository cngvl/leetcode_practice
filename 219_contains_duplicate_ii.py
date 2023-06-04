# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
# I think this is like a two step program
# Need to first filter out any elements that have duplicates
# And then return if there are any two values that subtract to be <= k

# The question its just fuckin worded like dogshit
# K refers to the size of the sliding window

# One option is to remove all the unique elements? - WONT WORK
    # Then I'll be left with only sets of dupes, which can then be sorted - this fails ex3 though


# Could I do something a lil slick by sorting first and seeing if there's any duplicates,
    # then checking the ORIGINAL array for the distance between the two?

# Currently thinking about some dynamically sized sliding window?
    # Check 0 gap, 1 gap, 2 gap etc. til k gap
    # If nothing, shift window one step rightwards


def containsNearbyDuplicate(nums, k):
    # print(nums)
    # sortedNums = sorted(nums)
    pointer1, pointer2 = 0, 1

    while pointer1 < len(nums):
        while pointer2 < len(nums) :
            if nums[pointer1] == nums[pointer2] and abs(pointer1 - pointer2) <= k:
                return True

            if abs(pointer1 - pointer2 + 1) <= k:
                pointer2 += 1
            else:
                break

        pointer1 += 1
        pointer2 = pointer1 + 1


    return False


nums = [1,2,3,1]
k = 3
# >>> true

nums = [1,0,1,1]
k = 1
# >>> true

# nums = [1,2,3,1,2,3]
# k = 2
# >>> false

print(containsNearbyDuplicate(nums, k))
