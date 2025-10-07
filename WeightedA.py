import grid
import heapq


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h

    def f(self, w1, w2):
        return w1 * self.g + w2 * self.h

    def __lt__(self, other):
        return self.f(1, 1) < other.f(1, 1)


def expand(node):
    children = []
    r, c = node.state
    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 0:
            g_new = node.g + 1
            h_new = heuristic((nr, nc), goal)
            children.append(Node((nr, nc), parent=node, g=g_new, h=h_new))
    return children


def AStarSearch (problem_start, problem_goal, w1=1, w2=1):
    start_node = Node(problem_start, g=0, h=heuristic(problem_start, problem_goal))

    frontier = []
    heapq.heappush(frontier, (start_node.f(w1, w2), start_node))

    explored = set()
    nodes_expanded = 0

    while frontier:
        _, node = heapq.heappop(frontier)
        nodes_expanded += 1

        if node.state == problem_goal:
            path = []
            while node:
                path.append(node.state)
                node = node.parent
            path.reverse()
            return path, nodes_expanded

        explored.add(node.state)

        for child in expand(node):
            if child.state in explored:
                continue
            in_frontier = next((item for _, item in frontier if item.state == child.state), None)

            if not in_frontier:
                heapq.heappush(frontier, (child.f(w1, w2), child))
            else:
                if child.f(w1, w2) < in_frontier.f(w1, w2):
                    frontier.remove((in_frontier.f(w1, w2), in_frontier))
                    heapq.heapify(frontier)
                    heapq.heappush(frontier, (child.f(w1, w2), child))

    return None, nodes_expanded


w1, w2 = 1.0, 2.0
path, expanded = AStarSearch(start, goal, w1, w2)

print(f"Weighted A* con w1={w1}, w2={w2}")
if path:
    print(f"Camino encontrado ({len(path)} pasos):")
    print(path)
else:
    print("No se encontró camino.")
print(f"Nodos explorados: {expanded}")


def show_path(path):
    grid_copy = [row[:] for row in grid]
    for r, c in path:
        if (r, c) != start and (r, c) != goal:
            grid_copy[r][c] = '*'
    for row in grid_copy:
        print(' '.join(str(x) for x in row))
    print()

if path:
    show_path(path)


