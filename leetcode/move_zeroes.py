# 283. Move Zeroes

#time complexity: O(n)
def moveZeroes(nums):
  """
  Do not return anything, modify nums in-place instead.
  """
  amount_to_remove = 0
  for num in nums:
    if num == 0:
      amount_to_remove += 1
  
  for i in range(amount_to_remove):
    nums.remove(0)
    nums.append(0)
  
nums = [0,1,0,3,12]
moveZeroes(nums)
print(nums)
