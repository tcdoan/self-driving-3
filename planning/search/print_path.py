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
    pq = [[0, init[0], init[1]]]
    visited = {tuple(init):''}
    costs = {tuple(init):0}
    numVisited = 0

    while len(pq) != 0:
        pq.sort()
        oldCost, currY, currX = pq.pop(0)
        if [currY, currX] == goal:
            print(numVisited)
            print([oldCost, currY, currX])
            
            path = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
            symbol = '*'
            path[currY][currX] = symbol
            while visited[(currY, currX)] is not '':
                currY, currX, symbol = visited[(currY, currX)]
                path[currY][currX] = symbol
            return path
        for i in range(len(delta)): 
            dY, dX = delta[i]
            newY, newX = (currY+dY, currX+dX)
            if (newY, newX) not in visited and inBounds(grid, (newY, newX)):
                visited[(newY, newX)] = [currY, currX, delta_name[i]]
                numVisited += 1
                costs[(newY, newX)] = costs[(currY, currX)] + cost
                pq.append([costs[(newY, newX)], newY, newX])

    return None

path = search(grid, init, goal, cost)
if path is not None:
    for i in range(len(path)):
        print(path[i])
else: 
    print('No path found')

print()

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
path = search(grid, init, goal, cost)
if path is not None:
    for i in range(len(path)):
        print(path[i])
else: 
    print('No path found')