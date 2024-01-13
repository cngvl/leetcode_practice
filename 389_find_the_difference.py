# Constraints:
# 0 <= s.length <= 1000
# t.length == s.length + 1
# s and t consist of lowercase English letters.

# Need to len(t) is always longer than len(s) - always by 1?
# can't iterate throuhg both at the same time because not sure where the difference in the two strings will be?
    # wrong assumption?
# need to make sure I account for empty strings
# misinterepted the question
    # should not have assumed the letters would be placed in the same order
# need to count the occurance of the letters themselves


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) == 0:
            return t

        sDict = {}
        tDict = {}

        for letterPos in range(0, len(s)):
            # ifCheck = s[letterPos] not in sDict
            if s[letterPos] not in sDict:
                sDict[s[letterPos]] = 1
            else:
                sDict[s[letterPos]] += 1

        print(sDict)

        for letterPos in range(0, len(t)):
            # ifCheck = t[letterPos] not in tDict
            if t[letterPos] not in tDict:
                tDict[t[letterPos]] = 1
            else:
                tDict[t[letterPos]] += 1

        print(tDict)

        for key in tDict:
            if key not in sDict or tDict[key] != sDict[key]:
                return key

# s = "abcd"
# t = "abcde"
# >>> "e"

s = ""
t = "y"
# >>> "y"

# s = "abcdefghijklmnopqrstuvwxyz"
# t = "abcdefghijklmnopqrstuvwxyza"
# >>> "a"

# s = "abcdefghijklmnopqrstuvwxyz"
# t = "abcdefghijklmanopqrstuvwxyz"
# >>> "a"

sol = Solution()
sol.findTheDifference(s, t)
