# Constraints:
    # 1 <= s.length <= 105
    # s consists of English letters, digits, and dashes '-'.
    # 1 <= k <= 104

# Can work from the end to the front
    # Don't really need to flip but might make it easier

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        returnString = ''
        kCount = 0

        for char in s[::-1]:
            if char == '-':
                continue
            ifCheck = (kCount == k)
            if kCount == k:
                returnString += f'-{char.upper()}'
                kCount = 1
            else:
                returnString += char.upper()
                kCount += 1


        print(returnString[::-1])

# s = "5F3Z-2e-9-w"
# k = 4
# >>> "5F3Z-2E9W"

# s = "2-5g-3-J"
# k = 2
# >>> "2-5G-3J"

s = "2-5-g-3-J"
k = 1
# >>> "2-5-G-3-J"

sol = Solution()
sol.licenseKeyFormatting(s, k)
