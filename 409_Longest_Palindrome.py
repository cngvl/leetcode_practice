# Constraints:
    # 1 <= s.length <= 2000
    # s consists of lowercase and/or uppercase English letters only.

# the question is what is the longest palindrome that can be BUILT using the input characters
# needs to be case sensitive a != A
# Can do some sort of counting?
    # needs to have multiples of two + a middle char?

class Solution:
    def longestPalindrome(self, s: str) -> int:
        charHash = {}
        returnInt = 0
        pivitBool = False

        for char in s:
            if char in charHash:
                charHash[char] += 1
            else:
                charHash[char] = 1

        print(charHash)

        for char in charHash:
            if charHash[char] >= 2:
                # pass
                returnInt += (charHash[char] // 2) * 2
                charHash[char] = charHash[char] % 2
            if pivitBool == False and charHash[char] >= 1:
                returnInt += 1
                pivitBool = True

        print(charHash)
        print(returnInt)

        return returnInt
s = "abccccdd"
# >>> 7

s = "a"
# >>> 1

s = "aa"
# >>> 2

s = "aab"
# >>> 3

# s = "abc"
# >>> 2

s = "ccc"
# >>> 3

sol = Solution()
sol.longestPalindrome(s)
