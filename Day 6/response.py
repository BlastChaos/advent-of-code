import re

inputPath = "./Day 6/input.txt"
file = open(inputPath, "r")

currentPostion = []
direction = 0

word = []

positionGo = set([])

content = file.readlines()

for i in range(len(content)):
    wordRow = []
    for j in range(len(content[i])):
        if(content[i][j] == '^'):
            positionGo.add((i, j))
            currentPostion = [i, j]
        wordRow.append(content[i][j])

    word.append(wordRow)


def canEscape(direction, currentPosition):
    if(direction == 0):
        return currentPosition[0] <= 0
    if(direction == 1):
        return currentPosition[1] >= len(word[0])
    if(direction == 2):
        return currentPosition[0] >= len(word)
    if(direction == 3):
        return currentPosition[1] <= 0
    return False


def hasObstacle(direction, currentPosition):
    obstablePosition = []

    if(direction == 0):
        obstablePosition = [currentPosition[0] - 1, currentPosition[1]]
    if(direction == 1):
        obstablePosition = [currentPosition[0], currentPosition[1] + 1]
    if(direction == 2):
        obstablePosition = [currentPosition[0] + 1, currentPosition[1]]
    if(direction == 3):
        obstablePosition = [currentPosition[0], currentPosition[1] - 1]

    return not canEscape(direction, obstablePosition) and word[obstablePosition[0]][obstablePosition[1]] == '#'


while not canEscape(direction, currentPostion):
    if(direction == 0):
        currentPostion[0] -= 1
    elif(direction == 1):
        currentPostion[1] += 1
    elif(direction == 2):
        currentPostion[0] += 1
    elif(direction == 3):
        currentPostion[1] -= 1

    if(hasObstacle(direction, currentPostion)):
        direction = (direction +1) % 4


    if tuple(currentPostion) not in positionGo:
        positionGo.add(tuple(currentPostion))

print(len(positionGo))