# Constraints:
# 1 <= s.length <= 105
# s consists of lowercase English letters and stars *.
# The operation above can be performed on s.

# Note:
# The input will be generated such that the operation is always possible.
    # Wont be given any stars BEFORE any chars have been included in the list?
# It can be shown that the resulting string will always be unique.

class Solution:
    def removeStars(self, s: str) -> str:
        # print(s)

        letterStack = []
        for char in s:
            if char == "*":
                letterStack.pop()
            else:
                letterStack.append(char)

        print(''.join(letterStack))
        print(letterStack)


s = "leet**cod*e"
# >>> "lecoe"

# s = "erase*****"
# >>> ""

sol = Solution()
sol.removeStars(s)
