n , s = map(int, input().split())

a = list(map(int, input().split()))

left = 0
noOfSegments = 0
curr = 0

for right in range(len(a)):
    curr += a[right]
    while curr >= s:
        noOfSegments += n - right
        curr -= a[left]
        left += 1

print(noOfSegments)
