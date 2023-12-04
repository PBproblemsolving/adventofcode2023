from math import prod

limit = {"red": 12, "green": 13, "blue": 14}
ids = 0
powers = 0

with open("input2.txt") as f:
    f = f.read().splitlines()
    
for line in f:
    valid = True
    as_few = {'red': 0, 'green': 0, 'blue': 0}
    for show in line.split(":")[1].split(";"):
        for cube in show.split(","):
            quantity, colour = cube.split()
            if limit.get(colour) < int(quantity):
                valid = False
            if as_few.get(colour) < int(quantity):
                as_few[colour] = int(quantity)            
    if valid:
        ids += int(line.split(":")[0].split()[1])
    powers += prod(as_few.values())

print(ids)
print(powers)