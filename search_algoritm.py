
from collections import deque

def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]

    # Antrian pencarian dari dua arah
    queue_start = deque([start])
    queue_goal = deque([goal])

    # Menyimpan jalur yang sudah dikunjungi
    visited_start = {start: None}
    visited_goal = {goal: None}

    while queue_start and queue_goal:

        # Pencarian dari titik awal
        current = queue_start.popleft()

        for neighbor in graph[current]:
            if neighbor not in visited_start:
                visited_start[neighbor] = current
                queue_start.append(neighbor)

                if neighbor in visited_goal:
                    return build_path(
                        neighbor, visited_start, visited_goal
                    )

        # Pencarian dari titik tujuan
        current = queue_goal.popleft()

        for neighbor in graph[current]:
            if neighbor not in visited_goal:
                visited_goal[neighbor] = current
                queue_goal.append(neighbor)

                if neighbor in visited_start:
                    return build_path(
                        neighbor, visited_start, visited_goal
                    )

    return None


def build_path(meeting, visited_start, visited_goal):
    # Susun jalur dari awal menuju titik pertemuan
    path_start = []
    node = meeting

    while node is not None:
        path_start.append(node)
        node = visited_start[node]

    path_start.reverse()

    # Susun jalur dari titik pertemuan menuju tujuan
    path_goal = []
    node = visited_goal[meeting]

    while node is not None:
        path_goal.append(node)
        node = visited_goal[node]

    return path_start + path_goal


# Contoh graf
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'G'],
    'E': ['B', 'G'],
    'F': ['C', 'G'],
    'G': ['D', 'E', 'F']
}

start = 'A'
goal = 'G'

result = bidirectional_search(graph, start, goal)

if result:
    print("Jalur ditemukan:", " -> ".join(result))
    print("Jumlah langkah:", len(result) - 1)
else:
    print("Jalur tidak ditemukan")
