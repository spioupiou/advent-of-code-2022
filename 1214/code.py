import re

def find_points_between(start, end: tuple) -> list:
    points = []

    # Check if the x-coordinates are the same (vertical line)
    if start[0] == end[0]:
        # Ensure start is the lower point
        if start[1] > end[1]:
            start, end = end, start
        for y in range(start[1], end[1] + 1):
            points.append((start[0], y))
    # Check if the y-coordinates are the same (horizontal line)
    elif start[1] == end[1]:
        # Ensure start is the leftmost point
        if start[0] > end[0]:
            start, end = end, start
        for x in range(start[0], end[0] + 1):
            points.append((x, start[1]))

    return points

def create_blocks(input_file_name: str) -> list:
    with open(input_file_name) as f:
        lines = f.readlines()


    blocks = []
    for i, _ in enumerate(lines):
        line = lines[i].strip('\n')
        coordinates = re.findall(r"[^->\s]+", line)

        path = set()
        for j in range(1, len(coordinates)):
            start, end = tuple(int(num) for num in coordinates[j-1].split(',')), tuple(int(num) for num in (coordinates[j].split(',')))

            for point in find_points_between(start, end):
                path.add(point)
        blocks.extend(path)

    return blocks    


def add_sand(blocks: list, bottom_max: int) -> tuple:
    sand = (500, 0)
    while sand[1] <= bottom_max:
        # down
        if (sand[0], sand[1]+1) not in blocks:
            sand = (sand[0], sand[1]+1)
        # left down
        elif (sand[0]-1, sand[1]+1) not in blocks:
            sand = (sand[0]-1, sand[1]+1)
        # right down
        elif (sand[0]+1, sand[1]+1) not in blocks:
            sand = (sand[0]+1, sand[1]+1)
        else: # sand is stuck
            return sand
    return sand   

def show_blocks(blocks: list):
    x_base = min(blocks, key=lambda p: p[0])[0]
    y_base = max(blocks, key=lambda p: p[1])[1]
    x_size = max(blocks, key=lambda p: p[0])[0] - x_base + 1
    y_size = y_base + 1
    for y in range(y_size):
        for x in range(x_size):
            if (x_base + x, y) in blocks:
                print('#', end='')
            else:
                print('.', end='')
        print()

        
def part_1(blocks: list):
    bottom_max = max(blocks, key=lambda p: p[1])[1]
    sand_units = 0
    new_sand = add_sand(blocks=blocks, bottom_max=bottom_max)
    while new_sand != None:
        blocks.append(new_sand)
        sand_units +=1
        new_sand = add_sand(blocks=blocks, bottom_max=bottom_max)
    return sand_units      

def part_2(blocks: list):
    bottom_max = max(blocks, key=lambda p: p[1])[1]
    sand_units = 0
    new_sand = add_sand(blocks=blocks, bottom_max=bottom_max)
    while new_sand != (500, 0):
        #show_blocks(blocks)
        #print()
        #print(sand_units)
        print(len(set(blocks)))
        blocks.append(new_sand)
        sand_units +=1
        new_sand = add_sand(blocks=blocks, bottom_max=bottom_max)    
    return sand_units + 1


blocks = create_blocks(input_file_name="input.txt")
print(part_2(blocks=blocks))
