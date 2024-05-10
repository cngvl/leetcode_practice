# Constraints:
    # 1 <= s.length <= 104
    # s consists of only English letters and spaces ' '.
    # There will be at least one word in s.

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

sol = Solution()
s = "Hello World"
sol.lengthOfLastWord(s)
# >>> 5

# s = "   fly me   to   the moon  "
# sol.lengthOfLastWord(s)
# >>> 4

# s = "luffy is still joyboy"
# sol.lengthOfLastWord(s)
# >>> 6
