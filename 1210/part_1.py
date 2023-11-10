with open('input.txt') as f:
  lines = f.readlines()

x = 1
x_values = [x]

for line in lines:
  command, *value = line.strip('\n').split(' ')
  x_values.append(x)
  if command == "addx":
    x += int(*value)
    x_values.append(x)

signal_strength = []
for i in range(19, len(x_values), 40):
  signal_strength.append(x_values[i] * (i+1))

print(sum(signal_strength))