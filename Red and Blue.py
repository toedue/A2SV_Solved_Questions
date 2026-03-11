t = int(input())

for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))

    m = int(input())
    b = list(map(int, input().split()))


    for i in range(1, len(r)):
        r[i] += r[i-1]

    for i in range(1, len(b)):
        b[i] += b[i-1]

    max_r = max(0,max(r))
    max_b = max(0,max(b))

    

    print(max_r + max_b)


