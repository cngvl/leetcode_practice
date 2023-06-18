# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        min, max = 1, n
        while max > min:
            pick = (min + max) // 2
            if guess(pick) == 1:
                min = pick + 1
            elif guess(pick) == -1:
                max = pick - 1
            else:
                return pick
