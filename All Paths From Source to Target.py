class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        target = len(graph) - 1

        def dfs(node, current_path):
            if node == target:
                result.append(list(current_path))
                return

            for neighbor in graph[node]:
                current_path.append(neighbor)
                dfs(neighbor, current_path)
                current_path.pop()

        # Start DFS from node 0 with path [0]   
        dfs(0, [0])

        return result
