# Constraints:
    # 1 <= left <= right <= 104

# Need to iterate through all the numbers between L and R values
# For each of those values, need to convert it to string? and then divide the value up by each digit
# If nonzero value and passes % check, add to returnlist

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        returnList = []
        for number in range(left, right + 1):
            numberString = str(number)
            appendCheck = True
            for digit in numberString:
                if digit == '0' or number % int(digit) != 0:
                    appendCheck = False
            if appendCheck:
                returnList.append(number)

        print(returnList)


left = 1
right = 22
# >>> [1,2,3,4,5,6,7,8,9,11,12,15,22]

# left = 47
# right = 85
# >>> [48,55,66,77]

# left = 9
# right = 13
# >>> [9,11,12]

sol = Solution()
sol.selfDividingNumbers(left, right)
