n , k = map(int, input().split())

a = list(map(int, input().split()))

arr = []

for i in range (1, len(a)):
    arr.append(a[i] - a[i-1])
arr.sort(reverse =True)

ans = (a[-1] - a[0]) - sum(arr[:k-1])

print(ans)
