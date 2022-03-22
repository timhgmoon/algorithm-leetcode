def rotate(nums, k):
  """
  Do not return anything, modify nums in-place instead.
  """
  for i in range(len(nums), len(nums)-k, -1):
    nums.insert(0, nums.pop())

nums = [1,2,3,4,5,6,7]
k = 3
rotate(nums, k)
"""
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""