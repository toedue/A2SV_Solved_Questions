n , s = map(int, input().split())

a = list(map(int, input().split()))

noOfGoodSegments= 0
curr = 0
left = 0

for right in range(len(a)):
    curr += a[right]
    while curr > s:
        curr -= a[left]
        left += 1  

    noOfGoodSegments += right - left + 1


print(noOfGoodSegments)
