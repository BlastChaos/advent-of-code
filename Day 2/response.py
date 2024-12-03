import os

inputPath = "./Day 2/input.txt"
file = open(inputPath, "r")

values = []

for line in file:
    values.append(line.strip().split(" "))

def is_safe(valuesRow):
    asc = all(int(valuesRow[i]) < int(valuesRow[i + 1]) and 1 <= int(valuesRow[i + 1]) - int(valuesRow[i]) <= 3 for i in range(len(valuesRow) - 1))
    desc = all(int(valuesRow[i]) > int(valuesRow[i + 1]) and 1 <= int(valuesRow[i]) - int(valuesRow[i + 1]) <= 3 for i in range(len(valuesRow) - 1))
    return asc or desc

def can_be_safe_with_one_removal(valuesRow):
    for i in range(len(valuesRow)):
        new_row = valuesRow[:i] + valuesRow[i + 1:]
        if is_safe(new_row):
            return True
    return False

result = 0

for valuesRow in values:
    if is_safe(valuesRow) or can_be_safe_with_one_removal(valuesRow):
        result += 1

print(result)
file.close()