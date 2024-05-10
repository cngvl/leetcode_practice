# Constraints:
    # 1 <= s.length <= 104
    # s consists of only English letters and spaces ' '.
    # There will be at least one word in s.

# Will attempt this question normally and then also try do some recursion solution
# Should ignore all the white space at the end of the string, but also stop at the first instance of white space
# Pointer solution starting from the right going leftwards
# I can do an initial 'loop' to find the point where the string starts?


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        returnInt = 0
        pointer = len(s) - 1
        # print('x')

        while s[pointer] == ' ':
            pointer -= 1

        while s[pointer] != ' ' and pointer >= 0:
            returnInt += 1
            pointer -= 1

        print(returnInt)


sol = Solution()
# s = "Hello World"
# sol.lengthOfLastWord(s)
# >>> 5

# s = "   fly me   to   the moon  "
# sol.lengthOfLastWord(s)
# >>> 4

# s = "luffy is still joyboy"
# sol.lengthOfLastWord(s)
# >>> 6

# Failed test case
# Fails because it starts off as 0, and then ticks down to -1, so the position of the pointer doesn't really change
# s = "a"
# sol.lengthOfLastWord(s)
# >>> 1

# Same issue as above, it would loop to 0 and then -1, making it look at the same position twice
s = "day"
sol.lengthOfLastWord(s)
# >>> 3
