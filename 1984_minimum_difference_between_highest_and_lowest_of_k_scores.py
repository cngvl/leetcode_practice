# Hint is to SORT the scores
    # By sorting the array first, the scores are as close to eachother as possible
    # The question doesn't require WHICH scores to be returned so this is fine


def minimumDifference(nums, k):
    # I don't exactly get what the k parameter is doing in this case
        # I think K is specifying how many scores to pick from?
        # How big the 'gap' of pointers is
    # My intial thought is to just brute force and run something with O(n2) time complex but that is usually not right
    # might need to use abs()
    # two pointer question
    # maybe make a dictionary to store the combinations? - No need as only the difference between scores needs to be returned
    # How to deal with arrays of size 1
    nums.sort()

    # 'Gap' between the pointers need to be variable in length
    pointer1 = 0
    pointer2 = k - 1
    minimumDiff = max(nums)
    # Need to interate across the array
        # Also need to protect against going out of bounds
        # Do min = min(min, abs(pointer1 - pointer2)) ?
    while pointer2 < len(nums):
        # print(abs(nums[pointer1] - nums[pointer2]))
        # print(nums[pointer1])
        # print(nums[pointer2])
        minimumDiff = min(minimumDiff, (abs(nums[pointer1] - nums[pointer2])))
        pointer1 += 1
        pointer2 += 1

    return minimumDiff

nums = [90]
k = 1
# >>> 0

# nums = [9,4,1,7]
# nums = [1,4,7,9]
# k = 2
# >>> 2
# Explanation: There are six ways to pick score(s) of two students:
# - [9,4,1,7]. The difference between the highest and lowest score is 9 - 4 = 5.
# - [9,4,1,7]. The difference between the highest and lowest score is 9 - 1 = 8.
# - [9,4,1,7]. The difference between the highest and lowest score is 9 - 7 = 2.
# - [9,4,1,7]. The difference between the highest and lowest score is 4 - 1 = 3.
# - [9,4,1,7]. The difference between the highest and lowest score is 7 - 4 = 3.
# - [9,4,1,7]. The difference between the highest and lowest score is 7 - 1 = 6.

print(minimumDifference(nums, k))
