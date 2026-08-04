class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        missing_nums = []

        nums.sort()
        
        for i in range(0, n - 1):
            if nums[i + 1] - 1 != nums[i]:
                for i in range(nums[i] + 1, nums[i + 1]):
                    missing_nums.append(i)
        
        return missing_nums
