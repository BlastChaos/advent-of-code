
inputPath = "./Day 12/input.txt"
file = open(inputPath, "r")

robots = {}

seconds = 100


contents = file.readlines()

for i in range(len(contents)):
    row = contents[i]

    positionVelocity = row.strip().split(" ")

    position = positionVelocity[0].replace("p=", "").split(",")

    velocity = positionVelocity[1].replace("v=", "").split(",")

    robots[i] = {
        "position": [int(position[0]), int(position[1])],
        "velocity": [int(velocity[0]), int(velocity[1])]
    }


def move(robot, second):
    robot["position"][0] =  (robot["position"][0] + robot["velocity"][0] * second) % 101
    robot["position"][1] = (robot["position"][1] + robot["velocity"][1] * second) % 103

    if robot["position"][0] < 0:
        robot["position"][0] += 101

    if robot["position"][1] < 0:
        robot["position"][1] += 103

    print(robot["position"])

topLeft = 0
topRight = 0
bottomLeft = 0
bottomRight = 0


for key, robot in robots.items():
    move(robot, seconds)
    x, y = robot["position"]

    if x == 101 // 2 or y == 103 // 2:
        continue

    if x < 101 // 2 and y < 103 // 2:
        topLeft += 1
    elif x < 101 // 2 and y > 103 // 2:
        bottomLeft += 1
    elif x > 101 // 2 and y < 103 // 2:
        topRight += 1
    else:
        bottomRight += 1

print(topLeft)
print(topRight)
print(bottomLeft)
print(bottomRight)

print(topLeft*topRight*bottomLeft*bottomRight)




