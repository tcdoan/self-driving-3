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
    for dX, dY in delta:
        newX, newY = x+dX, y+dY
        if newX >= len(grid) or newX < 0:
            continue
        if newY >= len(grid[0]) or newY < 0:
            continue
        if grid[newX][newY] == 1:
            continue
        neighbors.append([newX, newY])
    return neighbors

def compute_value(grid,goal,cost):
    value = [[99 for col in range(len(grid[0]))] for row in range(len(grid))]
    x,y = goal
    value[x][y] = 0

    queue = get_neighbors(grid, goal)
    while len(queue) != 0:
        curr = queue.pop()
        minCost = 99
        for newX, newY in get_neighbors(grid, curr):
            if value[newX][newY] == 99:
                queue.append([newX, newY])
            else: 
                minCost = min(minCost, value[newX][newY])
        value[curr[0]][curr[1]] = minCost + cost

    return value 

value = compute_value(grid, goal, cost)
for i in range(len(value)):
    print(value[i])