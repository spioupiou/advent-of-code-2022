with open("input.txt") as f:
    lines = f.readlines()

x = 1
x_values = [x]

for line in lines:
    command, *value = line.strip("\n").split(" ")
    x_values.append(x)
    if command == "addx":
        x += int(*value)
        x_values.append(x)

# Make the 40*6 grid
grid = []
for i in range(0, len(x_values) - 1, 40):
    grid.append(x_values[i : i + 40])

for line in grid:
    for i in range(0, len(line)):
        CRT = i
        if line[i] - 1 <= CRT <= line[i] + 1:
            print("# ", end="")
        else:
            print(". ", end="")

    print("\n")
