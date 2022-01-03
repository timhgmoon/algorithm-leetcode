def twoSum(nums, target):
    new_dict = {}
    for i in range(len(nums)):
        if nums[i] in new_dict:
            return [new_dict[nums[i]], i]
        else:
            new_dict[target-nums[i]] = i
            
        

        # i = 0
        # solution_list = []
        # while(i < len(nums)):
        #     j = i + 1
        #     while(j < len(nums)):
        #         if(nums[i] + nums[j] == target):
        #             solution_list.append(i)
        #             solution_list.append(j)
        #             return solution_list
        #         j += 1
        #     i += 1
        # return solution_list

print(twoSum([3,2,4], 6))