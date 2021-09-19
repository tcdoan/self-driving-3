# -----------
# User Instructions:
# 
# Modify the function search so that it returns
# a table of values called expand. This table
# will keep track of which step each node was
# expanded.
#
# Make sure that the initial cell in the grid 
# you return has the value 0.
# ----------

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid, init, goal, cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------

    # open list elements are of type: [g, y, x]
    closed = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]
    y, x = init
    g = 0
    closed[y][x] = 1

    expand = [[-1 for x in range(len(grid[0]))] for y in range(len(grid))]
    expand[y][x] = 0

    open = [[g, y, x]]
    found, resign = False, False
    expandedLen = 0
    while found is False and resign is False:
        if len(open) == 0:
            resign = True
            print('fail')
            return expand
        else:
            open.sort()
            next = open.pop(0)
            g, y, x = next

            if [y, x] == goal:
                found = True
                print(next)
                return expand
            else:
                # expand winning elemt and add to new open list
                for i in range(len(delta)):
                    y2, x2 = y + delta[i][0], x + delta[i][1]
                    if y2 >= 0 and y2 < len(grid) and x2 >=0 and x2 < len(grid[0]) and closed[y2][x2] == 0 and grid[y2][x2] == 0:
                        g2 = g + cost
                        open.append([g2, y2, x2])
                        closed[y2][x2] = 1
                        expandedLen += 1
                        expand[y2][x2] = expandedLen
    
    return 'fail'

expand = search(grid, init, goal, cost)
for i in range(len(expand)):
    print(expand[i])
