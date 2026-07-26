class Solution(object):
    def maximumProduct(self, nums):
        largest = second = third = float("-inf")
        smallest = second_smallest = float("inf")

        for x in nums:
            if x >= largest:
                third = second
                second = largest
                largest = x
            elif x >= second:
                third = second
                second = x
            elif x > third:
                third = x

            if x <= smallest:
                second_smallest = smallest
                smallest = x
            elif x < second_smallest:
                second_smallest = x

        return max(
            largest * second * third,
            largest * smallest * second_smallest
        )