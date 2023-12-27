class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        for val in range(0,len(x)):
            print(x[val])
            # xCheck = x[val]
            # xInverseCheck = x[~val]
            if x[val] != x[~val]:
                return False

        return True

# x = 121
# >>> true

# x = -121
# >>> false

# x = 10
# >>> false

x = 123456787654321
# >>> true

sol = Solution()
sol.isPalindrome(x)
