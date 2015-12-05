def process_direction(line):
    return 1

NORTH = '^'
EAST = '>'
SOUTH = 'v'
WEST = '<'

# Started from the bottom
current_long = 0
current_lat = 0

presents_map = []
presents_map.append(str(current_long)+'.'+str(current_lat))

with open('input.txt') as f:
    for line in f:
        for direction in list(line.strip()):
            if direction == NORTH:
                current_long += 1
            elif direction == EAST:
                current_lat += 1
            elif direction == SOUTH:
                current_long -= 1
            else:  # WEST
                current_lat -= 1

             presents_map.append(str(current_long)+'.'+str(current_lat))


# Now I'm here
print("Presents delivered: " + str(len(presentsMap)))
print("Houses that got presents: " + str(len(set(presentsMap))))
