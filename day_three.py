with open("day_3.txt", "r") as instruct:
    supplies = instruct.readlines()
    supplies = [line.strip() for line in supplies]


#part 1


points = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14,
             'o': 15, 'p': 16, 'q':17, 'r':18, 's':19, 't':20, 'u': 21, 'v' : 22, 'w' : 23, 'x' : 24, 'y' : 25, 'z' : 26,
          'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39,
             'N': 40, 'O': 41, 'P': 42, 'Q':43, 'R':44, 'S':45, 'T':46, 'U': 47, 'V' : 48, 'W' :49, 'X' : 50, 'Y' : 51, 'Z' : 52}

shared = []
for i in supplies:
    length = int(len(i))
    half = int(length/2)
    first_half = i[0:half]
    first_half = ''.join(sorted(set(first_half), key=first_half.index))
    second_half = i[half:]
    second_half = ''.join(sorted(set(second_half), key=second_half.index))
    for j in first_half:
        if j in second_half:
            shared.append(j)

count = 0
for i in shared:
    x = points[i]
    count += x

print(count)

#part two

newlist = []
for i in range(0, len(supplies) - 3 + 1):
    newlist.append(''.join(supplies[i:i+3]))

bruh = []
for i in range(0, len(supplies) - 3 + 1):
    if i % 3 == 0:
        first = supplies[i]
        first = ''.join(sorted(set(first), key=first.index))
        second = supplies[i+1]
        second = ''.join(sorted(set(second), key=second.index))
        third = supplies[i+2]
        third = ''.join(sorted(set(third), key=third.index))
        for j in first:
            if (j in second) and (j in third):
                bruh.append(j)

counted = 0
for i in bruh:
    s = points[i]
    counted += s
print(counted)
