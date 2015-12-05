def has_repeating_pair(line):
    index = 1
    last_char = "HOHOHO"
    for char in list(line):
        if index <= len(line) and last_char + char in line[index:]:
            return True
        else:
            index += 1
            last_char = char

    return False


def has_split_pair(line):
    index = 2
    for char in list(line):
        if index < len(line) and char == line[index]:
            return True
        index += 1

    return False


def process_line(line):
    return has_repeating_pair(line) and has_split_pair(line)

nice_strings, naughty_strings = 0, 0

with open('input.txt') as f:
    for line in f:
        if(process_line(line.strip())):
            nice_strings += 1
        else:
            naughty_strings += 1

print("Nice Strings: " + str(nice_strings))
print("Naughty Strings: " + str(naughty_strings))
