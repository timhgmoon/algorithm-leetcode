# 136. Single Number

# Time Complexity: O(n) Space Complexity: O(n)
def singleNumber(nums):
    duplicate_nums = {}

    for i in range(len(nums)):
        cur_num = nums[i]
        if cur_num in duplicate_nums:
            duplicate_nums[cur_num] += 1
        else:
            duplicate_nums[cur_num] = 1

    for key in duplicate_nums:
        if duplicate_nums[key] == 1:
            return key
# Optimized using sort and comparing two numbers next to each other
# Time Complexity: O(n) Space Complexity: O(1)


def singleNumber2(nums):
    nums.sort()
    for i in range(0, len(nums) - 1, 2):
        if nums[i] != nums[i+1]:
            return nums[i]
    return nums[len(nums)-1]


# nums = [2,2,1]
nums = [4, 1, 2, 1, 2]

print(singleNumber2(nums))
