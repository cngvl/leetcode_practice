# def pivotIndex(nums):
    # print('x')
    # Can find the target sum value by the total / 2 - doesn't work for 2 1 -1?
    # Will need to account for nums.length = 1
    # Run two loops, seperately?
        # One going left to right
        # Other going right to left
    # Loops continue until they hit the target value
    # Once they hit the target value, find the index they stopped at
    # Compare the two, if they match return the match value
    # If not, return -1
    # right_looper_total = 0
    # right_looper_history = [0]
    # for right_looper in nums:
    #     right_looper_total += right_looper
    #     right_looper_history.append(right_looper_total)
    #     # print(right_looper_total)

    # left_looper_total = 0
    # for left_looper in reversed(nums):
    #     left_looper_total += left_looper
    #     if left_looper_total in right_looper_history:
    #         print(nums.index(left_looper))
    #         return nums.index(left_looper)

    # return -1


nums = [1,7,3,6,5,6]
# >>> 3
# 1 8 11 17 22 28

# nums = [1,2,3]
# >>> -1

# nums = [2,1,-1]
# >>> 0


def pivotIndex(nums):
    # Alternative method is to loop through the array
    # At each step, calculate what is the sum of everything before and after the pointer, as two seperate sums
    # 0 .. pointer
    # pointer .. -1
    position = 0
    # can do a while condition - while position <= nums.length
    # for pointer in nums[0:3]:
        # print(pointer)
        # Everything to the left

        # Everything to the right
    for position in range(len(nums) + 1):
        # print(position)
        print('Left loop values:')
        left_sum = 0
        for i in nums[0:position]:
            print(i)
            left_sum += i

        # print('Left looping done')

        print('Right loop values:')
        right_sum = 0
        for j in nums[position:-1]:
            print(j)
            right_sum += j
        # print('Right looping done')

        # if left_sum == right_sum:
        #     print('THIS IS THE POSITION')
        #     print(position)
        print('*' * 20)
        print('ONE POSITION LOOP DONE')
        print('*' * 20)

# nums = [1,7,3,6,5,6]
# nums = [0,1,2,3,4,5]
pivotIndex(nums)
