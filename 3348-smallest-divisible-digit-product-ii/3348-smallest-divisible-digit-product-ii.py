class Solution:
    DIGIT_FACTORS = [
        (0,0,0,0), (0,0,0,0), (1,0,0,0), (0,1,0,0), (2,0,0,0),
        (0,0,1,0), (1,1,0,0), (0,0,0,1), (3,0,0,0), (0,2,0,0)
    ] 
    PRIMES = (2, 3, 5, 7)

    def smallestNumber(self, num: str, t: int) -> str:
        need = [0, 0, 0, 0]
        for i, p in enumerate(self.PRIMES):
            while t % p == 0:
                t //= p
                need[i] += 1
        if t != 1:
            return "-1"

        min_digits = self._minimal_digits(need)
        if sum(min_digits) > len(num):
            return self._build(min_digits)

        prefix = [0, 0, 0, 0]
        for c in num:
            prefix = self._add(prefix, self.DIGIT_FACTORS[int(c)])

        first_zero = num.find('0')
        if first_zero == -1:
            first_zero = len(num)
            if self._is_subset(need, prefix):
                return num

        n = len(num)
        for i in range(n - 1, -1, -1):
            d = int(num[i])
            prefix = self._subtract(prefix, self.DIGIT_FACTORS[d])  
            space_after = n - 1 - i
            if i > first_zero:
                continue

            for bigger in range(d + 1, 10):
                used = self._add(prefix, self.DIGIT_FACTORS[bigger])
                fill_digits = self._minimal_digits(self._subtract(need, used))
                fill_len = sum(fill_digits)
                if fill_len <= space_after:
                    return (
                        num[:i]
                        + str(bigger)
                        + '1' * (space_after - fill_len)
                        + self._build(fill_digits)
                    )

        full_digits = self._minimal_digits(need)
        return '1' * (n + 1 - sum(full_digits)) + self._build(full_digits)

    def _minimal_digits(self, need):
        e2, e3, e5, e7 = need
        c8, r2 = divmod(e2, 3)
        c9, c3 = divmod(e3, 2)
        c4, c2 = divmod(r2, 2)
        c6 = 0
        if c2 == 1 and c3 == 1:
            c2, c3, c6 = 0, 0, 1
        elif c3 == 1 and c4 == 1:
            c2, c6, c3, c4 = 1, 1, 0, 0
        return [c2, c3, c4, e5, c6, e7, c8, c9] 

    def _build(self, counts):
        parts = []
        for digit in range(2, 10):
            parts.append(str(digit) * counts[digit - 2])
        return ''.join(parts)

    def _add(self, a, b):
        return [x + y for x, y in zip(a, b)]

    def _subtract(self, a, b):
        return [max(0, x - y) for x, y in zip(a, b)]

    def _is_subset(self, need, have):
        return all(n <= h for n, h in zip(need, have))