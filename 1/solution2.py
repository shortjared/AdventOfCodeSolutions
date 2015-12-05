# Guess I would hvae saved a but of time if I did this for part 1

UP = '('
DOWN = ')'

floor = 0
operation = 0

# "UP DOWN UP DOWN UP DOWN, 'cause all I do is Win"
#     - DJ Khaled

with open('input.txt') as f:
    for line in f:
        for direction in list(line.strip()):
            operation += 1
            if direction == UP:
                floor += 1
            elif direction == DOWN:
                floor -= 1

            if floor == -1:
                break

print("Basemented Entered on Operation: " + str(operation))
