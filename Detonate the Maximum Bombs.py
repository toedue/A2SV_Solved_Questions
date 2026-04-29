class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)

        # graph[i] = list of bombs that bomb i can trigger
        graph = [[] for _ in range(n)]

        for i in range(n):
            x1, y1, r1 = bombs[i]

            for j in range(n):
                if i == j:
                    continue

                x2, y2, r2 = bombs[j]

                dist_sq = (x2-x1)**2 + (y2-y1)**2

                if dist_sq <= r1**2:
                    graph[i].append(j)

        def dfs(node, visited):
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor, visited)

            return len(visited)

        max_count = 0

        for i in range(n):
            visited = {i}
            count = dfs(i, visited)
            max_count = max(max_count, count)

        return max_count
