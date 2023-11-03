sum = 0

with open('input.txt') as f:
  bags = f.readlines()
  
  for i in range(0, len(bags), 3):
    bag1 = set(bags[i].strip('\n'))
    bag2 = set(bags[i+1].strip('\n'))
    common = bag1.intersection(bag2)
    bag3 = set(bags[i+2].strip('\n'))
    common3 = ''.join((common).intersection(bag3))
    print(common3)


    if common3.islower():
      sum += ord(common3) - 96
    else:
      sum += ord(common3) - 38

print(sum)