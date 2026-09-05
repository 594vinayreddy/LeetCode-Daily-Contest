class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        max_array = [float("inf")] * n
        max_array[0] = nums[0]

        min_array = [0] * n
        min_array[n - 1] = nums[n - 1]

        for i in range(1, n):
            max_array[i] = max(max_array[i - 1], nums[i])

        for j in range(n - 2, -1, -1):
            min_array[j] = min(min_array[j + 1], nums[j])

        for i in range(n):
            if max_array[i] - min_array[i] <= k:
                return i

        return -1