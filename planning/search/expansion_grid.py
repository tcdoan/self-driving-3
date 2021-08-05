grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
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
    pq = [[0, init[0], init[1]]]
    visited = {tuple(init)}
    costs = {tuple(init):0}
    numVisited = 0

    expanded = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    expanded[init[0]][init[1]] = 0

    while len(pq) != 0:
        pq.sort()
        oldCost, currY, currX = pq.pop(0)
        if [currY, currX] == goal:
            print(numVisited)
            print([oldCost, currY, currX])
        for [dY, dX] in delta: 
            newY, newX = (currY+dY, currX+dX)
            if (newY, newX) not in visited and inBounds(grid, (newY, newX)):
                visited.add((newY, newX))
                numVisited += 1
                expanded[newY][newX] = numVisited
                costs[(newY, newX)] = costs[(currY, currX)] + cost
                pq.append([costs[(newY, newX)], newY, newX])

    return expanded

expanded = search(grid, init, goal, cost)
for i in range(len(expanded)):
    print(expanded[i])