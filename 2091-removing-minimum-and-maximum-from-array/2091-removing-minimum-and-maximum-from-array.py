class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        min_index = 0
        max_index = 0

        for i in range(n):
            if nums[i] > nums[max_index]:
                max_index = i
            if nums[i] < nums[min_index]:
                min_index = i
        
        left = max(min_index, max_index) + 1

        right = n - min(min_index, max_index)

        both = min(min_index, max_index) + 1 + \
               n - max(min_index, max_index)

        return min(left, right, both)