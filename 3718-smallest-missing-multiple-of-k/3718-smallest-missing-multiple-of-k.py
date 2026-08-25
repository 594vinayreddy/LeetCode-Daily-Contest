class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq = Counter(nums)

        i = 1
        
        while True:
            multiple = k * i

            if multiple not in freq:
                return multiple

            i += 1