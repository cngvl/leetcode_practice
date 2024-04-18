# Constraints:
    # 1 <= flowerbed.length <= 2 * 104
    # flowerbed[i] is 0 or 1.
    # There are no two adjacent flowers in flowerbed.
    # 0 <= n <= flowerbed.length

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        pass

sol = Solution()
flowerbed = [1,0,0,0,1]
n = 1
sol.canPlaceFlowers(flowerbed, n)
# >>> true

# flowerbed = [1,0,0,0,1]
# n = 2
# sol.canPlaceFlowers(flowerbed, n)
# >>> false

# flowerbed = [0,0]
# n = 1
# sol.canPlaceFlowers(flowerbed, n)
# >>> true

# flowerbed = [0]
# n = 1
# sol.canPlaceFlowers(flowerbed, n)
# >>> true
