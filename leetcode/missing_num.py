def missingNumber(nums):
  nums_len = len(nums)
  expected_total = (nums_len * (nums_len + 1)) // 2
  current_total = 0

  for i in range(nums_len):
    current_total += nums[i]

  return expected_total - current_total

def missingNumber2(nums):
  nums.sort()
  if nums[0] != 0:
    return 0
  for i in range(1, len(nums), 1):
    if nums[i] - nums[i-1] != 1:
      return nums[i] - 1
  
  return len(nums)


# nums = [3, 0, 1]
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(missingNumber2(nums))