t = int(input()) 

for _ in range(t):
    n, x, k = map(int, input().split())
    s = input()

    position = x
    first_hit_time = -1  

    for i in range(n):
        if s[i] == 'L':
            position -= 1
        else:
            position += 1
            
        if position == 0:
            first_hit_time = i + 1  
            break

    if first_hit_time == -1 or first_hit_time > k:  # # if never reaches 0 or not enough time
        print(0)
        continue

    count = 1

    position = 0
    cycle_time = -1

    for i in range(n):
        if s[i] == 'L':
            position -= 1
        else:
            position += 1
        if position == 0:
            cycle_time = i + 1
            break

    if cycle_time == -1:
        print(count)
        continue

    remaining_time = k - first_hit_time

    extra_hits = remaining_time // cycle_time

    count += extra_hits

    print(count)
