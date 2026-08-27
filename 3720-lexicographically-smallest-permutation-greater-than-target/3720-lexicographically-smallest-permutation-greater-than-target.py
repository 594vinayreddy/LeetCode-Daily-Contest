class Solution(object):
    def lexGreaterPermutation(self, s, target):
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        n = len(target)
        used = []
        bp = n  

        for i in range(n):
            idx = ord(target[i]) - ord('a')
            if freq[idx] == 0:
                bp = i
                break
            freq[idx] -= 1
            used.append(idx)

        for j in range(bp, -1, -1):
            if j < len(used):
                freq[used[j]] += 1    
            elif not (j == bp and bp < n):
                continue      

            start = ord(target[j]) - ord('a') + 1
            for c in range(start, 26):
                if freq[c] > 0:
                    freq[c] -= 1
                    result = [target[:j], chr(c + ord('a'))]
                    for x in range(26):
                        if freq[x]:
                            result.append(chr(x + ord('a')) * freq[x])
                    return ''.join(result)

        return ""