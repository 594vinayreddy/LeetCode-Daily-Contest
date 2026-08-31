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
        curr = head
        nodes = []
        critical_points = []

        while curr:
            nodes.append(curr.val)
            curr = curr.next
        
        for i in range(2, len(nodes)):
            if nodes[i - 2] > nodes[i - 1] < nodes[i] or nodes[i - 2] < nodes[i - 1] > nodes[i]:
                critical_points.append(i - 1)

        m = len(critical_points)

        if m < 2:
            return [-1, -1]

        max_dist = critical_points[-1] - critical_points[0]

        min_dist = float("inf")

        for i in range(1, m):
            min_dist = min(min_dist, critical_points[i] - critical_points[i - 1])

        return [min_dist, max_dist]

