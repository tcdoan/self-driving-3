# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def get_neighbors(grid, cell):
    x, y = cell
    neighbors = []
    for i in range(len(delta)):
        dX, dY = delta[i]
        newX, newY = x+dX, y+dY
        if newX >= len(grid) or newX < 0:
            continue
        if newY >= len(grid[0]) or newY < 0:
            continue
        if grid[newX][newY] == 1:
            continue
        neighbors.append(i)
    return neighbors

def compute_value(grid,goal,cost):
    value = [[99 for col in range(len(grid[0]))] for row in range(len(grid))]
    x,y = goal
    value[x][y] = 0
    queue = [[x+delta[i][0], y+delta[i][1]] for i in get_neighbors(grid, goal)]
    while len(queue) != 0:
        curr = queue.pop(0)
        minCost = 99
        for i in get_neighbors(grid, curr):
            newX, newY = curr[0]+delta[i][0], curr[1]+delta[i][1]
            if value[newX][newY] == 99:
                queue.append([newX, newY])
            else: 
                minCost = min(minCost, value[newX][newY])
        value[curr[0]][curr[1]] = minCost + cost
    return value 

def optimum_policy(grid,goal,cost):
    value = compute_value(grid, goal, cost)
    policy = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]

    for x in range(len(grid)): 
        for y in range(len(grid[0])):
            if value[x][y] != 99:
                minVal, minIdx = min([[value[x+delta[i][0]][y+delta[i][1]], i] for i in get_neighbors(grid, [x,y])])
                policy[x][y] = delta_name[minIdx]

    policy[goal[0]][goal[1]] = '*'
    return policy

policy = optimum_policy(grid, goal, cost)
for i in range(len(policy)):
    print(policy[i])