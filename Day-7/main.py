# Problems 1 + 2

directories = {}

file = open("input", "r")

input = file.read().split("\n")

def check_folder(dir, index):
    size = 0
    while index < len(input):
        if input[index] == "$ cd ..":
            break
        if input[index].startswith("$ ls"):
            index = index + 1
            while not input[index].startswith("$"):
                if input[index].startswith("dir"):
                    index = index + 1
                else:
                    size += int(input[index].split(" ")[0])
                    index = index + 1
                if index == len(input):
                    break
        elif input[index].startswith("$ cd "):
            folder = dir + input[index].split(" ")[2] + "/"
            check = check_folder(folder, index + 1)
            size += check[0]
            index = check[1] + 1
    directories.update({dir:size})
    return (size, index)

index = 1
check_folder("/", index)

sum = 0

space_needed = 30000000 - (70000000 - directories["/"])

min = 70000000

for folder in directories:
    if directories[folder] <= 100000:
        sum += directories[folder]
    if directories[folder] >= space_needed and directories[folder] < min:
        min = directories[folder]

print("Problem 1: ", sum)
print("Problem 2: ", min)