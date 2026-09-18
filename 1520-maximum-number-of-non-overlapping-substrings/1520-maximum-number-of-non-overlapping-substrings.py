class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        first = {}
        last = {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i

        intervals = []
        for c, start in first.items():
            end = last[c]
            i = start
            valid = True
            while i <= end:
                ch = s[i]
                if first[ch] < start:
                    valid = False
                    break
                if last[ch] > end:
                    end = last[ch]  
                i += 1
            if valid:
                intervals.append((start, end))

        intervals.sort(key=lambda x: x[1])

        res = []
        prev_end = -1
        for start, end in intervals:
            if start > prev_end:
                res.append(s[start:end + 1])
                prev_end = end

        return res