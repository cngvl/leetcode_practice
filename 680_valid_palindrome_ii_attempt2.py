class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        skippedChars = 0

        while l < r:

            left_char = s[l]
            right_char = s[r]

            x = s[l - 1:r]
            string = s[::]

            if s[l] == s[r]:
                l += 1
                r -= 1
            elif s[l] == s[r - 1]:
                l += 1
                r -= 2
                skippedChars += 1
            elif s[l + 1] == s[r]:
                l += 2
                r -= 1
                skippedChars += 1
            # elif x[::] == x[::-1]:
            #     l += 2
            #     r -= 2
            else:
                return False

        if skippedChars > 1:
            return False

        return True

# s = "aba"
# >>> true

# s = "abca"
# >>> true

# s = "abc"
# >>> false

# s = "abcdefghij0jihgfecba"
# >>> true

# s = "abcdefghij0jihg0fecba"
# >>> false

# s = "aabdeenddbaagbddeedbaa"
# >>> false

s = "lcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupucul"
# >>> true

s = "deeee"
# >>> true

s = "eeccccbebaeeabebccceea"
# >>> false

sol = Solution()
print(sol.validPalindrome(s))
