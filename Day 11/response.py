
inputPath = "./Day 11/input.txt"
file = open(inputPath, "r")

stones = {}

blinkTime = 75

contents = file.readlines()[0].strip().split(" ")

for content in contents:
    stones[int(content)] = 1


print(stones)

def blink(currentStones):
    newStones = currentStones.copy()
    for key, currentCount in currentStones.items():
        newNumbers = blink_one_stone(key)
        for number in newNumbers:
            if number in newStones:
                newStones[number] += currentCount
            else:
                newStones[number] = currentCount
        newStones[key] += -1 * currentCount
        if newStones[key] == 0:
            del newStones[key]    
    return newStones


def blink_one_stone(number):
    stringNumber = str(number)
    strLength = len(stringNumber)

    if(number == 0):
        return [1]

    if (strLength % 2 == 0):
        value1 = stringNumber[:strLength//2]
        value2 = stringNumber[strLength//2:]
        return [int(value1), int(value2)]
    
    return [number * 2024]




for i in range(0, blinkTime):
    stones = blink(stones)

count = 0
for key, value in stones.items():
    count+=value
print(stones)

print(count)



