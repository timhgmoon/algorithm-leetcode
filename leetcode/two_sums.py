def twoSum(nums, target):
    new_dict = {}
    for i in range(len(nums)):
        if nums[i] in new_dict:
            return [new_dict[nums[i]], i]
        else:
            new_dict[target-nums[i]] = i
            

    for i in range(len(nums)):
        for j in range((i+1), len(nums)):
            if(target - nums[i] == nums[j]):
                return [i,j]
print(twoSum([3,2,4], 6))