# Problem 1

file = open("input", "r")

input = file.read().split("\n")

stacks = ["", "", "", "", "", "", "", "", ""]

for i in range(7, -1, -1):
    for j in range (1, 34, 4):
        if input[i][j].isalpha():
            stacks[int(j / 4)] += input[i][j]

for i in range(10, len(input)):
    task = input[i].split(" ")
    count = int(task[1])
    src = int(task[3]) - 1
    dest = int(task[5]) - 1
    for j in range(count):
        stacks[dest] += stacks[src][len(stacks[src]) - 1]
        stacks[src] = stacks[src][:(len(stacks[src]) - 1)]

ans = ""

for stack in stacks:
    ans += stack[len(stack) - 1]

print("Problem 1: ", ans)

# Problem 2

file = open("input", "r")

input = file.read().split("\n")

stacks = ["", "", "", "", "", "", "", "", ""]

for i in range(7, -1, -1):
    for j in range (1, 34, 4):
        if input[i][j].isalpha():
            stacks[int(j / 4)] += input[i][j]

for i in range(10, len(input)):
    task = input[i].split(" ")
    count = int(task[1])
    src = int(task[3]) - 1
    dest = int(task[5]) - 1
    stacks[dest] += stacks[src][(len(stacks[src]) - count):]
    stacks[src] = stacks[src][:(len(stacks[src]) - count)]

ans = ""

for stack in stacks:
    ans += stack[len(stack) - 1]

print("Problem 2: ", ans)