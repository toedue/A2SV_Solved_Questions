n = int(input())
a = list(map(int, input().split()))

currentDay = 1
a.sort()

for problem in a:
    if problem >= currentDay:
        currentDay += 1

print(currentDay-1)
