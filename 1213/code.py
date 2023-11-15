import json

with open("input.txt") as f:
    lines = f.readlines()

signals = []
for i, _ in enumerate(lines):
    line = lines[i].strip('\n')
    if (line == ""):
        continue
    nested_list = json.loads(line)
    signals.append(nested_list)

def compare(left, right):
    # print("left:", left)
    # print("right:", right)
    if type(left) == type(right) == int:
        if left < right:
            return 1
        elif right < left:
            return -1
        else:
            return 0
    elif type(left) == int:
        return compare([left], right)
    elif type(right) == int:
        return compare(left, [right])
    else:
        if left == right:
            return 0
        for i, _ in enumerate(left):
            if i >= len(right):
                return -1
            result = compare(left[i], right[i])
            if result == 1 or result == -1:
                return result
    return 1


i = 1
correct = []
for left, right in zip(signals[0::2], signals[1::2]):
    result = compare(left, right)
    if result == 1:
        correct.append(i)
    i+=1

print(sum(correct))
print (compare([1],[1]))

            

