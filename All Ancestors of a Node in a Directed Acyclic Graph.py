class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        indegree = [0] * n

        for frm , to in edges:
            graph[frm].append(to)
            indegree[to] += 1

        print(graph)
        print(indegree)

        ancestors = [set() for _ in range(n)]

        #bfs
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()

            for neighbor in graph[node]:
                ancestors[neighbor].update(ancestors[node])
                ancestors[neighbor].add(node)

                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return [sorted(ancestors[i]) for i in range(n)]

     
