def solve():
    n = int(input())

    a = input()
    b = input()

    flipped = False
    possible = True

    ones = [0]*(n+ 1)

    for i in range(n):
        ones[i+1] = ones[i] + (1 if a[i] == '1' else 0)

    for i in range(n- 1, -1, -1):
        if flipped:
            if a[i] == '1':
                effective = '0'
            else:
                effective = '1'
        else:
            effective = a[i]

        if effective == b[i]:
            pass
        else:               # effective != b[i]:
            prefix_length = i + 1

            if prefix_length % 2 == 1:
                possible = False
                break
            
            o = ones[prefix_length]
            z = prefix_length - o
            if o != z:
                possible = False
                break
            flipped = not flipped

    if possible:
        print("YES")
    else:
        print("NO")

t = int(input())

for _ in range(t):
    solve()
