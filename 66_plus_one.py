
# Constraints:
    # 1 <= digits.length <= 100
    # 0 <= digits[i] <= 9
    # digits does not contain any leading 0's.


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digitString = ""
        digitList = []
        for number in digits:
            digitString += str(number)

        digitString = int(digitString) + 1

        for val in str(digitString):
            digitList.append(int(val))

        return digitList

digits = [1,2,3]
# >>> [1,2,4]

# digits = [4,3,2,1]
# >>> [4,3,2,2]

# digits = [9]
# >>> [1,0]


sol = Solution()
sol.plusOne(digits)
