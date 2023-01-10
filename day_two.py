from math import *


with open("day_2.txt", "r") as rounds:
    rounds_in_game = rounds.readlines()
    rounds_in_game = [line.strip() for line in rounds_in_game]

#part 1
count = 0
for i in rounds_in_game:
    opp = i[0]
    you = i[2]
    if opp == "A":
        if you == "X":
            count += 1
            count += 3
        if you == "Y": #you win
            count += 2
            count += 6
        if you == "Z":
            count += 3
    if opp == "B":
        if you == "X":
            count += 1
        if you == "Y":
            count += 2
            count += 3
        if you == "Z":  #you win
            count += 3
            count += 6
    if opp == "C":
        if you == "X":  #you win
            count += 1
            count += 6
        if you == "Y":
            count += 2
        if you == "Z":
            count += 3
            count += 3
print(count)


#part 2
def turn(variable, opp):
    if variable == 'X':
        lists.append(lose[opp])
    if variable == 'Y':
        lists.append(draw[opp])
    if variable == 'Z':
        lists.append(win[opp])


outputs = {'X': 0,
           'Y': 3,
           'Z': 6}

lose = {'A': 3,
        'B': 1,
        'C': 2}

win = {'A': 2,
       'B': 3,
       'C': 1}

draw = {'A': 1,
        'B': 2,
        'C': 3}

lists = []
counts = 0
for i in rounds_in_game:
    second = i[2]
    opp = i[0]
    if second == 'X':
        counts += outputs['X']
        turn(second, opp)
    if second == 'Y':
        counts += outputs['Y']
        turn(second, opp)
    if second == 'Z':
        counts += outputs['Z']
        turn(second, opp)


additional = sum(i for i in lists)

counts += additional
print(counts)


'''
inputs = {'A': 'Rock',
          'B': 'Paper',
          'C': 'Scissors',
          'X': 'Rock',
          'Y': 'Paper',
          'Z': 'Scissors'}

played = {'Rock': 1,
          'Paper': 2,
          'Scissors': 3}

results = {'Lose': 0,
           'Draw': 3,
           'Win': 6}

def possibilities(round):
    opp = inputs[round[0]]
    you = inputs[round[2]]

    if opp == you:
        return (results['Draw'] + played[you])
    if (opp, you) in [('Paper', 'Rock'), ('Scissors', 'Paper'), ('Rock', 'Scissors')]:
        return (results['Lose'] + played[you])
    if (opp, you) in [('Rock', 'Scissors'), ('Paper', 'Scissors'), ('Scissors', 'Rock')]:
        return (results['Win'] + played[you])


sum([possibilities(round) for round in rounds_in_game]) '''


'''    for i in range(len(round)):
    for j in round[i]:
        current = round[i]
        opp = current[0]
        you = current[2]
        possibilites(opp, you)
    '''