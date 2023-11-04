with open('input.txt') as f:
  pairs = f.readlines()

count = 0

# pairs = ["2-4,6-8\n", "2-3,4-5\n", "5-7,7-9\n", "2-8,3-7\n", "6-6,4-6\n", "2-6,4-8\n"]
for pair in pairs:
  pair = pair.strip('\n').split(',')

  for i in range(0, len(pair), 2):
    array1 = [int(x) for x in pair[i].split('-')]
    array2 = [int(x) for x in pair[i + 1].split('-')]

    if array2[0] <= array1[0] <= array2[1] or array2[0] <= array1[1] <= array2[1]:
      count+=1
    elif array1[0] <= array2[0] <= array1[1] or array1[0] <= array2[1] <= array1[1]:
      count += 1
      
print(count)