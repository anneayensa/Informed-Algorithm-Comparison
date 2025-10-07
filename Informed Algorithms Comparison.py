import math

# ============================
#   Definición del grid
# ============================
# 0 = libre, 1 = obstáculo
grid = [
    [0, 0, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0],
]

start = (0, 0)
goal = (4, 6)

# ============================
#   Funciones auxiliares
# ============================

def manhattan(a, b):
    """Heurística: distancia Manhattan."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def vecinos(node):
    """Devuelve los vecinos válidos (sin salir del grid ni pasar por obstáculos)."""
    x, y = node
    moves = [(-1,0), (1,0), (0,-1), (0,1)]
    result = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
            result.append((nx, ny))
    return result

# ============================
#   Algoritmo IDA*
# ============================

def ida_star(start, goal):
    """Implementación de IDA*."""
    threshold = manhattan(start, goal)
    path = [start]
    visited = set()

    while True:
        temp = search(path, 0, threshold, goal, visited)
        if isinstance(temp, list):  # Encontró el camino
            return temp
        if temp == math.inf:
            return None  # No hay solución
        threshold = temp  # Aumentar límite

def search(path, g, threshold, goal, visited):
    """Búsqueda recursiva limitada por f = g + h."""
    node = path[-1]
    f = g + manhattan(node, goal)
    if f > threshold:
        return f
    if node == goal:
        return list(path)
    
    minimum = math.inf
    for succ in vecinos(node):
        if succ not in path:
            path.append(succ)
            temp = search(path, g + 1, threshold, goal, visited)
            if isinstance(temp, list):
                return temp
            if temp < minimum:
                minimum = temp
            path.pop()
    return minimum

# ============================
#   Ejecución y resultados
# ============================

camino = ida_star(start, goal)

if camino:
    print("✅ Camino encontrado por IDA*:")
    print(camino)
    print(f"Longitud del camino: {len(camino)-1}")

    # Visualización del grid con el camino
    for i in range(len(grid)):
        row = ""
        for j in range(len(grid[0])):
            if (i, j) == start:
                row += "S "
            elif (i, j) == goal:
                row += "G "
            elif (i, j) in camino:
                row += "· "
            elif grid[i][j] == 1:
                row += "█ "
            else:
                row += "  "
        print(row)
else:
    print("❌ No se encontró ningún camino.")
