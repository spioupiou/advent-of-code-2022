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
    # Create a queue of points to visit + set of visited points
    # Add the starting point to the queue and visited set
    queue = [PointWithStep(start, 0)]
    visited = set([start])
    
    # Until the queue is emptied:
    while queue:
        # Dequeue the first point
        point_with_step = queue.pop(0)
        current, step = point_with_step.point, point_with_step.step
        if current.coordinates() not in visited:
            visited.add(current.coordinates())
            # Find adjacent points
            filtered_adjacent_points = []
            # Make sure the adjacent points are in the height map and can be moved to
            for point in current.find_neighbors():
                if (point.coordinates()) in height_map and current.can_move_to(point):
                    filtered_adjacent_points.append(point)
            # For each adjacent point:
            for point in filtered_adjacent_points:
                # If the point is the target point, return true (increment step by 1 because we need to move to the goal)
                if point.is_goal():
                    return step + 1
                # Otherwise increment the step needed to reach that point by 1 and append to queue
                queue.append(PointWithStep(point, step + 1))

# Part 1
print(find_shortest_path(start, end))

# Part 2
paths = []
for k, v in height_map:
    if height_map[k, v] == 0:
        paths.append(find_shortest_path(Point(k, v), end))

print(min(filter(lambda x: x is not None, paths)))
