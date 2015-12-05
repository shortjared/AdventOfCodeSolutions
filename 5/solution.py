def has_3_vowels(line):
    count = 0
    for char in list(line):
        if char in ('aeiou'):
            count += 1
        if count == 3:
            return True

    return False


def has_double_repeat(line):
    print(line)
    last_char = ""
    for char in list(line):
        if char == last_char:
            return True
        last_char = char

    return False


def no_naughty_pairs(line):
    for naughty_pair in ['ab', 'cd', 'pq', 'xy']:
        if naughty_pair in line:
            return False

    return True


def process_line(line):
    return has_3_vowels(line) and has_double_repeat(line) and no_naughty_pairs(line)

nice_strings, naughty_strings = 0, 0

with open('input.txt') as f:
    for line in f:
        if(process_line(line.strip())):
            nice_strings += 1
        else:
            naughty_strings += 1

print("Nice Strings: " + str(nice_strings))
print("Naughty Strings: " + str(naughty_strings))
