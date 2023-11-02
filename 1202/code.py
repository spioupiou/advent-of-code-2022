# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors

# 1 for Rock, 2 for Paper, and 3 for Scissors
# 0 if you lost, 3 if the round was a draw, and 6 if you won

def get_score(opponent, me):
  if (opponent == 'A' and me == 'X') or (opponent == 'B' and me == 'Y') or (opponent == 'C' and me == 'Z'):
    return "draw"
  elif me == "X": # Rock
      if opponent == "C": # Scissors
          return "win"
      else:
          return "lose"
  elif me == "Y": # Paper
      if opponent == "A": # Rock
          return "win"
      else:
          return "lose"
  elif me == "Z": # Scissors
      if opponent == "B": # Paper
          return "win"
      else:
          return "lose"

score = 0
points = {
  'X': 1,
  'Y': 2,
  'Z': 3
}

with open('input.txt') as f:
  rounds = f.readlines()

  for round in rounds:
    opponent, me = round.strip('\n').split(' ')
    result = get_score(opponent, me)
    score += points[me]
    match result:
      case "win":
        score += 6
      case "draw":
        score += 3

print(score)


