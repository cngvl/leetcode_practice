# Constraints:
    # 0 <= nums.length <= 20
    # -231 <= nums[i] <= 231 - 1
    # All the values of nums are unique.
    # nums is sorted in ascending order.

# Is this some form of a staack question?
    # might just be some standard iterative question
    # "All the values of nums are unique." - need to keep this in mind
    # Not sure how I'm going to be including the "->"
        # Probably some interpolation? "{val1} -> {val2}"

# Loop through all the values of nums
    # If stack is empty append first num
    # if stack is not empty and num is +1 of stack[-1], append new num
    # if stack is not empty AND num is >+1 of stack[-1]
        # stack[0] and stack[-1] gets appended to returnList

    # once finished iterating, if stack is filled, add to returnList

class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        returnList = []
        stack = []

        for num in nums:
            if len(stack) == 0:
                stack.append(num)
            elif num == stack[-1] + 1:
                stack.append(num)
            elif len(stack) != 1:
                returnList.append(f"{stack[0]}->{stack[-1]}")
                stack.clear()
                stack.append(num)
            else:
                returnList.append(f"{stack[0]}")
                stack.clear()
                stack.append(num)


        if len(stack) == 1:
            returnList.append(f"{stack[0]}")
        else:
            returnList.append(f"{stack[0]}->{stack[-1]}")

        # print(returnList)
        return returnList

nums = [0,1,2,4,5,7]
# >>> ["0->2","4->5","7"]

# nums = [0,2,3,4,6,8,9]
# >>> ["0","2->4","6","8->9"]

sol = Solution()
sol.summaryRanges(nums)
