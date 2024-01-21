# Constraints:
    # -231 <= n <= 231 - 1
    # "positive integer whose prime factors are limited to 2, 3, and 5."

# Rough math problem
# n needs to % 2 3 and 5, but NOT any other vals
# use % or //
# Can't JUST be those vals because it would break for n = 30

class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        for val in [2,3,5]:
            while n % val == 0 :
                n = n // val

        return n == 1


n = 6
# >>> true

# n = 1
# >>> true

# n = 8
# >>> true

# n = 14
# >>> false

# n = 15
# >>> true

# n = 16
# >>> false

sol = Solution()
sol.isUgly(n)
