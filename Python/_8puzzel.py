def is_solvable(state):
    """
    Check if the 8-puzzle is solvable by counting inversions.
    """
    inversion_count = 0
    flat_state = [num for row in state for num in row if num != 0]
    for i in range(len(flat_state)):
        for j in range(i + 1, len(flat_state)):
            if flat_state[i] > flat_state[j]:
                inversion_count += 1
    return inversion_count % 2 == 0

def get_neighbors(state):
    """
    Get all possible moves from the current state.
    """
    neighbors = []
    zero_pos = [(i, j) for i in range(3) for j in range(3) if state[i][j] == 0][0]
    x, y = zero_pos
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def bfs_solve(start, goal):
    """
    Perform BFS to solve the 8-puzzle problem without deque.
    """
    queue = [(start, [])]  # List of (current_state, path)
    visited = set()

    while queue:
        # Get the first element in the queue
        current_state, path = queue.pop(0)
        state_tuple = tuple(tuple(row) for row in current_state)

        if current_state == goal:
            return path + [current_state]

        if state_tuple in visited:
            continue

        visited.add(state_tuple)

        # Add neighbors to the queue
        for neighbor in get_neighbors(current_state):
            if tuple(tuple(row) for row in neighbor) not in visited:
                queue.append((neighbor, path + [current_state]))

    return None  # If no solution is found

def print_puzzle(state):
    """
    Print the 3x3 puzzle grid.
    """
    for row in state:
        print(' '.join(str(num) if num != 0 else '_' for num in row))
    print()

# Define the start and goal states
start_state = [
    [1, 2, 3],
    [4, 0, 5],
    [7, 8, 6]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

if is_solvable(start_state):
    print("Solving the puzzle using BFS:")
    solution = bfs_solve(start_state, goal_state)
    if solution:
        for step in solution:
            print_puzzle(step)
    else:
        print("No solution found.")
else:
    print("The puzzle is unsolvable.")
