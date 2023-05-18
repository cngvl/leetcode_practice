def findDisappearedNumbers(nums):
    # Can sort the array of elements
    # Loop? through the array, for its range - not looping through the array itself???
        #  If the num is not in the array, push it to an answer array

    # Another option is to make a new array with a complete range, pop out every element (in the range array) that is contained in both
    # min(nums)
    # max(nums)
    nums_range = range(1, len(nums) + 1)
    ans_array = []
    for number in nums_range:
        # print(number)
        # print(number in nums)
        if number not in nums:
            # print(number)
            ans_array.append(number)

    # cheater
    # if len(ans_array) == 0:
    #     ans_array.append(max(nums) + 1)
    return ans_array

nums = [4,3,2,7,8,2,3,1]
# >>> [5,6]

# nums = [1,1]
# >>> [2]

# nums = [1,2,3]
# >>> []

# nums = [2,2]
# >>> [1]

# nums = [1, 2]
# >>> []

# nums = [3, 4]
# >>> [2] ??? or [1, 2]

print(findDisappearedNumbers(nums))
