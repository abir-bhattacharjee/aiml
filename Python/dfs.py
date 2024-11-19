def dfs(matrix, start, visited=None):
    if visited is None:
        visited = set()  # To keep track of visited nodes

    visited.add(start)
    print(start, end=' ')  # Print the node as we visit it

    # Loop through neighbors using the adjacency matrix
    for neighbor, is_connected in enumerate(matrix[start]):
        if is_connected and neighbor not in visited:
            dfs(matrix, neighbor, visited)

# Example graph (adjacency matrix representation)
# Graph:  0 -> 1, 0 -> 2, 1 -> 3, 1 -> 4, 2 -> 5
graph_matrix = [
    [0, 1, 1, 0, 0, 0],  # Node 0
    [0, 0, 0, 1, 1, 0],  # Node 1
    [0, 0, 0, 0, 0, 1],  # Node 2
    [0, 0, 0, 0, 0, 0],  # Node 3
    [0, 0, 0, 0, 0, 0],  # Node 4
    [0, 0, 0, 0, 0, 0],  # Node 5
]

# Perform DFS starting from node 0
dfs(graph_matrix, 0)
