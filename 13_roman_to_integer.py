# Constraints:
# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].

class Solution:
    def romanToInt(self, s: str) -> int:
        convertedStack = []
        romanConvert = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        for inputLetter in s:
            convertedStack.append(romanConvert[inputLetter])

        for numberPos in range(1,len(convertedStack)):
            if convertedStack[numberPos] > convertedStack[numberPos - 1]:
                convertedStack[numberPos - 1] *= -1

        return sum(convertedStack)

s = "III"
# >>> 3

# s = "LVIII"
# >>> 58

# s = "MCMXCIV"
# >>> 1994

sol = Solution()
sol.romanToInt(s)
