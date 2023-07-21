class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        baseString = s[::]

        while l < r:

            left_char = s[l]
            right_char = s[r]

            # string ignoring the LAST letter
            x = s[l:r]

            # string ignoring the FIRST letter
            y = s[l+1:r+1]

            # If the string already is a palindrome and doesn't need any deletions
            if s[::] == s[::-1]:
                return True

            if s[l] == s[r]:
                l += 1
                r -= 1

            elif x == x[::-1] or y == y[::-1]:
                return True

            else:
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

# s = "deeee"
# >>> true

# s = "eeccccbebaeeabebccceea"
# >>> false

sol = Solution()
print(sol.validPalindrome(s))
