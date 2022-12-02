# rock paper scissors
# A and X = Rock 1pt
# B and Y = Paper 2pt
# C and Z = scissors 3pt

# loss = 0pts, tie = 3pts, win = 6pts

input = open("input_day_02")
lines = input.readlines()

total_points = 0

outcomes = [
    #A, B, C
    [4, 1, 7],#X
    [8, 5, 2],#Y
    [3, 9, 6] #Z
]

part2_outcomes = [
    #A, B, C
    [3, 1, 2],#X
    [4, 5, 6],#Y
    [8, 9, 7] #Z
]

for line in lines:
    opponent = line[0:1]
    me = line[2:3]

    opponent_index = -1
    me_index = -1

    if opponent == 'A':
        opponent_index = 0
    elif opponent == 'B':
        opponent_index = 1
    else:
        opponent_index = 2

    if me == 'X':
        me_index = 0
    elif me == 'Y':
        me_index = 1
    else:
        me_index = 2

    total_points += part2_outcomes[me_index][opponent_index]
print(total_points)


