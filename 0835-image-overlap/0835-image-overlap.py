class Solution(object):
    def largestOverlap(self, img1, img2):
        """
        :type img1: List[List[int]]
        :type img2: List[List[int]]
        :rtype: int
        """
        n = len(img1)
        A = [(i, j) for i in range(n) for j in range(n) if img1[i][j] == 1]
        B = [(i, j) for i in range(n) for j in range(n) if img2[i][j] == 1]

        if not A or not B:
            return 0

        shift_count = Counter()
        for ax, ay in A:
            for bx, by in B:
                shift_count[(ax - bx, ay - by)] += 1

        return max(shift_count.values())