import re

with open('input.txt') as f:
  lines = f.readlines()

stacks = []
instructions = []

for i, line in enumerate(lines):
  line = line.strip('\n')
  if i <= 7:
    stacks.append(line)
  elif i > 9:
    instructions.append(line)

formatted_stacks = [[] for i in range(9)] 

for stack in stacks:
  work = re.findall('....?', stack)
  for i, letter in enumerate(work):
    letter = letter.replace('[', '').replace('] ', '').replace(']', '')
    if letter.isspace():
      continue
    else:
      formatted_stacks[i].append(letter)

for stack in formatted_stacks:
  stack.reverse()

for instruction in instructions:
  num_list = re.findall('\d+', instruction)
  ###### PART 1 ######
  # for item in range(0, int(num_list[0])):
  #   moved_stack = formatted_stacks[int(num_list[1])-1].pop()
  #   formatted_stacks[int(num_list[2])-1].append(moved_stack)

  ###### PART 2 ######
  moved_stack = formatted_stacks[int(num_list[1])-1][-(int(num_list[0])):]
  for item in moved_stack:
    formatted_stacks[int(num_list[1])-1].pop()
    formatted_stacks[int(num_list[2])-1].append(item)

result = ""

for item in formatted_stacks:
  result += item.pop()

print(result)