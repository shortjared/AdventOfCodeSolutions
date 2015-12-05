def process_direction(line):
    return 1

NORTH = '^'
EAST = '>'
SOUTH = 'v'
WEST = '<'

santa_current_long = 0
santa_current_lat = 0
robo_santa_current_long = 0
robo_santa_current_lat = 0

santa_presents_map = []
robo_santa_presents_map = []

with open('input.txt') as f:
    index = 0
    for line in f:
        for direction in list(line.strip()):
            index += 1

            if index % 2 == 0:  # SANTA
                if direction == NORTH:
                    santa_current_long += 1
                elif direction == EAST:
                    santa_current_lat += 1
                elif direction == SOUTH:
                    santa_current_long -= 1
                else:  # WEST
                    santa_current_lat -= 1

                santa_presents_map.append(str(santa_current_long)+'.'+str(santa_current_lat))
            else:  # ROBO SANTA
                if direction == NORTH:
                    robo_santa_current_long += 1
                elif direction == EAST:
                    robo_santa_current_lat += 1
                elif direction == SOUTH:
                    robo_santa_current_long -= 1
                else:  # WEST
                    robo_santa_current_lat -= 1

                robo_santa_presents_map.append(str(robo_santa_current_long)+'.'+str(robo_santa_current_lat))


print("Houses that got presents: " + str(len(set(santa_presents_map + robo_santa_presents_map))))
