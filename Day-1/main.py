# Problem 1

file = open("input", "r")

input = file.read()

max = 0

ceva = input.split("\n\n")
for list in ceva:
    elf = list.split("\n")
    suma = 0
    for cal in elf:
        if cal != '':
            suma += int(cal)
    if suma > max:
        max = suma

print("Problem 1: ", max)

# Problem 2

file2 = open("input", "r")

input = file2.read()

max1 = 0
max2 = 0
max3 = 0

ceva = input.split("\n\n")
for list in ceva:
    elf = list.split("\n")
    suma = 0
    for cal in elf:
        if cal != '':
            suma += int(cal)
    if suma > max1:
        max3 = max2
        max2 = max1
        max1 = suma
    elif suma > max2:
        max3 = max2
        max2 = suma
    elif suma > max3:
        max3 = suma

print("Problem 2: ", (max1 + max2 + max3))