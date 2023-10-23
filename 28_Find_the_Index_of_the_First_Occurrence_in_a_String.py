# Constraints:
# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        print(haystack, needle)

haystack = "sadbutsad"
needle = "sad"
# >>> 0

# haystack = "leetcode"
# needle = "leeto"
# >>> -1

sol = Solution()
sol.strStr(haystack, needle)
