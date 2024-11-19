def bfs(matrix, nodes_to_explore, visited):
    if not nodes_to_explore:
        return  # Base case: no more nodes to explore

    # Visit all nodes at the current level
    next_level = []
    for node in nodes_to_explore:
        if node not in visited:
            print(node, end=' ')  # Print the node as we visit it
            visited.add(node)  # Mark it as visited
            
            # Add neighbors of the current node to the next level
            for neighbor, is_connected in enumerate(matrix[node]):
                if is_connected and neighbor not in visited:
                    next_level.append(neighbor)

    # Recursive call for the next level
    bfs(matrix, next_level, visited)

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

# Start BFS from node 0
start_node = 0
visited = set()
print("BFS traversal starting from node 0:")
bfs(graph_matrix, [start_node], visited)
