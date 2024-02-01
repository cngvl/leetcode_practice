# Constraints:
# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100
    # Does this even change anything in terms of logic?

# Two pointer?
    # Does this result in a n2 solution?

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = []

        leftPointer = 0
        rightPointer = 1
        while leftPointer < len(temperatures):
            while rightPointer < len(temperatures):
                leftPointerCheck = temperatures[leftPointer]
                rightPointerCheck = temperatures[rightPointer]
                ifCheck = temperatures[leftPointer] < temperatures[rightPointer]
                elifCheck = (rightPointer == len(temperatures))
                if temperatures[leftPointer] < temperatures[rightPointer]:
                    answer.append(rightPointer - leftPointer)
                    break
                elif rightPointer == len(temperatures) - 1:
                    answer.append(0)
                    break
                else:
                    rightPointer += 1
                    # rightPointer

            leftPointer += 1
            rightPointer = leftPointer + 1
        # for day in temperatures:
        # while
        answer.append(0)

        print(answer)


# temperatures = [73,74,75,71,69,72,76,73]
# >>>          [01,01,04,02,01,01,00,00]

# temperatures = [30,40,50,60]
# >>> [1,1,1,0]

# temperatures = [30,60,90]
# >>> [1,1,0]

temperatures = [89,62,70,58,47,47,46,76,100,70]
# >>>          [08,01,05,04,03,02,01,01,000,00]

temperatures = [73,74,75,71,69,72,76,73]
# >>>          [01,01,04,02,01,01,00,00]
#              [01,01,04,02,01,01,00]


sol = Solution()
sol.dailyTemperatures(temperatures)
