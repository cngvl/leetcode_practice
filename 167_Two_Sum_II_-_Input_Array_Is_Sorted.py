# Constraints:
    # 2 <= numbers.length <= 3 * 104
    # -1000 <= numbers[i] <= 1000
    # numbers is sorted in non-decreasing order.
    # -1000 <= target <= 1000
    # The tests are generated such that there is exactly one solution.

# For sure a TwoPointer question
# Question specifies to use constant extra space - Two Pointers should be fine in this case
# I think I should initialise one of the pointers at the END of the array
    # while left is < right
    # rightPointer iterates until numbers[rightPointer] is less than target
    # This works because there is exactly one solution, the two pointers should never cross anyway with the while loop condition
    # The hard part is figuring out which pointer to iterate inwards
    # if rightPointer + leftPointer = target, return [leftPointer + 1, rightPointer + 1]
    # elif? rightPointer - target is > leftPointer, then rightPointer -= 1?

# Initial thought process worked for 11/23 test cases + the example ones
# Oversight was the use of negative values 🥲
#

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
       leftPointer = 0
       rightPointer = len(numbers) - 1

       while leftPointer < rightPointer:
            ifCheck = (numbers[leftPointer] + numbers[rightPointer] == target)
            elifCheck = (numbers[rightPointer] + numbers[leftPointer] >= target)
            # print('y')

            if ifCheck:
               print(f'{leftPointer + 1, rightPointer + 1}')
               return [leftPointer + 1, rightPointer + 1]
            elif elifCheck:
                rightPointer -= 1
            else:
                leftPointer += 1

            # print('x')

sol = Solution()
numbers = [2,7,11,15]
target = 9
sol.twoSum(numbers, target)
# >>> [1,2]

numbers = [2,3,4]
target = 6
sol.twoSum(numbers, target)
# >>> [1,3]

numbers = [-1,0]
target = -1
sol.twoSum(numbers, target)
# >>> [1,2]

numbers = [0,1,2,4,7,8,9]
target = 6
sol.twoSum(numbers, target)
# >>> [3,4]

numbers = [-1000,-1,0,1]
target = 1
sol.twoSum(numbers, target)
# >>> [3,4]
