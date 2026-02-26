n , m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


start, end = 0, 0
answer = 0


for i in range(m):
    while start < n and b[i] > a[start]:
        start += 1

    while end < n and b[i] >= a[end]:
        end += 1
    answer += end - start

print(answer)

    

