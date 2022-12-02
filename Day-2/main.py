# Problem 1

file = open("input", "r")
input = file.read().split("\n")

scor = 0

for play in input:
    if play[2] == 'X':
        scor += 1
        if play[0] == 'C':
            scor += 6
        elif play[0] == 'A':
            scor += 3
    elif play[2] == 'Y':
        scor += 2
        if play[0] == 'A':
            scor += 6
        elif play[0] == 'B':
            scor += 3
    else:
        scor += 3
        if play[0] == 'B':
            scor += 6
        elif play[0] == 'C':
            scor += 3

print("Problem 1: ", scor)

# Problem 2

file = open("input", "r")
input = file.read().split("\n")

scor = 0

for play in input:
    outcome = play[2]
    opponent = play[0]
    if outcome == 'X':
        if opponent == 'A':
            scor += 3
        elif opponent == 'B':
            scor += 1
        else:
            scor += 2
    elif outcome == 'Y':
        scor += 3
        if opponent == 'A':
            scor += 1
        elif opponent == 'B':
            scor += 2
        else:
            scor += 3
    else:
        scor += 6
        if opponent == 'A':
            scor += 2
        elif opponent == 'B':
            scor += 3
        else:
            scor += 1

print("Problem 2: ", scor)