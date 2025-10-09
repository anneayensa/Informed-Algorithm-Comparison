import math
import grid

goal = grid.goal
grid_data = grid.grid
start = grid.start

def h(node):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def expand(node):
    x, y = node
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    neighbors = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid_data) and 0 <= ny < len(grid_data[0]) and grid_data[nx][ny] == 0:
            neighbors.append((nx, ny))
    return neighbors

FOUND = object()

def Search(node, g, threshold, path, visited):
    f = g + h(node)
    if f > threshold:
        return f
    if node == goal:
        return FOUND
    
    min_exceed = math.inf
    for child in expand(node):
        if child not in visited:
            path.append(child)
            visited.add(child)
            temp = Search(child, g + 1, threshold, path, visited)
            if temp is FOUND:
                return FOUND
            if temp < min_exceed:
                min_exceed = temp
            path.pop()
            visited.remove(child)
    return min_exceed

def IDAStar():
    threshold = h(start)
    path = [start]
    visited = {start}

    while True:
        temp = Search(start, 0, threshold, path, visited)
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

    for i, row in enumerate(grid_data):
        print("".join(
            "S " if (i, j) == start else
            "G " if (i, j) == goal else
            "* " if (i, j) in camino else
            "█ " if cell == 1 else
            "· "
            for j, cell in enumerate(row)
        ))
else:
    print("❌ No se encontró ningún camino.")
