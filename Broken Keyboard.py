t = int(input())

for _ in range(t):
    s = input()

    left = 0
    set_ = set()

    while left < len(s):
        right = left 
        while right < len(s) and s[left] == s[right]:
            right += 1
        
        if (right - left) % 2 == 1:
            set_.add(s[left])

        left = right

    # print(set_)

    print("".join(sorted(set_)))        


# Loops,O(n),Each character is visited once by the pointers.
# Sorting,O(1),Alphabet size is fixed at 26 letters.
# Space,O(1),Set size never exceeds 26 letters.
