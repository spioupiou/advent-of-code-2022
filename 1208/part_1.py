import re

with open("input.txt") as f:
    lines = f.readlines()

trees = [] 

for line in lines:
    row = list(line.strip('\n'))
    trees.append(row)

# Add all edges are they're visible from the outside
count = (len(trees) - 2) * 2 + len(trees[0]) * 2

def check_top(x, y, value):
    while (x >= 0):
        if int(value) <= int(trees[x][y]):
            return False
        x -= 1
    return True

def check_down(x, y, value):
    while (x <= len(trees)-1):
        if int(value) <= int(trees[x][y]):
            return False
        x += 1
    return True

def check_left(x, y, value):
    while (y >= 0):
        if int(value) <= int(trees[x][y]):
            return False
        y -= 1
    return True

def check_right(x, y, value):
    while (y <= len(trees[x])-1):
        if int(value) <= int(trees[x][y]):
            return False
        y += 1
    return True

for i in range(1, len(trees)-1, 1):
    for j in range(1, len(trees[i])-1, 1):
        if check_top(i-1, j, trees[i][j]):
            count += 1
            continue
        if check_down(i+1, j, trees[i][j]):
            count += 1
            continue
        if check_left(i, j-1, trees[i][j]):
            count += 1
            continue
        if check_right(i, j+1, trees[i][j]):
            count += 1
            continue

print(count)