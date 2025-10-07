import heapq

# --- Datos del problema ---
grid = [
    [0, 0, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0],
]
start = (0, 0)
goal  = (4, 6)

# --- Heurística (distancia Manhattan) ---
def h(a, b):
    (r1, c1), (r2, c2) = a, b
    return abs(r1 - r2) + abs(c1 - c2)

# --- Vecinos válidos (4 direcciones) ---
def vecinos(grid, pos):
    r, c = pos
    pasos = [(1,0), (-1,0), (0,1), (0,-1)]
    for dr, dc in pasos:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 0:
            yield (nr, nc)

# --- Greedy Best-First Search ---
def GreedyBestFirst(grid, start, goal):
    frontera = []                                 # PriorityQueue (ordenada por h)
    heapq.heappush(frontera, (h(start, goal), start))
    padres = {start: None}                        # para reconstruir camino
    explorados = set()

    while frontera:
        _, actual = heapq.heappop(frontera)       # saca el de menor h
        if actual == goal:                        # si es el objetivo → fin
            # reconstruir camino
            camino = []
            while actual is not None:
                camino.append(actual)
                actual = padres[actual]
            camino.reverse()
            return camino

        explorados.add(actual)                    # marca como explorado
        for vecino in vecinos(grid, actual):      # expande vecinos
            if vecino not in explorados and vecino not in padres:
                padres[vecino] = actual
                heapq.heappush(frontera, (h(vecino, goal), vecino))

    return None                                   # si no encuentra solución

# --- Ejecutar ---
camino = GreedyBestFirst(grid, start, goal)
if camino:
    print("Camino encontrado:", camino)
    print("Longitud:", len(camino) - 1)
else:
    print("No hay camino posible.")
