# A for Rock, B for Paper, and C for Scissors
# X for lose, Y for draw, and Z for win

# 1 for Rock, 2 for Paper, and 3 for Scissors
# 0 if you lost, 3 if the round was a draw, and 6 if you won

def get_hand(opponent, outcome):
  if (outcome == 'Z'): # Win
     if opponent == 'A':
       return 'B'
     elif opponent == 'B':
       return 'C'
     else:
       return 'A'
  if (outcome == 'X'): # Lose
     if opponent == 'A':
       return 'C'
     elif opponent == 'B':
       return 'A'
     else:
       return 'B'
  return opponent

score = 0
points = {
  'A': 1,
  'B': 2,
  'C': 3
}

with open('input.txt') as f:
  rounds = f.readlines()

  for round in rounds:
    opponent, outcome = round.strip('\n').split(' ')
    result = get_hand(opponent, outcome)
    score += points[result]
    if outcome == 'Z': # Win
        score += 6
    elif outcome == 'Y': # Draw
        score += 3

print(score)


