# bfs 
def bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            print(node, end= " ")
            queue.extend(graph[node] - visited)

# graph .. 
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(graph, 'A')

# bfs with path
def bfs_path(graph, start, end):
    visited = set()
    queue = [(start, [start])]
    while queue:
        node, path = queue.pop(0)
        if node not in visited:
            visited.add(node)
            if node == end:
                return path
            for neighbor in graph[node]:
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))
    return None

print(bfs_path(graph, 'A', 'E'))

# bfs with path and weight
def bfs_weight(graph, start, end):
    visited = {}
    queue = [(start, 0, [start])]
    while queue:
        node, weight, path = queue.pop(0)
        if node not in visited or weight < visited[node]:
            visited[node] = weight
            if node == end:
                return path, weight
            for neighbor, cost in graph[node].items():
                new_weight = weight + cost
                new_path = path + [neighbor]
                queue.append((neighbor, new_weight, new_path))
    return None, float('inf')

print(bfs_weight(graph, 'A', 'E'))

# dijkstra
import heapq

def dijkstra(graph, start):
    visited = {node: float('inf') for node in graph}
    visited[start] = 0
    queue = [(0, start)]
    while queue:
        weight, node = heapq.heappop(queue)
        if visited[node] < weight:
            continue
        for neighbor, cost in graph[node].items():
            new_weight = weight + cost
            if new_weight < visited[neighbor]:
                visited[neighbor] = new_weight
                heapq.heappush(queue, (new_weight, neighbor))
    return visited

print(dijkstra(graph, 'A'))

# dijkstra with path
def dijkstra_path(graph, start, end):
    visited = {node: float('inf') for node in graph}
    visited[start] = 0
    path = {node: [] for node in graph}
    path[start] = [start]
    queue = [(0, start)]
    while queue:
        weight, node = heapq.heappop(queue)
        if visited[node] < weight:
            continue
        for neighbor, cost in graph[node].items():
            new_weight = weight + cost
            if new_weight < visited[neighbor]:
                visited[neighbor] = new_weight
                path[neighbor] = path[node] + [neighbor]
                heapq.heappush(queue, (new_weight, neighbor))
    return path[end]

print(dijkstra_path(graph, 'A', 'E'))

# a* search
import heapq

def heuristic_cost(node1, node2):
    # For demo purposes, using a dummy heuristic (Manhattan-like distance)
    # You need coordinates for actual heuristic; here's a placeholder
    return abs(ord(node1) - ord(node2))


def a_star(graph, start, end):
    visited = {}
    queue = [(0 + heuristic_cost(start, end), 0, start, [start])]
    
    while queue:
        estimated_total, cost_so_far, node, path = heapq.heappop(queue)

        if node == end:
            return path, cost_so_far

        if node in visited and cost_so_far >= visited[node]:
            continue

        visited[node] = cost_so_far

        for neighbor, cost in graph[node].items():
            new_cost = cost_so_far + cost
            new_path = path + [neighbor]
            est_total = new_cost + heuristic_cost(neighbor, end)
            heapq.heappush(queue, (est_total, new_cost, neighbor, new_path))

    return None, float('inf')

print(a_star(graph, 'A', 'E'))
