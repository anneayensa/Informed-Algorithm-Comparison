import math

# Change mode GRAPH to GRID if you want to use a grid
MODE = "GRAPH" 

if MODE == "GRID":
    import grid
    start = grid.start
    goal = grid.goal
    grid_data = grid.grid
elif MODE == "GRAPH":
    import graph
    start = graph.start
    goal = graph.goal
    g_graph = graph.graph
    h_values = graph.h_values
else:
    raise ValueError("MODE debe ser 'GRID' o 'GRAPH'")

FOUND = object()

def h(node):
    if MODE == "GRID":
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])
    else:
        return h_values.get(node, 0)

def expand(node):
    neighbors = []
    if MODE == "GRID":
        x, y = node
        moves = [(-1,0),(1,0),(0,-1),(0,1)]
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid_data) and 0 <= ny < len(grid_data[0]) and grid_data[nx][ny] == 0:
                neighbors.append((nx, ny))
    else:
        neighbors = list(g_graph.get(node, {}).keys())
    return neighbors

def cost(node1, node2):
    if MODE == "GRID":
        return 1
    else:
        return g_graph[node1][node2]

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
            temp = Search(child, g + cost(node, child), threshold, path, visited)
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

if __name__ == "__main__":
    camino = IDAStar()

    if camino:
        print("✅ Path found by IDA*:")
        print(camino)
        print(f"Path length: {len(camino)-1}")

        if MODE == "GRID":
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
