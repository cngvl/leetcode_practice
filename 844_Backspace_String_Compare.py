# Constraints:
    # 1 <= s.length, t.length <= 200
    # s and t only contain lowercase letters and '#' characters.

# Follow up: Can you solve it in O(n) time and O(1) space?

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        pass

sol = Solution()
sol.backspaceCompare(s,t)

s = "ab#c"
t = "ad#c"
# >>> true

# s = "ab##"
# t = "c#d#"
# >>> true

# s = "a#c"
# t = "b"
# >>> false
