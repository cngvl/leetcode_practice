# Constraints:
# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        print(temperatures)

temperatures = [73,74,75,71,69,72,76,73]
# >>> [1,1,4,2,1,1,0,0]

# temperatures = [30,40,50,60]
# >>> [1,1,1,0]

# temperatures = [30,60,90]
# >>> [1,1,0]



sol = Solution()
sol.dailyTemperatures(temperatures)
