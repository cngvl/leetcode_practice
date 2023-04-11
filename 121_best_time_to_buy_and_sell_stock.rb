# @param {Integer[]} prices
# @return {Integer}
def max_profit(prices)
  l = 0
  r = 1
  max_profit = 0
  # right to keep going through the array
  # left should be the lowest value
  # compare right vs. left
  # if no profit yet, store as max_profit
  # if profit > max_profit, max_profit = profit
  while r < prices.length do
    if prices[l] < prices[r]
      profit = prices[r] - prices[l]
      max_profit = profit if profit > max_profit
    elsif prices[l] > prices[r]
      l = r
    end
    r += 1
  end
  max_profit
end
