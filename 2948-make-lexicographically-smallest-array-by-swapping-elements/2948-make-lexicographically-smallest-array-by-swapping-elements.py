class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        n = len(nums)

        idx = sorted(range(n), key=lambda i: nums[i])

        result = [0] * n
        i = 0
        while i < n:
            j = i
            group = [idx[i]]

            while j + 1 < n and nums[idx[j + 1]] - nums[idx[j]] <= limit:
                j += 1
                group.append(idx[j])

            sorted_indices = sorted(group)

            for k, pos in enumerate(sorted_indices):
                result[pos] = nums[idx[i + k]]

            i = j + 1
        return result
