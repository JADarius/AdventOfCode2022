# Problem 1

file = open("input", "r")

input = file.read().split("\n")

count = 0

for pair in input:
    pair_list = pair.split(",")
    first = pair_list[0].split("-")
    second = pair_list[1].split("-")
    if int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[1]):
        count = count + 1
    elif int(first[0]) >= int(second[0]) and int(first[1]) <= int(second[1]):
        count = count + 1

print("Problem 1: ", count)

# Problem 2

file = open("input", "r")

input = file.read().split("\n")

count = 0

for pair in input:
    pair_list = pair.split(",")
    first = pair_list[0].split("-")
    second = pair_list[1].split("-")
    fir_1 = int(first[0])
    fir_2 = int(first[1])
    sec_1 = int(second[0])
    sec_2 = int(second[1])
    if fir_1 in range(sec_1, sec_2 + 1) or fir_2 in range(sec_1, sec_2 + 1) or sec_1 in range(fir_1, fir_2 + 1) or sec_2 in range(fir_1, fir_2 + 1):
        count = count + 1

print("Problem 2: ", count)