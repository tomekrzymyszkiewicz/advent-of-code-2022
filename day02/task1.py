enemy_dict = {'A':'rock','B':'paper','C':'scissors'}
player_dict = {'X':'rock','Y':'paper','Z':'scissors'}
win = [['rock','paper'],['paper','scissors'],['scissors','rock']]
loss = [list(reversed(pair)) for pair in win]
draw = [[pair[0]]*2 for pair in win]
results = {6:win, 3:draw, 0:loss}
move_points = {'scissors':3, 'paper':2,'rock':1}
moves = [line.split() for line in open('input.txt','r')]

points = 0
for move in moves:
    move_translated = [enemy_dict.get(move[0]),player_dict.get(move[1])]
    for result_points,result_list in results.items():
        if move_translated in result_list:
            points += result_points
    points += move_points.get(move_translated[1])
    
print(points)