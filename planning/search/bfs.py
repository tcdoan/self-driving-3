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
# Solution: https://www.youtube.com/embed/cl8Kdkr4Gbg
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

def search(grid, init, goal, cost):
    queue = [init]
    costs = {(init[0], init[1]) : 0}
    visited = {(init[0], init[1])}
    totalCost = 0
    while not len(queue) == 0:
        y, x = queue.pop(0)
        if [y, x] == goal:
            print('totalCost', totalCost)
            return [costs[(y, x)], y, x]
        for i in range(len(delta_name)):
            dY, dX = delta[i]
            newY, newX = y+dY, x+dX
            if newY < len(grid) and newY >=0 and newX < len(grid[0]) and newX >= 0 and grid[newY][newX] == 0 and (newY, newX) not in visited:
                visited.add((newY, newX))
                totalCost += cost
                costs[(newY, newX)] = costs[(y, x)] + cost
                queue += [[newY, newX]]

    return 'fail'

solution = search(grid, init, goal, cost)
print(solution)