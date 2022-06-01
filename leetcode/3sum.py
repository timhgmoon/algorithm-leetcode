class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        total = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums) -2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                current_sum = nums[left] + nums[right] + nums[i]
                if current_sum == target:
                    return target
                if abs(target - current_sum) < abs(target-total):
                    total = current_sum
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
        return total
