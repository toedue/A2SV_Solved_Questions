from collections import Counter

T = int(input()) 

for _ in range(T):

    s = input().strip()
    t = input().strip()

    # check if impossible
    if Counter(s) - Counter(t):
        print("Impossible")
        continue

    answer = []
    index = 0
    box = Counter(t)
    
    # NEW: A running tally of what s still needs
    need = Counter(s) 

    while index < len(s):
        for c in "abcdefghijklmnopqrstuvwxyz":
            
            if box[c] == 0:
                continue

            # take the letter out of the box temporarly
            box[c] -= 1
            
            # NEW: Did this letter match the next letter of s?
            matched = (c == s[index])
            
            # If it matched, we no longer "need" it for the rest of s!
            if matched:
                need[c] -= 1

            # check if our box has enough letters to build what 'need' asks for
            safe = True
            for letter in need:
                if need[letter] > box[letter]:
                    safe = False
                    break
            
            if safe:
                answer.append(c)
                if matched:
                    index += 1  # We matched a letter of s, move forward!
                break

            else:
                # NOT safe! Put the letter back in the box
                box[c] += 1
                
                # AND put the need back if we took it earlier
                if matched:
                    need[c] += 1

    # the remaining letters from the box
    for c in "abcdefghijklmnopqrstuvwxyz":
        answer.append(c * box[c])

    print("".join(answer))
