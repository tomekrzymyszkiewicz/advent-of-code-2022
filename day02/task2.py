enemy_dict = {'A':'rock','B':'paper','C':'scissors'}
results = {'X':0,'Y':3,'Z':6}
win = [['rock','paper'],['paper','scissors'],['scissors','rock']]
loss = [list(reversed(pair)) for pair in win]
draw = [[pair[0]]*2 for pair in win]
results_pairs = {'X':loss,'Y':draw,'Z':win}
move_points = {'scissors':3, 'paper':2,'rock':1}
moves = [line.split() for line in open('input.txt','r')]

points = 0
for move in moves:
    points += results.get(move[1])
    player_move,  = [pair[1] for pair in results_pairs.get(move[1]) if pair[0]==enemy_dict.get(move[0])]
    points += move_points.get(player_move)
    
print(points)