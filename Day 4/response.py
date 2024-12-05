import re

inputPath = "./Day 4/input.txt"
file = open(inputPath, "r")

wordPermitted = ['X', 'M', 'A', 'S']

values = []

def isPermitted(incrementX, incrementY, values, x, y):
    for i in range(len(wordPermitted)):
        positionX = x + incrementX*i
        positionY = y + incrementY*i
        if(positionX >= len(values) or positionY >= len(values[positionX])):
            return False
        if(positionX < 0 or positionY < 0):
            return False
        
        if(values[positionX][positionY] != wordPermitted[i]):
            return False
    return True


for line in file:
    valuesRow = []
    for value in line.strip():
        if value in wordPermitted:
            valuesRow.append(value)
        else:
            valuesRow.append(".")

    values.append(valuesRow)

print(values)

count = 0

for i in range(len(values)):
    for j in range(len(values[0])):
        if(isPermitted(-1, -1, values, i, j)):
            count+=1
        if(isPermitted(1, 1, values, i, j)):
            count+=1
        if(isPermitted(1, 0, values, i, j)):
            count+=1
        if(isPermitted(-1, 0, values, i, j)):
            count+=1
        if(isPermitted(0, 1, values, i, j)):
            count+=1
        if(isPermitted(0, -1, values, i, j)):
            count+=1
        if(isPermitted(1, -1, values, i, j)):
            count+=1
        if(isPermitted(-1, 1, values, i, j)):
            count+=1
    

print(count)