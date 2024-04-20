# Constraints:
    # 1 <= arr.length <= 104
    # 1 <= arr[i] <= 105

# Doing an easy question because I'm lazy
# I think I've seen a video on this question before?
    # First attempt at this solution used a left to right iteration while slicing off the 0th index and then checking max in the original array
    # Works but I think it can be optimised - not sure what the time complex for slicing operation is

# Can use a pointer going from right to left
# can do for loop but how do I make the -1 index == -1?


class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        currMax = -1

        for numPos in range(len(arr) -1, -1, -1):
            # print(num)
            if currMax == -1:
                temp = arr[numPos]
                arr[numPos] = currMax
                currMax = max(temp,-1)
            # elif currMax > arr[numPos]:
            #     arr[numPos] = currMax
            # else:
            #     currMax = arr[numPos]
            else:
                temp = arr[numPos]
                arr[numPos] = currMax
                currMax = max(currMax, temp)
                print('x')

        print(arr)





sol = Solution()
arr = [17,18,5,4,6,1]
sol.replaceElements(arr)
# >>> [18,6,6,6,1,-1]

arr = [400]
sol.replaceElements(arr)
# >>> [-1]
