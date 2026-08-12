class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq_dict = defaultdict(int)
        i = 0
        ans = 0

        for j in range(len(nums)):
            freq_dict[nums[j]] += 1
            while freq_dict[nums[j]] > k:
                freq_dict[nums[i]] -= 1
                i += 1
            ans = max(ans, j - i + 1)

        return ans