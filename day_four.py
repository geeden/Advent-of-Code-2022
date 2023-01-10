import re

with open("day_4.txt", "r") as list_pairs:
    pairs = list_pairs.readlines()
    pairs = [line.strip() for line in pairs]

count = []
zcount = []


def part_two(first, second, third, fourth): #part two
    s = 1
    #print(first, second, third, fourth)
    if first in range(third, fourth+1):
        zcount.append(s)
    elif second in range(third, fourth+1):
        zcount.append(s)
    elif third in range(first, second+1):
        zcount.append(s)
    elif fourth in range(first, second+1):
        zcount.append(s)



def compare(first, second, third, fourth): #part one
    x= 1
    if (third >= first) and (second >= fourth):
        count.append(x)
    elif (third <= first) and (second <= fourth):
        count.append(x)


def separate(current):
    for i in current:
        if i in ['-', ',']:
            current = current.replace(i, ' ')
    numberstring = current.split()
    strone = int(numberstring[0])
    strtwo = int(numberstring[1])
    strthree = int(numberstring[2])
    strfour = int(numberstring[3])
    compare(strone, strtwo, strthree, strfour)
    part_two(strone, strtwo, strthree, strfour)


#uncomment for part one
'''for i in pairs:
    separate(i)

print(len(count)) '''



#part two
for i in pairs:
    separate(i)

print(len(zcount))