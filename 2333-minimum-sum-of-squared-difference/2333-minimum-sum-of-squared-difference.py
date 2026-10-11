class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k1: int
        :type k2: int
        :rtype: int
        """
        k = k1 + k2
        d = sorted((abs(a - b) for a, b in zip(nums1, nums2)), reverse=True)

        if sum(d) <= k:
            return 0

        d.append(0)  
        n = len(nums1)

        for i in range(n):
            cnt = i + 1                    
            cost = cnt * (d[i] - d[i + 1])  

            if k >= cost:
                k -= cost                   
            else:
                q, r = divmod(k, cnt)
                level = d[i] - q
                total = r * (level - 1) ** 2 + (cnt - r) * level ** 2
                total += sum(x * x for x in d[i + 1:n])   
                return total

        return 0