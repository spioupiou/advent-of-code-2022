# message = "bvwbjplbgvbhsrlpgdmjqwftvncz"

with open('input.txt') as f:
  message = f.readlines()[0]

def check(buffer: str) -> bool:
  for char in buffer:
    if buffer.count(char) > 1:
      return False
  return True

# For Part 2 change to 14
for i, _ in enumerate(message):
  if i + 4 <= len(message):
    buffer = message[i:i+4]
    if check(buffer):
      print(i + 4)
      break
    
