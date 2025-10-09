# greedy_core.py
import heapq

def greedy_best_first(start, goal, neighbors_fn, heuristic_fn):
    """
    Greedy Best-First Search genérico.
    """
    frontera = []
    heapq.heappush(frontera, (heuristic_fn(start), start))

    padres = {start: None}
    visitados = set()
    orden_expansion = []

    while frontera:
        _, actual = heapq.heappop(frontera)
        if actual in visitados:
            continue

        orden_expansion.append(actual)

        if actual == goal:
            # reconstruir camino
            camino = []
            while actual is not None:
                camino.append(actual)
                actual = padres[actual]
            camino.reverse()
            return camino, orden_expansion

        visitados.add(actual)

        for v in neighbors_fn(actual):
            if v not in visitados and v not in padres:
                padres[v] = actual
                heapq.heappush(frontera, (heuristic_fn(v), v))

    return None, orden_expansion
