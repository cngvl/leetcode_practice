# Constraints:
    # 1 <= flowerbed.length <= 2 * 104
    # flowerbed[i] is 0 or 1.
    # There are no two adjacent flowers in flowerbed.
    # 0 <= n <= flowerbed.length

# Second attempt at this question and thought about it over a bit before sitting down to code the solution
# First attempt tried to turn it into a string? and then do some changes there but was unsuccessful
    # also don't remember what the solution is
# Maybe a TwoPointer technique?
    # Need to consider when len(flowerbed) == 1
    # Not sure if I need to mutate anything
    # Iterate through flowerbed with adjacent pointers
    # if two consecutive 0's, leftPointer changes the 0 to a 1, and then iterate both up two indexes
        # - Don't need to change the flowerbed input itself, just needs to return bool val
        # Doesn't work for flowerbed = [0,0,0] with n = 2

# Doesn't work when flowerbed [1,0,0]
    # having THREE pointers sounds a bit silly innit

# Can I use a stack for this question?
    # iterate through the flowerbed,
        # if 1, skip this iteration and next? - is this even possible
        # if 0, - this doesn't look like it'll work
            # would require three consecutive 0's to make it work?
        # Might be able to make this work if I reconsider the logic of this

# Maybe do some counter type shit?
# initialise a variable at 0
# iterate through flowerbed
    # if 1, variable -= 1
    # if 0, variable += 1
# - This only works retroactively? - I can't see what's infront of the pointer iterating through the flowerbed
    # if 0 and var >= 2, n -= 1


# Watched the neetcode solution
    # Used three pointers
    # Modified the input flowerbed array to have one extra 0 at the start and end to make sure there's enough space for the three pointers
    # Dogshit question


class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        flowerCounter = 0

        print(f'flowerbed = {flowerbed}')

        for flowerPos in range(len(flowerbed)):

            if flowerbed[flowerPos] == 1:
                flowerCounter -= 1
            elif flowerbed[flowerPos] == 0:
                flowerCounter += 1

            if flowerbed[flowerPos] == 0 and flowerCounter == 1:
                flowerbed[flowerPos] = 1
                flowerCounter = -1
                n -= 1

            # print('x')

        # if flowerCounter > 0:
        #     n -= 1

        # print(f'flowerCounter = {flowerCounter}')
        print(f'flowerbed = {flowerbed}')
        print(f'n = {n}')
        print(n <= 0)

    def canPlaceFlowersNeetCode(self, flowerbed: list[int], n: int) -> bool:
        f = [0] + flowerbed + [0]

        for i in range(1, len(f) - 1):
            if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
                f[i] = 1
                n -= 1

        return n <= 0

sol = Solution()
# flowerbed = [1,0,0,0,1]
# n = 1
# sol.canPlaceFlowers(flowerbed, n)
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

# flowerbed = [0,0,0]
# n = 2
# sol.canPlaceFlowers(flowerbed, n)
# >>> true

# Failed this test case
flowerbed = [1,0,0,0,0,1]
n = 2
sol.canPlaceFlowers(flowerbed, n)
# >>> false
