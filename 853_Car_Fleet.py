# Constraints:
    # n == position.length == speed.length
    # 1 <= n <= 105
    # 0 < target <= 106
    # 0 <= position[i] < target
    # All the values of position are unique.
    # 0 < speed[i] <= 106

# position and speed arrays of same length
# Can iterate through both at the same time and then add speed[i] to position[i]
# Stop looping once theres a pos[i] val that is >= target?
# maybe keep a max speed tracker to figure out whnen to stop looping
# Can do a final loop to check the number of fleets? - see how many vals are the same?¿
# Gets weird because there's also the no overtaking clause - can adjust the speed value?
# Question is listed as a Monotonic stack question - rock smashin type shit

# Might be a good idea to sort the position of the cars first and then somehow match them with their speeds?
    # Probably some HashMap for this

class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        maxDistance = 0
        matchedCars = {}

        for index in range(len(position)):
            matchedCars[position[index]] = speed[index]

        print(matchedCars)
        position.sort()
        position.reverse()

        for index in range(len(position)):
            # Can add a check to see if the previous/next val is than or equal to the curr val. If true, add spd ( but not too much to exceed the prev car )
            position[index] += matchedCars[position[index]]
            maxDistance = max(position[index], maxDistance)

        print(maxDistance)
        print(position)

sol = Solution()
target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
sol.carFleet(target, position, speed)
# >>> 3
# 10 08 0 5 3
# 12 12 1 6 6

# target = 10
# position = [3]
# speed = [3]
# sol.carFleet(target, position, speed)
# >>> 1

# target = 100
# position = [0,2,4]
# speed = [4,2,1]
# sol.carFleet(target, position, speed)
# >>> 1
# 0 2 4
# 4 4 5
# 6 6 6
