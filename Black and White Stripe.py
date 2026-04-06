t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    count = 0
    ans = n

    for i in range(k):
        if s[i] == 'W':
            count += 1

    ans = min(ans, count)

    for i in range(k,n):
        if s[i] == 'W':
            count += 1
        if s[i-k] == 'W':
            count -= 1

        ans = min(ans, count)

    print(ans)


