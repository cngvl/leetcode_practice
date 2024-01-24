# Constraints:
    # 0 <= num <= 231 - 1

# Follow up: Could you do it without any loop/recursion in O(1) runtime?
    # Is there some trick to this?

class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            count = 0
            num = str(num)
            for char in num:
                count += int(char)

            num = count

        return num

    def addDigits2(self, num: int) -> int:
        if num % 9 == 0 and num > 0:
            return 9

        elif num > 9:
            num = num % 9

        return num


num = 38
# >>> 2

# num = 0
# >>> 0

sol = Solution()
sol.addDigits(num)
