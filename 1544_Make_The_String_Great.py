# Constraints:
    # 1 <= s.length <= 100
    # s contains only lower and upper case English letters.

class Solution:
    def makeGood(self, s: str) -> str:
        pass

sol = Solution()
s = "leEeetcode"
# >>> "leetcode"
sol.makeGood(s)

s = "abBAcC"
# >>> ""
sol.makeGood(s)

s = "s"
# >>> "s"
sol.makeGood(s)
