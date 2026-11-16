class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        while len(s) > k:
            temp = ""

            for i in range(0, len(s), k):
                group = s[i:i+k]

                total = 0

                for digit in group:
                    total += int(digit)
                
                temp += str(total)

            s = temp 
        
        return s