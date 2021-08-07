# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's 
# optimal path to the position specified in goal; 
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a 
# right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right
                
goal = [2, 0] # given in the form [row,col]

cost = [2, 1, 30] # cost has 3 values, corresponding to making 
                  # a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------



def compute_value(grid,goal,cost):
    value = [[[999 for dir in range(len(forward))] for col in range(len(grid[0]))] for row in range(len(grid))]
    x,y = goal
    value[x][y] = [0 for dir in range(len(forward))]

    changed = True
    while changed:
        changed = False
        for x in range(len(value)):
            for y in range(len(value[0])):
                if grid[x][y] == 0:
                    for dir in range(len(value[0][0])):
                        minVal = value[x][y][dir]
                        minIdx = -1;
                        for i in range(len(action)):
                            newDir = (dir+action[i]) % len(forward)
                            newX = x + forward[newDir][0]
                            newY = y + forward[newDir][1]
                            if newX < len(grid) and newX >=0 and newY < len(grid[0]) and newY >= 0 and grid[newX][newY] == 0:
                                if value[newX][newY][newDir] + cost[i] < minVal:
                                    minVal = value[newX][newY][newDir] + cost[i]
                                    minIdx = i
                        if minIdx != -1:
                            value[x][y][dir] = minVal
                            changed = True

    return value 

value = compute_value(grid, goal, cost)
for i in range(len(value)):
    print(value[i])

def optimum_policy2D(grid,init,goal,cost):
    value = compute_value(grid, goal, cost)
    policy = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]

    x, y, dir = init
    minIdx = 0
    while minIdx != -1:
        minVal = 999
        minIdx = -1
        for i in range(len(action)):
            newDir = (dir+action[i]) % len(forward)
            newX = x + forward[newDir][0]
            newY = y + forward[newDir][1]
            if newX < len(grid) and newX >=0 and newY < len(grid[0]) and newY >= 0 and grid[newX][newY] == 0:
                if value[newX][newY][newDir] + cost[i] < minVal:
                    minVal = value[newX][newY][newDir] + cost[i]
                    minIdx = i
        policy[x][y] = action_name[minIdx]
        dir = (dir+action[minIdx]) % len(forward)
        x = x + forward[dir][0]
        y = y + forward[dir][1]

    policy[goal[0]][goal[1]] = '*'
    return policy

policy = optimum_policy2D(grid,init,goal,cost)
for i in range(len(policy)):
    print(policy[i])