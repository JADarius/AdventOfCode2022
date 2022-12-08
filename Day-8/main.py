# Problem 1

file = open("input", "r")
input = file.read().split("\n")

visible = 2 * len(input) + 2 * (len(input) - 2)

for i in range(1, len(input) - 1):
    for j in range(1, len(input) - 1):
        vis = 4
        for k in range(j - 1, -1, -1):
            if int(input[i][j]) <= int(input[i][k]):
                vis -= 1
                break
        for k in range(j + 1, len(input)):
            if int(input[i][j]) <= int(input[i][k]):
                vis -= 1
                break
        for k in range(i - 1, -1, -1):
            if int(input[i][j]) <= int(input[k][j]):
                vis -= 1
                break
        for k in range(i + 1, len(input)):
            if int(input[i][j]) <= int(input[k][j]):
                vis -= 1
                break
        if vis > 0:
            visible = visible + 1

print("Problem 1: ", visible)

# Problem 2

file = open("input", "r")
input = file.read().split("\n")

max_visible = 0

for i in range(1, len(input) - 1):
    for j in range(1, len(input) - 1):
        vis = 1
        count = 0
        for k in range(j - 1, -1, -1):
            count += 1
            if int(input[i][j]) <= int(input[i][k]) or k == 0:
                vis *= count
                break
        count = 0
        for k in range(j + 1, len(input)):
            count += 1
            if (int(input[i][j]) <= int(input[i][k])) or (k == (len(input) - 1)):
                vis *= count
                break
        count = 0
        for k in range(i - 1, -1, -1):
            count += 1
            if int(input[i][j]) <= int(input[k][j]) or k == 0:
                vis *= count
                break
        count = 0
        for k in range(i + 1, len(input)):
            count += 1
            if (int(input[i][j]) <= int(input[k][j])) or (k == (len(input) - 1)):
                vis *= count
                break
        if vis > max_visible:
            max_visible = vis

print("Problem 2: ", max_visible)