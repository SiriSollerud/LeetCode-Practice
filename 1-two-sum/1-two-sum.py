class Solution(object):
    def twoSum(self, nums, target):
        # find indices of 2 numbers in nums that add up to target
        indexes = []
        for i in range(len(nums)):
            x = target - nums[i]
            if (x) in nums:
                if (len(nums) == 2) and (nums[0] + nums[1] == target):
                    indexes = [0, 1]
                    return indexes
                if nums[i] * 2 == target:
                    if nums.count(nums[i]) > 1:
                        indexes.append(i)
                else:
                    indexes.append(i)
        return indexes


        