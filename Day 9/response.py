import re

inputPath = "./Day 9/input.txt"
file = open(inputPath, "r")

currentPostion = []
direction = 0

word = []

positionGo = set([])

content = file.readlines()[0]

isFile = True

result = []


for i in range(len(content)):
    valueToAppend = ""
    if(i%2 == 0):
        valueToAppend = str(int(i/2))
    else:
        valueToAppend = "."
    for j in range(int(content[i])):
        result.append(valueToAppend)



isDone = False
position = 0

for i in range(len(result)):
    if(result[len(result)-1-i] != "."):
        while(result[position] != "."):
            position += 1
            if(position > len(result)-1-i):
                isDone = True
                break
        if(isDone):
            break
        result[position] = result[len(result)-1-i]
        result[len(result)-1-i] = "."


print(result)
position= 0 
sum = 0
while(result[position] != "."):
    sum += int(result[position])* position
    position += 1
print(sum)

