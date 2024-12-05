import re

inputPath = "./Day 4/input.txt"
file = open(inputPath, "r")

wordPermitted = ['X', 'M', 'A', 'S']
wordPermittedV2 = ['M', 'A', 'S']

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


def isPermittedV2(values, x, y):
    if(values[x][y] != 'A'):
        return False
    

    if(x-1 < 0 or y-1 < 0):
        return False
    
    if(x+1 >= len(values) or y+1 >= len(values[x])):
        return False
    
    cross1 = (values[x-1][y-1] == 'M' and values[x+1][y+1] == 'S') or (values[x-1][y-1] == 'S' and values[x+1][y+1] == 'M')
    cross2 = (values[x-1][y+1] == 'M' and values[x+1][y-1] == 'S') or (values[x-1][y+1] == 'S' and values[x+1][y-1] == 'M')
    return cross1 and cross2


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
        if(isPermittedV2(values, i, j)):
            count+=1
    

print(count)