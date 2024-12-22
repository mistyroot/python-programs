scores=[]
n=int(input("Enter how many players?"))

for i in range(n):
    score=int(input("Enter Score "))
    scores.append(score)

print(f'Scores are {scores}')

# Calculating Total
total=0
for s in scores:
    total=total+s

print(f'Total Score is {total}')

# Maximum score
max_score=0
for s in scores:
    if s>max_score:
        max_score=s

print(f'Maximum Score is {max_score}')

# Minimum Score
min_score=scores[0]
for s in scores:
    if s<min_score:
        min_score=s

print(f'Minimum Score is {min_score}')


