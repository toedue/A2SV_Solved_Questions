from collections import deque, defaultdict

import sys
input = sys.stdin.readline 




def bfs(start, graph, n):
    # bfs from start node, returns (farthest_node, distance_to_farthest_node)

    # dist[i] = distance from start to node i
    # -1 means not visited yet 

    dist = [- 1] * (n+1)
    dist[start] = 0

    queue = deque()
    queue.append(start)

    farthest_node = start
    max_dist = 0

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if dist[neighbor] == -1: # not visited
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)

                # track the farthest node we've seen
                if dist[neighbor] > max_dist:
                    max_dist = dist[neighbor]
                    farthest_node = neighbor

    return farthest_node, max_dist




n = int(input())

# built adjacency list
graph = defaultdict(list)

for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

if n == 1:
    print(0)
else:
    # bfs from node 1, and find the farthest node A
    A, _ = bfs(1, graph, n)

    # bfs from A to find the farthest node B and the diameter
    B, diameter = bfs(A, graph, n)

    # circumference 
    print(diameter * 3)

