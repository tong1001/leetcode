'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero. Note:The solution set must not contain duplicate triplets.
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。 注意：答案中不可以包含重复的三元组。
例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为： [ [-1, 0, 1], [-1, -1, 2] ]
'''

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        tupleList = []
        nums.sort()
        index_greater_than_zero = self.indexGreaterThanZero(nums)
        listLen = len(nums)
        for i in range(index_greater_than_zero):
            for j in range(index_greater_than_zero,listLen,1):
                temp = 0 - nums[i] + nums[j]
                if temp in nums and [nums[i], nums[j], temp] not in tupleList:
                    tupleList.append([nums[i], nums[j], temp])
                else:
                    continue
        return tupleList
    
    def indexGreaterThanZero(self,nums):
        for index, value in enumerate(nums):
            if value>=0:
                return index
            else:
                continue
        return 0
