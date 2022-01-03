# def threeSum(nums): 
#   #brute force
#   answer = []

#   for i in range(len(nums)):
#     current_list = []
#     current_list.append(nums[i])
#     for j in range(i+1, len(nums)):
#       current_list.append(nums[j])
#       if len(current_list) % 3 == 0:
#         if sum(current_list) == 0:
#           answer.append(current_list.copy())
#         current_list.pop(1)
#         current_list.pop(1)
#   return answer

def threeSum(nums):
  nums.sort()
  ans = []
  for i in range(len(nums)):
    if(nums[i] > 0):
      break
    if(i == 0 or nums[i] != nums[i-1]):
      twoSum(nums, i, ans)
  return ans

def twoSum(nums, i , ans):
  lo, hi = i+1, len(nums) - 1
  while( lo < hi):
    sum = nums[i] + nums[lo] + nums[hi]
    if sum < 0:
      lo += 1
    elif sum > 0:
      hi -= 1
    else:
      ans.append([nums[i], nums[lo], nums[hi]])
      lo += 1
      hi -= 1
      while lo < hi and nums[lo] == nums[lo-1]:
        lo += 1

nums=[-1,0,1,2,-1,-4]
print(threeSum(nums))


