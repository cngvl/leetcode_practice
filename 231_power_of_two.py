# Constraints:
    # -231 <= n <= 231 - 1

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True

        while n > 2:
            n = n / 2

        return True if n == 2 else False
# n = 1
# >>> true

n = 16
# >>> true

# n = 3
# >>> false



sol = Solution()
sol.isPowerOfTwo(n)
