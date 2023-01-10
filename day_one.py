#part one
cal = open("day_1.txt", "r")

calories = cal.read().split("\n")

sum = 0
kcal = 0

for i in calories:
    if i == "":
        if sum > kcal:
            kcal = sum
        sum = 0
    else:
        sum += int(i)
print(kcal)


#part2
sum = 0
kcal = []

for i in calories:
    if i == "":
        kcal.append(sum)
        sum = 0
    else:
        sum += int(i)

kcal.sort(reverse=True)
counter = 0
for i in range(3):
    counter += kcal[i]

print(counter)