import re

with open("input.txt") as f:
    lines = f.readlines()

trees = []

for line in lines:
    row = list(line.strip("\n"))
    trees.append(row)


def check_top(x, y, value):
    top = 0
    while x >= 0:
        top += 1
        if int(value) <= int(trees[x][y]):
            return top
        x -= 1
    return top


def check_down(x, y, value):
    down = 0
    while x <= len(trees) - 1:
        down += 1
        if int(value) <= int(trees[x][y]):
            return down
        x += 1
    return down


def check_left(x, y, value):
    left = 0
    while y >= 0:
        left += 1
        if int(value) <= int(trees[x][y]):
            return left
        y -= 1
    return left


def check_right(x, y, value):
    right = 0
    while y <= len(trees[x]) - 1:
        right += 1
        if int(value) <= int(trees[x][y]):
            return right
        y += 1
    return right


scenic_scores = []
for i in range(1, len(trees) - 1, 1):
    for j in range(1, len(trees[i]) - 1, 1):
        top_count = check_top(i - 1, j, trees[i][j])
        down_count = check_down(i + 1, j, trees[i][j])
        left_count = check_left(i, j - 1, trees[i][j])
        right_count = check_right(i, j + 1, trees[i][j])
        scenic_scores.append(top_count * left_count * right_count * down_count)

print(max(scenic_scores))
