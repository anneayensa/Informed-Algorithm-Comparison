import math
import grid

def h(node):
    goal = grid.goal
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def expand(node):
    x, y = node
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    neighbors = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid.grid) and 0 <= ny < len(grid.grid[0]) and grid.grid[nx][ny] == 0:
            neighbors.append((nx, ny))
    return neighbors

def cost(node1, node2):
    return 1

FOUND = object()

def Search(node, g, threshold, path):
    f = g + h(node)
    if f > threshold:
        return f
    if node == grid.goal:
        return FOUND
    
    min_exceed = math.inf
    for child in expand(node):
        if child not in path: 
            path.append(child)
            temp = Search(child, g + cost(node, child), threshold, path)
            if temp is FOUND:
                return FOUND
            if temp < min_exceed:
                min_exceed = temp
            path.pop()
    return min_exceed

def IDAStar():
    threshold = h(grid.start)
    path = [grid.start]

    while True:
        temp = Search(grid.start, 0, threshold, path)
        if temp is FOUND:
            return path
        if temp == math.inf:
            return None
        threshold = temp

camino = IDAStar()

if camino:
    print("✅ Path found by IDA*:")
    print(camino)
    print(f"Path length: {len(camino)-1}")


    for i in range(len(grid.grid)):
        row = ""
        for j in range(len(grid.grid[0])):
            if (i, j) == grid.start:
                row += "S "
            elif (i, j) == grid.goal:
                row += "G "
            elif (i, j) in camino:
                row += "· "
            elif grid.grid[i][j] == 1:
                row += "█ "
            else:
                row += "  "
        print(row)
else:
    print("❌ No se encontró ningún camino.")
