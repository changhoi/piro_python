file = open('chicken.txt', 'r', encoding = 'utf-8')

amount = 0
days = 0
for line in file:
    days += 1
    new_line = line.split(": ")
    amount += int(new_line[1])

avg = amount / days

print(avg)