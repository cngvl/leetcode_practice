# Constraints:
    # 1 <= s.length <= 100
    # s contains only lower and upper case English letters.

# Initially thought I could use a stack to store all the letters seen and then pop off but this breaks if the first letter seen is capital
# Can be a two pointer question instead?
    # Can do a two pointer and then check if +1 or -1 is similar then remove them? and then reset back to 0
        # Can't pop strings because they're immutable
        # Maybe I do use a stack? - Topic suggests that stack is correcto
    # This might break if the resulting string is too small ( index error )
    # How can I make this loop multiple times?

class Solution:
    def makeGood(self, s: str) -> str:
        sStack = []
        pointer = 0

        while pointer < len(s):
            if (
                sStack and
                sStack[-1] != s[pointer] and
                sStack[-1].lower() == s[pointer].lower()
            ):
                sStack.pop()
            else:
                sStack.append(s[pointer])
            pointer += 1

        return "".join(sStack)

sol = Solution()
s = "leEeetcode"
# >>> "leetcode"
print(sol.makeGood(s))

s = "abBAcC"
# >>> ""
# print(sol.makeGood(s))

s = "s"
# >>> "s"
# print(sol.makeGood(s))

s = "Ss"
# >>> ""
# print(sol.makeGood(s))

s = "SsaBbA"
# >>> ""
# print(sol.makeGood(s))
