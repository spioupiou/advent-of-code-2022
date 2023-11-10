with open('input.txt') as f:
  lines = f.readlines()

x_values = []
x = 1
x_values.append(x)

for line in lines:
  command, *value = line.strip('\n').split(' ')
  if command == "noop":
    x_values.append(x)
  else:
    x_values.append(x)
    x += int(*value)
    x_values.append(x)

signal_strength = []
for i in range(19, len(x_values), 40):
  signal_strength.append(x_values[i] * (i+1))

print(sum(signal_strength))