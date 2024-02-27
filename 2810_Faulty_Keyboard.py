# Constraints:
    # 1 <= s.length <= 100
    # s consists of lowercase English letters.
    # s[0] != 'i'


class Solution:
    def finalString(self, s: str) -> str:
        returnString = ''

        for letter in s:
            if letter == 'i':
                returnString = returnString[::-1]
            else:
                returnString += letter

        print(returnString)

s = "string"
# >>> "rtsng"

# s = "poiinter"
# >>> "ponter"

sol = Solution()
sol.finalString(s)
