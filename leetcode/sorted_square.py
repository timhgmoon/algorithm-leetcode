# Time Complexity: O(n) Space Complexity: O(n)
def sortedSquares(nums):
  squared_nums = []
  for num in nums:
    squared_nums.append(num**2)

  squared_nums.sort()
  return squared_nums

nums = [-7, -3, 2, 3, 11]

print(sortedSquares(nums))

