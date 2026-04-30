from collections import deque

n = int(input())
names = [input().strip() for _ in range(n)] 

# list of letters that come that must come after it 
graph = {c:[] for c in "abcdefghijklmnopqrstuvwxyz"}

# indegree how many letters must come before this letter
indegree = {c:0 for c in "abcdefghijklmnopqrstuvwxyz"} 

impossible = False
#compare each neighboring pair
for i in range(n-1):
    a = names[i]
    b = names[i+1]

    #find the first differing char
    found = False

    for k in range(min(len(a), len(b))):
        if a[k] != b[k]:
            graph[a[k]].append(b[k])
            indegree[b[k]] += 1
            found = True
            break

    if not found and len(a) > len(b):
        impossible = True 

if impossible:
    print("Impossible")

else:
    # topological sort 
    queue = deque()

    for c in "abcdefghijklmnopqrstuvwxyz":
        if indegree[c] == 0:
            queue.append(c)

    result = []

    while queue:
        c = queue.popleft()

        result.append(c)

        for neighbor in graph[c]:
            indegree[neighbor] -= 1 

            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) == 26:
        print(''.join(result))
    else:
        print("Impossible")
