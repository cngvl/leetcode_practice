# Constraints:
# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.

# Notes:
# can do some two pointer type shit
# iterate throguh the haystack and needle at same time
    # if the iteration breaks just move onto the next character for the haystack, but needle resets to 0
# default returns -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        letterPos = 0
        needleCounter = 0

        while letterPos < len(haystack):

            haystackLetter = haystack[letterPos]
            needleLetter = needle[needleCounter]

            if haystack[letterPos] == needle[needleCounter]:
                needleCounter += 1
            else:
                letterPos = letterPos - needleCounter
                needleCounter = 0

            if needleCounter == len(needle):
                # print(letterPos - needleCounter + 1)
                return letterPos - needleCounter + 1

            letterPos += 1

        return -1


# haystack = "sadbutsad"
# needle = "sad"
# >>> 0

haystack = "leetcode"
needle = "leeto"
# >>> -1

# haystack = "mississippi"
# needle = "issip"
# >>> 4

sol = Solution()
sol.strStr(haystack, needle)
