# Constraints:
# 1 <= ransomNote.length, magazine.length <= 10^5
# ransomNote and magazine consist of lowercase English letters.

# I wonder if you can do some letter counting + hashMap solution

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sPointer = 0
        tPointer = 0

        if len(t) == 0 and len(t) > 0:
            return False

        if len(s) == 0:
            return True

        while tPointer < len(t):
            x = s[sPointer]
            y = t[tPointer]

            if sPointer == len(s):
                return True
            elif s[sPointer] == t[tPointer]:
                sPointer += 1
                tPointer += 1
            else:
                tPointer += 1

        return sPointer == len(s)



s = "abc"
t = "ahbgdc"
# >>> true

# s = "axc"
# t = "ahbgdc"
# >>> false

# s = "aa"
# t = "aab"
# >>> true

sol = Solution()
print(sol.canConstruct(s, t))
