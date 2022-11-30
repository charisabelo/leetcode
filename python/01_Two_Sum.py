class Solution:
    def twoSum(self, nums, target):
        output = []
        found = {}

        for i in range(len(nums)):
            total = target - nums[i]
            if total in found:
                output = [found[total], i]
            else:
                found[nums[i]] = i

        return output
