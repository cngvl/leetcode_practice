# Constraints:
# -231 <= n <= 231 - 1

# Follow up: Could you solve it without loops/recursion?

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # pass
        if n < 0:
            return False

        while n > 3:
            n = n / 3

        if n == 3 or n == 1:
            print('True')
            return True
        else:
            print('False')
            return False

n = 27
# >>> true

# n = 0
# >>> false

n = 28
# >>> false

# n = -1
# >>> false

sol = Solution()
sol.isPowerOfThree(n)
