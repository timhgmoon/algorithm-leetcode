#35 search insert position
def searchInsert(nums, target):
  low = 0
  high = len(nums) - 1
  
  while low <= high:
      mid = (high + low) // 2
      guess = nums[mid]
      if target == guess:
          return mid
      if target > guess:
          low = mid + 1
      else:
          high = mid - 1
  return low

# nums = [1,3,5,6]
nums = [1,3,4,6,8,10]
target = 5
print(searchInsert(nums, target))