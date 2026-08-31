# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        prev = head
        curr = head.next

        index = 1
        first = -1
        last = -1
        min_dist = float("inf")

        while curr and curr.next:
            next_node = curr.next

            if ((curr.val > prev.val and curr.val > next_node.val) or
                (curr.val < prev.val and curr.val < next_node.val)):

                if first == -1:
                    first = index
                else:
                    min_dist = min(min_dist, index - last)

                last = index

            prev = curr
            curr = curr.next
            index += 1

        if min_dist == float("inf"):
            return [-1, -1]

        max_dist = last - first

        return [min_dist, max_dist]