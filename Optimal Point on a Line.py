n = int(input())

arr = list(map(int, input().split()))
arr.sort()
size = len(arr)

if size % 2 == 1:
    print(arr[size//2])
else:
    print(arr[(size-1)//2])

# The best position is the median of the points
