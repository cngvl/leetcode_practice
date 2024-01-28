# Constraints:
# 1 <= n <= 231 - 1

# How to avoid infinite loops (e.g. n = 11)
    # can do a check to see if the before and after values are different

# if n != 1
# Need to convert n to string
# Split the string
# For each value in the string, square it and then add to some variable
#

class Solution:
    def isHappy(self, n: int) -> bool:
        previousValues = []
        currentSum = 0
        while n != 1:
            stringN = str(n)
            currentSum = 0
            for num in stringN:
                currentSum += int(num) ** 2

            if currentSum not in previousValues:
                previousValues.append(currentSum)
            else:
                # print('False')
                return False

            n = currentSum


        # print('True')
        return True

# n = 19
# >>> true

# n = 2
# >>> false

n = 11
# >>> false

sol = Solution()
sol.isHappy(n)
