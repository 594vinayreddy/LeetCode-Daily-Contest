from collections import deque

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        grid = [list(row) for row in classroom]

        sr = sc = -1
        litter_index = {}
        litter_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S':
                    sr, sc = i, j
                elif grid[i][j] == 'L':
                    litter_index[(i, j)] = litter_count
                    litter_count += 1

        full_mask = (1 << litter_count) - 1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        start_mask = 0
        if (sr, sc) in litter_index:
            start_mask |= 1 << litter_index[(sr, sc)]

        if start_mask == full_mask:
            return 0

        best = {(sr, sc, start_mask): energy}
        queue = deque([(sr, sc, start_mask, energy, 0)])  

        while queue:
            r, c, mask, e, moves = queue.popleft()

            if e <= 0:
                continue  

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                if grid[nr][nc] == 'X':
                    continue

                ne = energy if grid[nr][nc] == 'R' else e - 1

                nmask = mask
                if (nr, nc) in litter_index:
                    nmask |= 1 << litter_index[(nr, nc)]

                if nmask == full_mask:
                    return moves + 1

                key = (nr, nc, nmask)
                if best.get(key, -1) >= ne:
                    continue  
                best[key] = ne
                queue.append((nr, nc, nmask, ne, moves + 1))

        return -1