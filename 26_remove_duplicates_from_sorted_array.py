# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:


# Initial thought was to make a hashmap and record all the numbers that have been seen when iterating over
    # Iterate through nums and then add unique values to hash
    # If a value is old, remove it
# Have a bit of a hint in knowing that this is a two-pointer question
    # If if I do a two pointer that reads through every value and checks the whole list for that value it becomes an O(n2) time complex value
    # list(dict.fromkeys(nums))

def removeDuplicates(nums):
    # print(nums)
    # len(list(dict.fromkeys(nums)))
    # timesLooped = 0
    seenLetters = {}
    for number in nums:
        # timesLooped += 1
        # if number in seenLetters:
        if number in seenLetters:
            print(f"{number} is found!")
            # del nums[number]
            nums.remove(number)
        else:
            seenLetters[number] = 1




# nums = [1,1,2]
# # >>> 2, nums = [1,2,_]

nums = [0,0,1,1,1,2,2,3,3,4]
# # >>> 5, nums = [0,1,2,3,4,_,_,_,_,_]

removeDuplicates(nums)
