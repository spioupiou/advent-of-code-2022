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

def create_rocks(input_file_name: str) -> list:
    with open(input_file_name) as f:
        lines = f.readlines()


    rocks = []
    for i, _ in enumerate(lines):
        line = lines[i].strip('\n')
        coordinates = re.findall(r"[^->\s]+", line)

        path = set()
        for j in range(1, len(coordinates)):
            start, end = tuple(int(num) for num in coordinates[j-1].split(',')), tuple(int(num) for num in (coordinates[j].split(',')))

            for point in find_points_between(start, end):
                path.add(point)
        rocks.extend(path)

    return rocks    


def add_sand(bottom_max: int) -> tuple:
    sand = (500, 0)
    while sand[1] <= bottom_max:
        # down
        if (sand[0], sand[1]+1) not in rocks:
            sand = (sand[0], sand[1]+1)
        # left down
        elif (sand[0]-1, sand[1]+1) not in rocks:
            sand = (sand[0]-1, sand[1]+1)
        # right down
        elif (sand[0]+1, sand[1]+1) not in rocks:
            sand = (sand[0]+1, sand[1]+1)
        else: # sand is stuck
            return sand
        
def part_1(bottom_max: int):
    sand_units = 0
    new_sand = add_sand(bottom_max=bottom_max)
    while new_sand != None:
        rocks.append((new_sand[0], new_sand[1]))
        sand_units +=1
        new_sand = add_sand(bottom_max=bottom_max)
    return sand_units        


rocks = create_rocks(input_file_name="input.txt")

bottom_max = max(rocks, key=lambda p: p[1])[1]

print(part_1(bottom_max=bottom_max))
