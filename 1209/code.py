with open('input.txt') as f:
  lines = f.readlines()

# H, T starts at (0,0)
head_coordinates = [(0, 0)]
tail_coordinates = [(0, 0)]

# direction map
head_coordinates_delta = {
  'R': (1, 0),  # move right (x+1)
  'U': (0, 1),  # move up    (y+1)
  'L': (-1, 0), # move left  (x-1)
  'D': (0, -1), # move down  (y-1)
}

print(tail_coordinates[-1])

def move_tail(hX, hY):
  tX, tY = tail_coordinates[-1]
  if hX != tX and hY - tY > 1:
    tail_coordinates.append(head_coordinates[-2])
  elif hY != tY and tX - hX > 1:
    tail_coordinates.append(head_coordinates[-2])
  elif hY != tY and hX - tX > 1:
    tail_coordinates.append(head_coordinates[-2])
  elif hX != tX and tY - hY > 1:
    tail_coordinates.append(head_coordinates[-2])
  elif hX - tX > 1:
    tail_coordinates.append(head_coordinates[-2])
  elif hY - tY > 1:
    tail_coordinates.append(head_coordinates[-2])
  elif tX - hX > 1:
    tail_coordinates.append(head_coordinates[-2])
  elif tY - hY > 1:
    tail_coordinates.append(head_coordinates[-2])
   
for line in lines:
  direction, moves = line.strip('\n').split(' ')

  # get coordinates changes depending on direction
  dx, dy = head_coordinates_delta[direction]

  # move head one move at a time
  for _ in range(int(moves)):
      hX, hY = head_coordinates[-1]
      hX_new, hY_new = hX + dx, hY + dy
      head_coordinates.append((hX_new, hY_new))
      move_tail(hX_new, hY_new)
      print(tail_coordinates[-1])
  print("\n")

# 13 with test
# 6269       
print(len(set(tail_coordinates)))