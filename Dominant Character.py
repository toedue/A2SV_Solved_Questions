t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    d = {
        "aa":2,
        "aba": 3,
        "aca": 3,
        "abca": 4,
        "acba": 4,
        "abbacca": 7,
        "accabba": 7,
    }


    flag = False

    for key in d.keys():
        if key in s:
            flag = True
            break

    if flag:
        print(d[key])
    else:
        print(-1)
