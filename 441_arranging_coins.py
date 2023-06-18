# Constraints:
# 1 <= n <= 2^31 - 1

# Need to make some sort of loop that increases by 1 each time, 1 + 2 + 3
# Can I use (first + last) / 2?
# Should do some while loop that compares the total number of squares with n
# Once n is < total, stop the loop?
# if n is at a specific value (1 3 6 10...) it fills a complete row
# Maybe a hash?

class Solution:
    def arrangeCoins(self, n: int) -> int:
        # print(n)
        totalSquares = 0
        rowNumber = 0
        squareHash = {}
        while n >= totalSquares:
            rowNumber += 1
            totalSquares += rowNumber
            squareHash[rowNumber] = totalSquares
            # print('*' * rowNumber)

        if n == squareHash[rowNumber]:
            return rowNumber
        else:
            return rowNumber - 1





# n = 5
# >>> 2

n = 8
# >>> 3

s = Solution()
print(s.arrangeCoins(n))
