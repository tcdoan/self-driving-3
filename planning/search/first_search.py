# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space


grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def inBounds(grid, cell):
    if cell[0] >= len(grid) or cell[0] < 0:
        return False
    if cell[1] >= len(grid[0]) or cell[1] < 0:
        return False
    if grid[cell[0]][cell[1]] == 1:
        return False
    return True

def search(grid,init,goal,cost):
    pq = [tuple(init)]
    visited = {tuple(init)}
    costs = {tuple(init):0}
    numVisited = 0

    while len(pq) != 0:
        curr = pq.pop(0)
        if list(curr) == goal:
            print(numVisited)
            return [costs[curr]] + list(curr)
        for [dX, dY] in delta: 
            found = (curr[0]+dX, curr[1]+dY)
            if found not in visited and inBounds(grid, found):
                visited.add(found)
                numVisited += 1
                pq.append(found)
                costs[found] = costs[curr] + cost

    return 'fail'

print(search(grid, init, goal, cost))