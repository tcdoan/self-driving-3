# -----------
# User Instructions:
#
# Modify the the search function so that it returns
# a shortest path as follows:
# 
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left, 
# up, and down motions. Note that the 'v' should be 
# lowercase. '*' should mark the goal cell.
#
# You may assume that all test cases for this function
# will have a path from init to goal.
# ----------

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1
delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right
delta_name = ['^', '<', 'v', '>']
def search(grid, init, goal, cost):
    path = {}
    y, x = init
    g = 0
    open = [[g, y, x]]
    closed = [[0 for x in range(len(grid[0]))] for col in range(len(grid))]
    closed[y][x] = 1
    found, resign = False, False 
    while not found and not resign:
        if len(open) == 0:
            resign = True
            print('fail')
            return None
        else:
            open.sort()
            next = open.pop(0)
            g, y, x = next
            if [y, x] == goal:
                found = True
                return path
            else:
                for i in range(len(delta)):
                    y2 = y + delta[i][0]
                    x2 = x + delta[i][1]
                    if y2 >= 0 and y2 < len(grid) and x2 >=0 and x2 < len(grid[0]):
                        if closed[y2][x2] == 0 and grid[y2][x2] == 0:
                            g2 = g + cost
                            open.append([g2, y2, x2])
                            closed[y2][x2] = 1
                            path[(y2, x2)] = (y, x, delta_name[i])
    return path

expand = [['.' for x in range(len(grid[0]))] for y in range(len(grid))]
path = search(grid, init, goal, cost)

y, x = goal
symbol = '*'
while  [y, x] != init:
    expand[y][x] = symbol
    y, x, symbol = path[(y, x)]
expand[y][x] = symbol

for i in range(len(expand)):
    print(expand[i])