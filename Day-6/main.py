# Problem 1

input = open("input", "r").read()

for i in range(4, len(input) + 1):
    code = input[(i - 4):i]
    ok = 1
    for letter in code:
        if code.count(letter) != 1:
            ok = 0
            break
    if ok == 1:
        print("Problem 1: ", i)
        break

# Problem 2

input = open("input", "r").read()

for i in range(14, len(input) + 1):
    code = input[(i - 14):i]
    ok = 1
    for letter in code:
        if code.count(letter) != 1:
            ok = 0
            break
    if ok == 1:
        print("Problem 2: ", i)
        break