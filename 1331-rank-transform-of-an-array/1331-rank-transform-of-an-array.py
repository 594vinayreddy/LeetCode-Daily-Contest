class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        rank = {v : i for i,v in enumerate(sorted(set(arr)),1)}
        return [rank[v] for v in arr]