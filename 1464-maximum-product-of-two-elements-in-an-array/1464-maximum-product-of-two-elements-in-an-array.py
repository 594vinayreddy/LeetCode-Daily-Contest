class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = 0
        sdecond = 0

        for digit in nums:
            if digit >= largest:
                second = largest
                largest = digit

            elif digit > second:
                second = digit
            
        return (largest -1) * (second - 1)
        