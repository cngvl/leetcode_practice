# Notes
# Assume all input is in lower case and at least two characters long.

class Solution:
    def stutter(self, word:str) -> str:
        stutterCount = 0
        returnString = ''
        while stutterCount < 2:
            # maxPos = 1
            for letterPos in range(0,2):
                returnString += f'{word[letterPos]}'
            returnString += '... '
            stutterCount += 1

        returnString += f'{word}?'
        print(returnString)


sol = Solution()

word = "incredible"
sol.stutter(word)
# >>> "in... in... incredible?"

word = ("enthusiastic")
sol.stutter(word)
# >>> "en... en... enthusiastic?"

word = ("outstanding")
sol.stutter(word)
# >>> "ou... ou... outstanding?"

word = "so"
sol.stutter(word)
# >>> "so... so... so?"
