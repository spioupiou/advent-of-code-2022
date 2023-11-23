import re

start_point = (500, 0)

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

def create_blocks(input_file_name: str) -> dict:
    with open(input_file_name) as f:
        lines = f.readlines()

    blocks = {}
    for i, _ in enumerate(lines):
        line = lines[i].strip('\n')
        coordinates = re.findall(r"[^->\s]+", line)

        for j in range(1, len(coordinates)):
            start, end = tuple(int(num) for num in coordinates[j-1].split(',')), tuple(int(num) for num in (coordinates[j].split(',')))

            for x, y in find_points_between(start, end):
                if x not in blocks.keys():
                    blocks[x] = set()
                blocks[x].add(y)        

    return blocks

def add_sand(blocks: dict, bottom_max: int) -> tuple:
    sand = start_point

    while sand[1] < bottom_max:
        x, y = sand
        y_first_block = min([y_block for y_block in blocks[x] if y_block > y])
        # check if sand can fall to left
        if x - 1 not in blocks.keys():
            return (x - 1, bottom_max)
        elif y_first_block not in blocks[x - 1]:
            sand = (x - 1, y_first_block)
        # check if sand can fall to right
        elif x + 1 not in blocks.keys():
            return (x + 1, bottom_max)     
        elif y_first_block not in blocks[x + 1]:
            sand = (x + 1, y_first_block)
        else:
            return (x, y_first_block - 1)                 
    return sand


def get_max_depth(blocks: dict) -> int:
    max_depth = 0
    for values in blocks.values():
        max_depth_in_values = max(values)
        if max_depth_in_values > max_depth:
            max_depth = max_depth_in_values
    return max_depth        


def show_blocks(blocks: dict):
    x_base = min(blocks.keys())
    x_size = max(blocks.keys()) - x_base + 1
    y_size = get_max_depth(blocks) + 1
    for y in range(y_size):
        for x in range(x_size):
            if x_base + x in blocks.keys() and y in blocks[x_base + x]:
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

def part_2(blocks: dict):
    bottom_max = get_max_depth(blocks) + 1
    sand_units = 0
    new_sand = add_sand(blocks=blocks, bottom_max=bottom_max)
    while new_sand != start_point:
        x, y = new_sand
        if x not in blocks.keys():
            blocks[x] = set()
        blocks[x].add(y)
        #show_blocks(blocks=blocks)
        sand_units +=1
        new_sand = add_sand(blocks=blocks, bottom_max=bottom_max)  
    return sand_units + 1

blocks = create_blocks(input_file_name="input.txt")
print(part_2(blocks=blocks))
