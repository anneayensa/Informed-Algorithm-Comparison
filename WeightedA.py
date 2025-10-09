import heapq
from graph2 import graph, start, goal, h_values  

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
    """Devuelve nodos hijos y sus costos según las conexiones del grafo"""
    children = []
    for neighbor, cost in graph.get(node.state, {}).items():
        g_new = node.g + cost
        h_new = h_values.get(neighbor, float('inf'))
        children.append(Node(neighbor, parent=node, g=g_new, h=h_new))
    return children


def WeightedAStar(problem_start, problem_goal, w1=1, w2=1):
    start_node = Node(problem_start, g=0, h=h_values.get(problem_start, float('inf')))
    frontier = []
    heapq.heappush(frontier, (start_node.f(w1, w2), start_node))
    explored = set()
    nodes_expanded = 0

    while frontier:
        _, node = heapq.heappop(frontier)
        nodes_expanded += 1

        if node.state == problem_goal:
            path = []
            total_cost = node.g
            while node:
                path.append(node.state)
                node = node.parent
            return path[::-1], total_cost, nodes_expanded

        explored.add(node.state)

        for child in expand(node):
            if child.state in explored:
                continue

            in_frontier = next((item for _, item in frontier if item.state == child.state), None)
            if not in_frontier:
                heapq.heappush(frontier, (child.f(w1, w2), child))
            elif child.f(w1, w2) < in_frontier.f(w1, w2):
                frontier.remove((in_frontier.f(w1, w2), in_frontier))
                heapq.heapify(frontier)
                heapq.heappush(frontier, (child.f(w1, w2), child))

    return None, float('inf'), nodes_expanded


if __name__ == "__main__":
    w1, w2 = 1.0, 2.0  
    path, cost, expanded = WeightedAStar(start, goal, w1, w2)

    print(f"Weighted A*: w1={w1}, w2={w2}")
    if path:
        print(f"Path found (cost {cost}): {' → '.join(path)}")
    else:
        print("No path found.")
    print(f"Nodes expanded: {expanded}")




