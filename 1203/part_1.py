sum = 0

with open('input.txt') as f:
  bags = f.readlines()

  for bag in bags:
    bag = bag.strip('\n')
    half = len(bag)//2
    comp_1 = set(bag[:half])
    comp_2 = set(bag[half:])
    common = ''.join(comp_1.intersection(comp_2))

    if common.islower():
      sum += ord(common) - 96
    else:
      sum += ord(common) - 38

print(sum)