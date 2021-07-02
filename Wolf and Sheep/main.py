import numpy as np


def find_path(residual):
    size = residual.shape[0]
    visited = [0]
    q = [0]
    prev = [-1 for _ in range(size)]
    while q:
        cur = q.pop()
        for dest in range(size):
            if dest not in visited and residual[cur, dest] > 0:
                q.append(dest)
                visited.append(dest)
                prev[dest] = cur
                if dest == size - 1:
                    path = [dest]
                    node = dest
                    while node != 0:
                        path.insert(0, prev[node])
                        node = prev[node]
                    return path
    return False


def augment(res_graph, path):
    length = len(path)
    for i in range(length - 1):
        start = path[i]
        end = path[i + 1]
        res_graph[start, end] = False
        res_graph[end, start] = True
    return res_graph


def safe_paths(res_graph, adjacency):
    flow = res_graph.T & adjacency
    for end in range(flow.shape[0]):
        cur = 0
        path = [0]
        if flow[cur, end]:
            path.append(end)
            cur = end
            while cur != flow.shape[0] - 1:
                end = np.argwhere(flow[cur, :] == 1)[0][0]
                path.append(end)
                cur = end
            print(path)


def wolf_sheep(adjacency):
    res_graph = np.copy(adjacency)

    n_found = 0
    path = find_path(res_graph)
    while n_found < 2 and path:
        res_graph = augment(res_graph, path)
        path = find_path(res_graph)
        n_found += 1
    if n_found == 2:
        safe_paths(res_graph, adjacency)
        return True
    else:
        return False


if __name__ == '__main__':
    n = int(input())
    adj = np.zeros((n, n), dtype=bool)

    # Vertices 1 and n are s and t respectively
    inp = input()
    while inp != 'end':
        u, v = list(map(int, inp.split()))
        if 1 <= u <= n and 1 <= v <= n:
            adj[u - 1, v - 1] = 1
            inp = input()
        else:
            inp = input('Invalid input. Try again.')

    if not wolf_sheep(adj):
        print("Sorry sheep :(")
