# Constraints:
# n == nums.length
    # How does 'n' relate to anything?
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.

# Notes
    # Empty arrays?
    # Arrays with only one or two of the listed values


# Two pointer?
    # compare the two and if the latter pointer is greater than the former then swap the two,
    # this only compares the one directly, doesn't check the whole array if there are any smaller values

# Could also do something that is almost? n2 time complex
# Trying this first

# I wonder if I can do a counting method with some hashmap and then reproduce the original array

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        # """
        # Do not return anything, modify nums in-place instead.
        # """
        # print(nums)

        leftPointer = 0
        while leftPointer + 1 < len(nums):
            leftValue = nums[leftPointer]

            rightPointer = leftPointer + 1 # Can cause out of range issue
            lowestSeen = nums[rightPointer]
            lowestSeenIndex = rightPointer

            while rightPointer < len(nums):
                rightValue = nums[rightPointer]

                if rightValue < lowestSeen:
                    lowestSeen = nums[rightPointer]
                    lowestSeenIndex = rightPointer

                rightPointer += 1


            if lowestSeen < leftValue:
                nums[leftPointer] = lowestSeen
                nums[lowestSeenIndex] = leftValue

            leftPointer += 1


nums = [2,0,2,1,1,0]
# >>> [0,0,1,1,2,2]

# nums = [2,0,1]
# >>> [0,1,2]

sol = Solution()
sol.sortColors(nums)
