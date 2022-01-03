import operator
import functools
def productExceptSelf(nums):
  # left = []
  # right = nums.copy()
  # right.pop()
  # right.append(1)

  # answer = []

  # left.append(1)
  
  # for i in range(1, len(nums)):
  #   left.append(nums[i - 1] * left[i - 1])

  # for i in range(len(nums) - 2, -1, -1):
  #   right[i] = nums[i+1] * right[i + 1]
  
  # for i in range(len(nums)):
  #   answer.append(left[i] * right[i])

  # return answer
  p = 1
  n = len(nums)
  output = []
  for i in range(0,n):
    output.append(p)
    p = p * nums[i]
  p = 1
  for i in range(n-1,-1,-1):
    output[i] = output[i] * p
    p = p * nums[i]
  return output

num = [1,2,3,4]
print(productExceptSelf(num))
# print(functools.reduce(operator.mul, [1,2,3,4]))

