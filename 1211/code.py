import re
import operator

with open('input.txt') as f:
  lines = f.readlines()

class Monkey:
  def __init__(self, name: int, items: list, operation, test, inspect_count = 0):
    self.name = name
    self.items = items
    self.operation = operation
    self.test = test
    self.inspect_count = inspect_count
    
# Part 1
monkeys = []

ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv }

for i, line in enumerate(lines):
  if line.startswith("Monkey"):
    operation_str = re.match(r'.*old\s(.{1})\s(\d+|old)', lines[i+2])
    operator = ops[operation_str.group(1)]
    y = operation_str.group(2)
    modulo = int(re.findall(r'\d+', lines[i+3])[0])
    test_true = int(re.findall(r'\d+', lines[i+4])[0])
    test_false = int(re.findall(r'\d+', lines[i+5])[0])
    monkey = Monkey(
        name = re.match(r'.*(\d+)', line).group(1),
        items = [int(i) for i in re.findall(r'\d+', lines[i+1])],
        operation = lambda x, operator=operator, y=y: operator(x, x if y == "old" else int(y)),
        test = lambda x, modulo=modulo, test_true=test_true, test_false=test_false: test_true if x % modulo == 0 else test_false
      )
    monkeys.append(monkey)

for i in range(0, 20):
  for monkey in monkeys:
    for item in monkey.items:
      item_after_inspection = monkey.operation(item) // 3
      next_monkey = monkey.test(item_after_inspection)
      monkeys[next_monkey].items.append(item_after_inspection)
      monkey.inspect_count += 1
    monkey.items = []

monkeys.sort(key=lambda x: x.inspect_count, reverse=True)
# print(monkeys[0].inspect_count)
# print(monkeys[1].inspect_count)
print(monkeys[0].inspect_count * monkeys[1].inspect_count)
