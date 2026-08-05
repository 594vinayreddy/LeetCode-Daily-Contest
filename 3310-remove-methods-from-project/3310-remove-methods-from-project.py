class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(list)
        for a, b in invocations:
            graph[a].append(b)

        suspicious = {k}
        queue = deque([k])

        while queue:
            node = queue.popleft()
            for v in graph[node]:
                if v not in suspicious:
                    suspicious.add(v)
                    queue.append(v)

        for a, b in invocations:
            if b in suspicious and a not in suspicious:
                return list(range(n))

        return sorted(i for i in range(n) if i not in suspicious)