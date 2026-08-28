class Solution(object):
    def lexPalindromicPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        n = len(target)
        freq = Counter(s)
        odd_chars = [c for c in freq if freq[c] % 2 == 1]
        if len(odd_chars) > 1:
            return ""
        mid_char = odd_chars[0] if odd_chars else None

        m = (n + 1) // 2
        doubled_len = n // 2
        avail = {c : freq[c] // 2 for c in freq}

        remaining = dict(avail)
        p_max = 0
        for i in range(min(n, doubled_len)):
            c = target[i]
            if remaining.get(c, 0) > 0:
                remaining[c] -= 1
                p_max = i + 1
            else:
                break
        
        def build(half):
            return half + half[::-1] if n % 2 == 0 else half + half[:-1][::-1]

        if doubled_len == p_max and (n % 2 == 0 or target[m - 1] == mid_char):
            candidate = build(target[:m])
            if candidate > target:
                return candidate
        
        remaining = dict(avail)
        for i in range(p_max):
            remaining[target[i]] -= 1

        p = p_max
        while p >= 0:
            if p <= m - 1:
                if n % 2 == 1 and p == m -1:
                    if mid_char is not None and mid_char > target[p]:
                        candidate = build(target[:p] + mid_char)
                        if candidate > target:
                            return candidate
                else:
                    chosen = next((chr(c) for c in range(ord(target[p]) + 1, ord('z') + 1) if remaining.get(chr(c), 0) > 0), None)

                    if chosen:
                        remaining[chosen] -= 1
                        rest= ''.join(chr(c) * remaining.get(chr(c), 0) for c in range(ord('a'), ord('z') + 1))
                        half = target[:p] + chosen + rest + (mid_char if n% 2 else "")
                        candidate = build(half)
                        if candidate > target:
                            return candidate
                        remaining[chosen] += 1
            
            if p > 0:
                remaining[target[p - 1]] = remaining.get(target[p - 1], 0) + 1
            p -= 1
        return ""