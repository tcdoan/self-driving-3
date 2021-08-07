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

def compute_value(grid, goal, cost):
    # make sure your function returns a grid of values as 
    # demonstrated in below videos
    # https://youtu.be/Sn-ZUbZdOn8
    # https://youtu.be/RXpuBRA-cpo
    value = [[99 for x in range(len(grid[0]))] for y in range(len(grid)) ]
    y, x = goal
    value[y][x] = 0
    queue = [goal]
    closed = [[0 for x in range(len(grid[0]))] for y in range(len(grid)) ]

    while len(queue) != 0:
        y, x = queue.pop(0)
        closed[y][x] = 1
        for i in range(len(delta)):
            y2, x2 = y + delta[i][0], x + delta[i][1]
            if y2 >= 0 and y2 < len(grid) and x2 >=0 and x2 < len(grid[0]):
                if grid[y2][x2] == 0 and closed[y2][x2] == 0:
                    value[y2][x2] = value[y][x] + 1
                    queue.append([y2, x2])
    return value 

value = compute_value(grid, goal, cost)
for i in range(len(value)):
    print(value[i])
