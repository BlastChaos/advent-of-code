
inputPath = "./Day 11/input.txt"
file = open(inputPath, "r")

numbers = []

blinkTime = 25

contents = file.readlines()[0].strip().split(" ")

for content in contents:
    numbers.append(int(content))


print(numbers)

def blink(numbers):
    newNumbers = []
    for number in numbers:
        stringNumber = str(number)
        strLength = len(stringNumber)

        if(number == 0):
            newNumbers.append(1)
            continue

        if (strLength % 2 == 0):
            value1 = stringNumber[:strLength//2]
            value2 = stringNumber[strLength//2:]
            newNumbers.append(int(value1))
            newNumbers.append(int(value2))
            continue

        newNumbers.append(number * 2024)
    return newNumbers




for i in range(0, blinkTime):
    numbers = blink(numbers)

print(len(numbers))



