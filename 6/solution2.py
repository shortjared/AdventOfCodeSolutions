# Super easy because solution to #1 was generalized enough!
# #Planning #TurnUpTheLights

OFF, ON, TOGGLE = -1, 1, 2

grid = [[0 for x in range(1000)] for x in range(1000)]


def light_ops(grid, cords_1, cords_2, action):
    cords_1 = map(int, cords_1.split(','))
    cords_2 = map(int, cords_2.split(','))

    x_cords = [cords_1[0], cords_2[0]]
    y_cords = [cords_1[1], cords_2[1]]
    x_cords.sort()
    y_cords.sort()

    for x in range(x_cords[0], x_cords[1] + 1):
        for y in range(y_cords[0], y_cords[1] + 1):
                grid[x][y] += action

                # lazy reset to zero
                if grid[x][y] < 0:
                    grid[x][y] = 0

    return grid


def process_line(line, grid):
    line = line.strip().split(' ')
    if "toggle" in line:
        cords_1 = line[1]
        cords_2 = line[3]
        action = TOGGLE
    elif "on" in line:
        cords_1 = line[2]
        cords_2 = line[4]
        action = ON
    else:
        cords_1 = line[2]
        cords_2 = line[4]
        action = OFF

    return light_ops(grid, cords_1, cords_2, action)


with open('input.txt') as f:
    for line in f:
        grid = process_line(line, grid)

    print("Lights On: " + str(sum(map(sum, grid))))