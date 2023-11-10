with open('input.txt') as f:
  lines = f.readlines()

head_coordinates = []
tail_coordinates = []
# start at 0.0
head_coordinates.append((0, 0))
tail_coordinates.append((0, 0))

print(tail_coordinates[-1])

def check_tail(hX, hY):
  tX, tY = tail_coordinates[-1]
  if hX != tX and hY - tY > 1:
    tX = hX
    tY = hY - 1
    tail_coordinates.append((tX, tY))
  elif hY != tY and tX - hX > 1:
    tX = hX + 1
    tY = hY
    tail_coordinates.append((tX, tY))
  elif hY != tY and hX - tX > 1:
    tX = hX - 1
    tY = hY
    tail_coordinates.append((tX, tY))
  elif hX != tX and tY - hY > 1:
    tX = hX
    tY = hY + 1
    tail_coordinates.append((tX, tY))
  elif hX - tX > 1:
    tX = hX - 1
    tail_coordinates.append((tX, tY))
  elif hY - tY > 1:
    tY = hY - 1
    tail_coordinates.append((tX, tY))
  elif tX - hX > 1:
    tX = hX + 1
    tail_coordinates.append((tX, tY))
  elif tY - hY > 1:
    tY = hY + 1
    tail_coordinates.append((tX, tY))

def move_tail(direction, moves):
  match direction:
    case 'R':
      # move right
      for _ in range(int(moves)):
        hX, hY = head_coordinates[-1]
        hX += 1
        head_coordinates.append((hX, hY))
        check_tail(hX, hY)
        print(tail_coordinates[-1])
    case 'U':
      # move up
      for _ in range(int(moves)):
        hX, hY = head_coordinates[-1]
        hY += 1
        head_coordinates.append((hX, hY))
        check_tail(hX, hY)
        print(tail_coordinates[-1])
    case 'L':
      # move left
      for _ in range(int(moves)):
        hX, hY = head_coordinates[-1]
        hX -= 1
        head_coordinates.append((hX, hY))
        check_tail(hX, hY)
        print(tail_coordinates[-1])
    case 'D':
      # move down
      for _ in range(int(moves)):
        hX, hY = head_coordinates[-1]
        hY -= 1
        head_coordinates.append((hX, hY))
        check_tail(hX, hY)
        print(tail_coordinates[-1])
  print("\n")
      

      
for line in lines:
    direction, moves = line.strip('\n').split(' ')
    # check if direction is R U L or D
    move_tail(direction, moves)



          
print(len(set(tail_coordinates)))