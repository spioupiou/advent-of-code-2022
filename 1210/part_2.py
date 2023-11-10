with open('test_input.txt') as f:
  lines = f.readlines()

x = 1
x_values = [x]

for line in lines:
  command, *value = line.strip('\n').split(' ')
  x_values.append(x)
  if command == 'addx':
    x += int(*value)
    x_values.append(x)

stuff = []
for i in range(0, len(x_values), 40):
  stuff.append(x_values[i:i+40])

for item in stuff:
  for i in range(0, len(item)):
    # print(item[i], end = "")
    CRT = i
    if i == 0:
      CRT += 1
    if item[i] -1 <= CRT <= item[i]+1:
      print('#', end='')
    else:
      print('.', end ='')
  
  print('\n')

