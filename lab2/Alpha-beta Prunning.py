import random
import math

id=str(input('Enter you 8 digit Student ID: ')) #Entering 8 digit id through console2
final_id=""
for i in id:
    if i=="0":
        final_id=final_id+"8"
    else:
        final_id=final_id+i
minPoint=int(final_id[4])
shuffle=int(final_id[3])
win_points=final_id[6:8]
win_points=int(win_points[::-1])
maxPoint=math.ceil(win_points*1.5)
values=[]
for i in range(len(final_id)):
    ran=random.randrange(minPoint,maxPoint)
    values.append(ran)


MAX, MIN = float('inf'), -float('inf')
def alphaBetaPruning(depth, nodeIndex, maximizingPlayer,
            values, alpha, beta):
    if depth == 3:
        return values[nodeIndex]
 
    if maximizingPlayer:
        best = MIN
        for i in range(0, 2):
            val = alphaBetaPruning(depth + 1, nodeIndex * 2 + i,
                          False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = MAX
        for i in range(0, 2):
          
            val = alphaBetaPruning(depth + 1, nodeIndex * 2 + i,
                            True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best



#Output for Task 1
print('Generated 8 random points between the minimum and maximum point limits: ',values)
print("Total points to win: ",win_points)
x= alphaBetaPruning(0, 0, True, values, MIN, MAX)
print("Achieved point by applying alpha-beta pruning = ",x)
if x>=win_points:
    print('The Winner is Optimus Prime')
else:
    print('The Winner is Megatron')

#Output for Task 2
print()
print('After the shuffle:')
shuffle_values=[]
for i in range(shuffle):
    random.shuffle(values)
    x=alphaBetaPruning(0, 0, True, values, MIN, MAX)
    shuffle_values.append(x)
print('List of all points values from each shuffle: ',shuffle_values)

m=max(shuffle_values)
print('The maximum value of all shuffles: ', m)

count=0
for i in range(len(shuffle_values)):
    if shuffle_values[i]>=win_points:
        count+=1
print('Won',count,'times out of',len(shuffle_values),'number of shuffles' )