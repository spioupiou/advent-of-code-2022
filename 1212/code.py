import re

with open("input.txt") as f:
    lines = f.readlines()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def find_neighbors(self):
        return [
            Point(self.x+1, self.y), 
            Point(self.x-1, self.y), 
            Point(self.x, self.y+1), 
            Point(self.x, self.y-1)
        ]
    
    def coordinates(self) -> tuple:
        return (self.x, self.y)
    
    def is_goal(self) -> bool:
        return self.x == end.x and self.y == end.y
    
    def can_move_to(self, point):
        return height_map[point.coordinates()] - height_map[self.coordinates()] <= 1

start: Point
end: Point
height_map = {}

for i, line in enumerate(lines):
    line = line.strip('\n')
    for j, char in enumerate(line):
        here = Point(j, i)
        match char:
            case 'S':
                height = 0
                start = here
            case 'E':
                height = 25
                end = here
            case default:
                height = ord(char)-ord('a')
        height_map[here.coordinates()] = height

class PointWithStep:
    def __init__(self, point: Point, step: int):
        self.point = point
        self.step = step

def find_shortest_path(start: Point, end: Point):
    # Keep track of visited points
    visited = set([start])
    # Keep track of all the paths to be checked
    queue = [[start]]
    
    # Until the queue is emptied:
    while queue:
        # Dequeue the first path
        path = queue.pop(0)
        # Get the last point from the path
        current = path[-1]
        # If the last point has not been visited...
        if current.coordinates() not in visited:
            visited.add(current.coordinates())
            # ...find the adjacent points
            filtered_adjacent_points = []
            # Make sure the adjacent points are in the height map and can be moved to
            for point in current.find_neighbors():
                if (point.coordinates()) in height_map and current.can_move_to(point):
                    filtered_adjacent_points.append(point)
            # For each adjacent point, make a new path and push it into the queue:
            for point in filtered_adjacent_points:
                new_path = list(path)
                new_path.append(point)
                queue.append(new_path)
                # If the point is the target point, return the path taken to reach it
                if point.is_goal():
                    return new_path
                
    raise ValueError("No path found")

# Part 1
path = find_shortest_path(start, end)
# Print len(path) - 1 to find the number of steps (because you don't need to move to the starting point)
print(len(path)-1)

# Part 2
paths = []
for k, v in height_map:
    # Try all possible starting points with elevation 0
    if height_map[k, v] == 0:
        try:
            path = find_shortest_path(Point(k, v), end)
            paths.append(path)
        except ValueError:
            print("No path found, skipping")
            continue

# print min no of steps
print(min([len(path) for path in paths])-1)
