# ----------
# User Instructions:
# https://youtu.be/bQA2ELDNmmg
# https://youtu.be/M7ZJ74RVHqo
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

cost = [2, 1, 20] # cost has 3 values, corresponding to making 
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

def optimum_policy2D(grid, init, goal, cost):
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    value = [
                [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
                [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
                [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
                [[999 for row in range(len(grid[0]))] for col in range(len(grid))]
            ]
    change = True
    while change:
        change = False
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if goal == [y, x]:
                    for h in range(len(forward)):
                        if value[h][y][x] > 0:
                            value[h][y][x] = 0
                            policy[y][x] = '*'
                            change = True
                elif grid[y][x] == 0:
                    for h in range(len(forward)):
                        for a in range(len(action)):
                            h2 = (h + action[a]) % len(forward)
                            delta = forward[h2]
                            y2 = y + delta[0]
                            x2 = x + delta[1]
                            if y2 >= 0 and y2 < len(grid) and x2 >= 0 and x2 < len(grid[0]) and grid[y2][x2] == 0:
                                v2 = value[h2][y2][x2] + cost[a]
                                if v2 < value[h][y][x]:
                                    change = True
                                    value[h][y][x] = v2

    for h in range(len(value)):
        for y in range(len(value)):
            print(value[h][y])
        print("----------------------------------------------")

    y, x, h = init
    while [y, x] != goal:
        minV, minA = 999, -1
        for a in range(len(action)):
            h2 = (h + action[a]) % len(forward)
            delta = forward[h2]
            y2 = y + delta[0]
            x2 = x + delta[1]
            if y2 >= 0 and y2 < len(grid) and x2 >= 0 and x2 < len(grid[0]) and grid[y2][x2] == 0:
                if value[h2][y2][x2] + cost[a] < minV:
                    minV = value[h2][y2][x2] + cost[a]
                    minA = a
        if minA == -1:
            return 'Failed'
        
        policy[y][x] = action_name[minA]
        h = (h + action[minA]) % len(forward)
        delta = forward[h]
        y = y + delta[0]
        x = x + delta[1]

    return policy

policy = optimum_policy2D(grid, init, goal, cost)
for i in range(len(policy)):
    print(policy[i])