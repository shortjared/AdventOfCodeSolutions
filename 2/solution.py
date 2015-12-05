#                    _   _
#                   ((\o/))
#              .-----//^\\-----.
#              |    /`| |`\    |
#              |      | |      |
#              |      | |      |
#              |      | |      |
#              '------===------'


def process_line(line):
    line = line.strip().split('x')
    line = [int(i) for i in line]
    line.sort()
    a1_and_slack = (3*line[0]*line[1])
    a2 = (2*line[0]*line[2])
    a3 = (2*line[1]*line[2])
    return a1_and_slack + a2 + a3

total = 0
with open('input.txt') as f:
    for line in f:
        total += process_line(line)

print("Square footage needed: " str(total))
