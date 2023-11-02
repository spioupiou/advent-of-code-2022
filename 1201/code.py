with open('input.txt') as f:
  lines = f.readlines()

inventories = []
sum = 0
for line in lines:
  line = line.strip('\n')
  if line == '':
    inventories.append(sum)
    sum = 0
  else:
    sum += int(line)

inventories.sort(reverse=True)

# TOP 1
print(inventories[0])

top_3_sum = 0
for i, inventory in enumerate(inventories):
  if i == 3:
    break
  top_3_sum += inventory

# TOP 3
print(top_3_sum)