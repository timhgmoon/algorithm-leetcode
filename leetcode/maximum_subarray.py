# def maxSubArray(nums):
#   #O(n^2)
#   max = float('-inf')

#   if len(nums) == 1:
#     return nums[0]

#   for i in range(len(nums)):
#     j = i + 1
#     sum = 0
#     for j in range(i, len(nums)):
#       sum += nums[j]
#       if(max < sum):
#         max = sum

#   return max

def maxSubArray(nums):
  currentSubarray = nums[0]
  maxSubarray = nums[0]

  for i in range(1, len(nums)):
    if currentSubarray < 0:
      currentSubarray = 0
    currentSubarray += nums[i]
    
    if maxSubarray < currentSubarray:
      maxSubarray = currentSubarray

  return maxSubarray
  
# nums = [-2,1,-3,4,-1,2,1,-5,4]
nums= [-2,-1,-5]

print(maxSubArray(nums))