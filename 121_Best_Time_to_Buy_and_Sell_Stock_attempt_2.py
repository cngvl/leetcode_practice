# Constraints:
    # 1 <= prices.length <= 105
    # 0 <= prices[i] <= 104

# Sliding window type question
# Will need two pointers, leftPointer and rightPointer, which will never cross and only iterate through the array once
# Loop through the array while leftPointer is less than len(prices) - Might encounter rightPointer index errors
# profit is calced as rightPointer - leftPointer ( need to MAKE profit )
# if leftPointer is > rightPointer, iterate both += 1
# if rightPointer is < leftPointer:
    # leftPointer = rightPointer and rightPointer += 1
# if rightPointer is > leftPointer:
    # rightPointer += 1

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        leftPointer = 0
        rightPointer = 1
        profit = 0

        while rightPointer < len(prices):
            # if prices[leftPointer] > prices[rightPointer]:
            #     leftPointer += 1
            #     rightPointer += 1
            if prices[rightPointer] < prices[leftPointer]:
                leftPointer = rightPointer
                rightPointer += 1
            else:
                profit = max(profit, (prices[rightPointer] - prices[leftPointer]))
                rightPointer += 1

        print(profit)
        return profit



sol = Solution()
prices = [7,1,5,3,6,4]
# >>> 5
sol.maxProfit(prices)

prices = [7,6,4,3,1]
# >>> 0
sol.maxProfit(prices)
