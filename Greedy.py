
import heapq
from grid import grid, start, goal   

#manhattan distance 
def distancia(a, b):
    fila1, col1 = a
    fila2, col2 = b
    return abs(fila1 - fila2) + abs(col1 - col2)

#neighbours near the position:up,down,left,right
def obtener_vecinos(grid, posicion):
    fila, col = posicion
    movimientos = [(1,0), (-1,0), (0,1), (0,-1)]
    vecinos = []

    for df, dc in movimientos:
        nf, nc = fila + df, col + dc
        if 0 <= nf < len(grid) and 0 <= nc < len(grid[0]) and grid[nf][nc] == 0:
            vecinos.append((nf, nc))
    return vecinos

# Greedy Algorithm
def greedy_best_first(grid, start, goal):
    frontera = []
    heapq.heappush(frontera, (distancia(start, goal), start))

    padres = {start: None}   
    visitados = set()

    while frontera:
       
        _, actual = heapq.heappop(frontera)

        if actual == goal:
            camino = []
            while actual is not None:
                camino.append(actual)
                actual = padres[actual]
            camino.reverse()
            return camino

        visitados.add(actual)

       
        for vecino in obtener_vecinos(grid, actual):
            if vecino not in visitados and vecino not in padres:
                padres[vecino] = actual
                heapq.heappush(frontera, (distancia(vecino, goal), vecino))

    return None 


#show the grid with the path
def mostrar_camino(grid, camino, start, goal):
    for fila in range(len(grid)):
        for col in range(len(grid[0])):
            pos = (fila, col)
            if pos == start:
                print("S", end=" ")
            elif pos == goal:
                print("G", end=" ")
            elif grid[fila][col] == 1:
                print("-", end=" ")
            elif pos in camino:
                print("*", end=" ")
            else:
                print(".", end=" ")
        print()
    print()



#result
camino = greedy_best_first(grid, start, goal)

if camino:
    print("Camino encontrado:", camino)
    mostrar_camino(grid, camino, start, goal)
    print("Longitud del camino:", len(camino) - 1)
else:
    print("No hay camino posible.")
