class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Case 1: k == 1
        if k == 1:
            freq = {}

            for num in nums:
                freq[num] = freq.get(num, 0) + 1

            ans = -1
            for num in freq:
                if freq[num] == 1:
                    ans = max(ans, num)

            return ans

        # Case 2: k == n
        if k == n:
            return max(nums)

        # Case 3: 1 < k < n
        # Only the first and last elements can occur
        # in exactly one subarray.

        first = nums[0]
        last = nums[-1]

        # Check if first occurs only once
        if nums.count(first) == 1:
            ans = first
        else:
            ans = -1

        # Check if last occurs only once
        if nums.count(last) == 1:
            ans = max(ans, last)

        return ans