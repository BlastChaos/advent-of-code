from typing import List

inputPath = "./Day 10/input.txt"
file = open(inputPath, "r")

position = []

startPosition = set()

contents = file.readlines()

for i in range(len(contents)):
    row = contents[i]
    positionRow = []
    for j in range(len(row.strip())):
        value = int(row[j])
        if(value == 0):
            startPosition.add((i,j))
        positionRow.append(value)
    position.append(positionRow)




def findPath(x, y, number):
    if number == 9:
        return 1
    

    pathResult = 0

    numberIncreased = number + 1

    if x >0 and position[x-1][y] == numberIncreased:
        pathResult += findPath(x-1, y, numberIncreased)
    
    if x < len(position) - 1 and position[x+1][y] == numberIncreased:
        pathResult+= findPath(x+1, y, numberIncreased)
    
    if y > 0 and position[x][y-1] == numberIncreased:
        pathResult+= findPath(x, y-1, numberIncreased)
    
    if y < len(position[0]) - 1 and position[x][y+1] == numberIncreased:
        pathResult+= findPath(x, y+1, numberIncreased)
    
    return pathResult

result = 0
for x,y in startPosition:
    result = result + findPath(x, y, 0)

print(result)








#Part 1
# def findPath(x, y, number, positionAlreadyVisited = set()):
#     if number == 9:
#         if (x,y) in positionAlreadyVisited:
#             return 0
#         else:
#             positionAlreadyVisited.add((x,y))
#             return 1
    

#     pathResult = 0

#     numberIncreased = number + 1

#     if x >0 and position[x-1][y] == numberIncreased:
#         pathResult += findPath(x-1, y, numberIncreased, positionAlreadyVisited)
    
#     if x < len(position) - 1 and position[x+1][y] == numberIncreased:
#         pathResult+= findPath(x+1, y, numberIncreased, positionAlreadyVisited)
    
#     if y > 0 and position[x][y-1] == numberIncreased:
#         pathResult+= findPath(x, y-1, numberIncreased, positionAlreadyVisited)
    
#     if y < len(position[0]) - 1 and position[x][y+1] == numberIncreased:
#         pathResult+= findPath(x, y+1, numberIncreased, positionAlreadyVisited)
    
#     return pathResult

# result = 0
# for x,y in startPosition:
#     result = result + findPath(x, y, 0, set())

# print(result)




