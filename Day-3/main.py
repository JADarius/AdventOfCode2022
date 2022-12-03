# Problem 1

file = open("input", "r")

input = file.read().split("\n")

prio = 0

for bag in input:
    mid = (int)(len(bag) / 2)
    for type in bag[:mid]:
        if type in bag[mid:]:
            if type.islower():
                prio += ord(type) - ord('a') + 1
            else:
                prio += ord(type) - ord('A') + 27
            break

print("Problem 1: ", prio)

# Problem 2

file = open("input", "r")

input = file.read().split("\n")

prio = 0

for index in range(0, len(input), 3):
    bag1 = input[index]
    bag2 = input[index + 1]
    bag3 = input[index + 2]
    for type in bag1:
        if type in bag2 and type in bag3:
            if type.islower():
                prio += ord(type) - ord('a') + 1
            else:
                prio += ord(type) - ord('A') + 27
            break

print("Problem 2: ", prio)