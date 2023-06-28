# Constraints:
# 0 <= x <= 2^31 - 1
# You must not use any built-in exponent function or operator.
    # For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        min, max = 1, x

        while max >= min:
            mid = min + (max - min) // 2
            if mid == x // mid:
                return mid
            elif mid > x // mid:
                max = mid - 1
            else:
                min = mid + 1
        return max

x = 8
# >>> 2

# x = 4
# >>> 2

# x = 0
# >>> 0

# x = 1
# >>> 1

s = Solution()
print(s.mySqrt(x))
