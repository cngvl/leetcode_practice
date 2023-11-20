# Constraints:
# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100
    # Does this even change anything in terms of logic?

# Can do a loop that only looks at things downstream
    # Not sure if there's any cleaner options?

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = []
        # print(temperatures)

        for position in range(0,len(temperatures)):
            # print(position)
            currentTemp = temperatures[position]
            days_till_warmer = 0

            for downstreamPosition in range(position + 1, len(temperatures)):
                # print(downstreamPosition)
                ifCheck = temperatures[downstreamPosition] > currentTemp
                if temperatures[downstreamPosition] > currentTemp:
                    days_till_warmer = downstreamPosition - position
                    break

            answer.append(days_till_warmer)

        print(answer)

temperatures = [73,74,75,71,69,72,76,73]
# >>> [1,1,4,2,1,1,0,0]

# temperatures = [30,40,50,60]
# >>> [1,1,1,0]

# temperatures = [30,60,90]
# >>> [1,1,0]

sol = Solution()
sol.dailyTemperatures(temperatures)
