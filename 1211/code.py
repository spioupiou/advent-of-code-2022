import re
import operator

with open('test_input.txt') as f:
  lines = f.readlines()

class Monkey:
  def __init__(self, name: int, items: list, operation, test):
    self.name = name
    self.items = items
    self.operation = operation
    self.test = test
    
# Part 1
monkeys = []

ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv }

for i, line in enumerate(lines):
  if line.startswith("Monkey"):
    operation_str = re.match(r'.*old\s(.{1})\s(\d+|old)', lines[i+2])
    print(operation_str.groups())
    modulo = re.match(r'.*(\d+)', lines[i+3]).group(1)
    test_true = re.match(r'.*monkey\s(\d+)', lines[i+4]).group(1)
    test_false = re.match(r'.*monkey\s(\d+)', lines[i+5]).group(1)
    monkey = Monkey(
        name = re.match(r'.*(\d+)', line).group(1),
        items = [int(x) for x in re.findall(r'\d+', lines[i+1])],
        operation = lambda x: ops[operation_str.group(1)](x, x if operation_str.group(2) == "old" else int(operation_str.group(2))),
        test = lambda x: int(test_true) if x % int(modulo[0]) == 0 else int(test_false)
      )
    monkeys.append(monkey)
    print(monkey.operation(3))

for monkey in monkeys:
  print(monkey.operation(3))