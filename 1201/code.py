with open('input.txt') as f:
  lines = f.readlines()

inventories = []
total = 0
for line in lines:
  line = line.strip('\n')
  if line == '':
    inventories.append(total)
    total = 0
  else:
    total += int(line)

inventories.sort(reverse=True)

# TOP 1
print(inventories[0])

# TOP 3
print(sum(inventories[0:3]))