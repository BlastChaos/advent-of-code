import os
inputPath = "./input.txt"
file = open(inputPath, "r")

values = []


for line in file:
    print(line.strip().split(" "))
    values.append(line.strip().split(" "))


# QUESTION 1

# left.sort()
# right.sort()

# diff = 0

# for i in range(len(left)):
#     diff += abs(left[i] - right[i])

# print(diff)


# QUESTION 2

result = 0

for i in range(len(left)):
    valuePresentRight = 0
    valueLeft = left[i]

    for j in range(len(right)):
        if right[j] == valueLeft:
            valuePresentRight+=1
    
    result+= valueLeft * valuePresentRight

print(result)