'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.You may assume that each input would have exactly one solution, and you may not use the same element twice.
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

Example: Given nums = [2, 7, 11, 15], target = 9, Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in nums:
            if (target - i) in nums and (target - i) == i:
                try:
                    targetSubtractI = nums.index(target-i, nums.index(i)+1, len(nums))
                    return [nums.index(i), targetSubtractI]
                except:
                    continue
            if (target - i) in nums and (target - i) != i:
                return [nums.index(i), nums.index(target-i)]
