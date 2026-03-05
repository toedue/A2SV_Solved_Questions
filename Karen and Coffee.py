n, k, q = map(int, input().split())

recipes = []
questions = []
for _ in range(n):
    x, y = map(int, input().split())
    recipes.append((x,y))

for _ in range(q):
    x, y = map(int, input().split())
    questions.append((x,y))

# print(recipes)
# print(questions)

MAX_TEMP = 200002
ps = [0] * MAX_TEMP

for l, r in recipes:
    ps[l] += 1
    ps[r +1] -= 1

for i in range(1,len(ps)):
    ps[i] += ps[i - 1]

# print(ps)

admissible = [0] * MAX_TEMP

for i in range(len(ps)):
    admissible[i] = 1 if ps[i] >= k else 0
    

for i in range(1, len(admissible)):
    admissible[i] += admissible[i-1]

for l, r in questions:
    print(admissible[r] - admissible[l - 1])
