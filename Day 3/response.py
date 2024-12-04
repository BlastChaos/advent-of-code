import re

inputPath = "./Day 3/input.txt"
file = open(inputPath, "r")

values = []

for line in file:
    values = values + re.findall(r'(?:mul\(\d+,\d+\)|do\(\)|don\'t\(\))', line)

result = 0

enabled = True

for i in range(len(values)):
    resultRow = 1
    print(values[i])
    if values[i] == "don't()":
        enabled = False
        continue
    elif values[i] == "do()":
        enabled = True
        continue

    if not enabled:
        continue


    rows= re.findall(r'\d+', values[i])
    for j in range(len(rows)):
        resultRow = resultRow * int(rows[j])
    result = result + resultRow

print(result)
