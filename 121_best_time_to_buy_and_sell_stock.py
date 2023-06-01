# Need to loop through the array
# Do not do any brute force methods
# Can only take elements DOWNSTREAM
# Should I try do some subarray things? - don't see how I can do this with a hashmap
# Sliding window question - the two pointers should never cross
# I SHOULDN'T do abs() because that removes the potential loss from selling the stock
# Not a for loop, should stop when one of the pointers reach the end
# Sliding windows dont necessarily increase by 1
# Is it a big if..elif..else conditional?


def maxProfit(prices):
    # print(prices)
    leftPointer = 0
    rightPointer = 1
    storedMax = 0
    # for day in prices:
    while rightPointer < len(prices):
        # print(day)
        tempMax = prices[rightPointer] - prices[leftPointer]
        if tempMax > storedMax:
            storedMax = tempMax
            # rightPointer += 1

        if prices[rightPointer] < prices[leftPointer]:
            leftPointer = rightPointer
            # rightPointer += 1

        rightPointer += 1
        # print(prices[rightPointer])
        # print(prices[leftPointer])

        # rightPointer += 1
        # leftPointer += 1
    return storedMax



# prices = [7,1,5,3,6,4]
# >>> 5

prices = [7,6,4,3,1]
# >>> 0

print(maxProfit(prices))
