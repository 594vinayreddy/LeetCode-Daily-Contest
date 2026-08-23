class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        leftSum = rightSum = 0
        leftCnt = rightCnt = 0
        for i, c in enumerate(num[:n//2]):
            if c == '?': leftCnt += 1
            else: leftSum += int(c)
        for i, c in enumerate(num[n//2:]):
            if c == '?': rightCnt += 1
            else: rightSum += int(c)

        if (leftCnt + rightCnt) % 2 == 1:
            return True 

        diff = leftSum - rightSum
        return diff != 9 * (rightCnt - leftCnt) // 2