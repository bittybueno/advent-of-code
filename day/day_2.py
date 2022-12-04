# A = X = rock = 1
# B = Y = paper = 2 
# C = Z = scissors = 3

# win = 6
# draw = 3
# lose = 0

file = open('input_files/day_2_input.txt', 'r')
lines = file.readlines()
total_points = []

def do_you_win(you, opp):
    if opp == you:
        return 0

    # rock vs paper
    if you == 1 and opp == 2:
        return -1

    # rock vs scissors
    if you == 1 and opp == 3:
        return 1

    # paper vs rock
    if you == 2 and opp == 1:
        return 1

    # paper vs scissors
    if you == 2 and opp == 3:
        return -1

    # scissors vs rock
    if you == 3 and opp == 1:
        return -1

    # scissors vs paper
    if you == 3 and opp == 2:
        return 1


def getMoveScore(move):
    if move == "A" or move == "X":
        return 1

    if move == "B" or move == "Y":
        return 2

    if move == "C" or move == "Z":
        return 3

for line in lines:
    you_score = 0

    stripped = line.split()
    opponent = stripped[0]
    you = stripped[1]

    opponent_score = getMoveScore(opponent)
    you_score = getMoveScore(you)

    do_you_win_ret = do_you_win(you_score, opponent_score)

    if do_you_win_ret == 1:
        you_score+=6
    elif do_you_win_ret == -1:
        you_score+=0
    else: 
        you_score+=3
    
    
    total_points.append(you_score)
 
print("Your score is: {}".format(sum(total_points)))


# x -> lose
# y -> draw
# z -> win

# Rock (A) to draw - Rock (X)
# Rock (A) to win - Scissors (Z)
# Rock (A) to lose - Paper (Y)

# Paper (B) to draw - Paper (Y)
# Paper (B) to win - Rock (X)
# Paper (B) to lose - Scissors (Z)

# Scissors (C) to draw - Scissors (Z)
# Scissors (C) to win - Paper (Y)
# Scissors (C) to lose - Rock (X)

draw = {"A": "X", "B": "Y", "C": "Z"}
win = {"A": "Y", "B": "Z", "C": "X"}
lose = {"A": "Z", "B": "X", "C": "Y"}

total_points_2 = []

for line in lines:
    you_score = 0
    stripped = line.split()
    opponent = stripped[0]
    outcome = stripped[1]
    you_move = 0

    if outcome == "X":
        # lose
        you_score+=0
        you_move = getMoveScore(lose[opponent])
    elif outcome == "Y":
        # draw
        you_score+=3
        you_move = getMoveScore(draw[opponent])
    else:
        # win
        you_score+=6
        you_move = getMoveScore(win[opponent])
    
    you_score+=you_move
    total_points_2.append(you_score)

print("Your score for part 2: {}".format(sum(total_points_2)))

    

