def process_line(line):
    line = line.strip().split('x')
    line = [int(i) for i in line]
    line.sort()
    smallest_perimeter = (2*line[0]+2*line[1])
    cubic_feet = (line[0] * line[1] * line[2])
    return smallest_perimeter + cubic_feet

total = 0
with open('input.txt') as f:
    for line in f:
        total += process_line(line)

print("Feet of Ribbon: " + str(total))
