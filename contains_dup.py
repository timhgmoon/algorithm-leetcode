#problem having, test solution size is too big (need better than O(n^2)

# def containsDuplicate(nums):
#   for i in range(len(nums)):
#     j = i + 1
#     while(j < len(nums)):
#       if nums[i] == nums[j]:
#         return True
#       j += 1
#   return False

# def containsDuplicate(nums):
#   nums_set = set(nums)
#   if(len(nums) == len(nums_set)):
#     return False
#   return True

# nums_set = set()

def containsDuplicate(nums):
  nums_set = set()
  nums_list = []
  for i in range(len(nums)):
    nums_set.add(nums[i])
    nums_list.append(nums[i])
    if(len(nums_set) != len(nums_list)):
      return nums[i]
  return 

print(containsDuplicate([2,5,3,4, 5]))

