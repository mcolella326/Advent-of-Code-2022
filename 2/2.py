import re

#Part 1
with open(r'./input') as f:
    rounds = f.read()
    rounds = rounds.splitlines()

opponent = []
player = []
for round in rounds:
    o, p = re.split('\s', round)
    opponent.append(o)
    player.append(p)

opp_dict = {'A': 1, 'B': 2, 'C': 3}
play_dict = {'X': 1, 'Y': 2, 'Z': 3}
point_dict = {'lose': 0, 'tie': 3, 'win': 6}

#RPS outcome
def rps(opp_move, play_move):
    if opp_move == play_move:
        outcome = 'tie'
    elif (opp_move == 1 and play_move == 2) or (opp_move == 2 and play_move == 3) or (opp_move == 3 and play_move == 1):
        outcome = 'win'
    else:
        outcome = 'lose'
    return outcome

total_pts = 0
for round, move in enumerate(player):
    outcome = rps(opp_dict[opponent[round]], play_dict[player[round]])
    total_pts += (play_dict[move] + point_dict[outcome])


print(f'The Part 1 answer is {total_pts}')

#Part 2
play_dict_adj = {'X':'lose', 'Y':'tie', 'Z':'win'}

def rps_backcheck(opp_move, win_con):
    if win_con == 'tie':
        played_move = opp_move
    elif win_con == 'win' and opp_move == 1:
        played_move = 2
    elif win_con == 'win' and opp_move == 2:
        played_move = 3
    elif win_con == 'win' and opp_move == 3:
        played_move = 1
    elif win_con == 'lose' and opp_move == 1:
        played_move = 3
    elif win_con == 'lose' and opp_move == 2:
        played_move = 1
    elif win_con == 'lose' and opp_move == 3:
        played_move = 2
    return played_move

total_pts = 0
for round, win_con in enumerate(player):
    played_move = rps_backcheck(opp_dict[opponent[round]], play_dict_adj[player[round]])
    total_pts += (played_move + point_dict[play_dict_adj[win_con]])

print(f'The Part 2 answer is {total_pts}')