def maxProfit(prices):
  difference = 0
  first = prices[0]

  for i in range(1, len(prices)):
    if((prices[i] - first) > difference):
      difference = prices[i] - first
    else:
      if(prices[i] < first):
        first = prices[i]
  
  return difference
  
print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([1,2]))

 # O(n^2)
  # difference = 0
  # for i in range(len(prices)):
  #   for j in range(i + 1, len(prices)):
  #     if(prices[j] > prices[i]):
  #       if((prices[j] - prices[i]) > difference):
  #         difference = prices[j] - prices[i]
  # return difference
