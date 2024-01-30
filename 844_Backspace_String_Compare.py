import itertools

# Constraints:
    # 1 <= s.length, t.length <= 200
    # s and t only contain lowercase letters and '#' characters.

# Follow up: Can you solve it in O(n) time and O(1) space?

# Not sure how I can solve the followup question
# Basic answer is to make a stack for both and then compare at the end

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sStack = []
        tStack = []

        for letter in s:
            if letter != "#":
                sStack.append(letter)
            elif letter == "#" and len(sStack) > 0:
                sStack.pop()

        for letter in t:
            if letter != "#":
                tStack.append(letter)
            elif letter == "#" and len(tStack) > 0:
                tStack.pop()

        return sStack == tStack


    def backspaceCompare2(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x


        return all(x == y for x, y in itertools.izip_longest(F(S), F(T)))

# s = "ab#c"
# t = "ad#c"
# >>> true

# s = "ab##"
# t = "c#d#"
# >>> true

s = "a#c"
t = "b"
# >>> false

sol = Solution()
sol.backspaceCompare(s,t)
