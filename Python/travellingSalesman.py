import itertools

# Define the distance matrix (Example: symmetric TSP problem)
# Distance between each pair of cities
# Example with 4 cities
distance_matrix = [
    [0, 10, 15, 20],  # Distances from City 0 to other cities
    [10, 0, 35, 25],  # Distances from City 1 to other cities
    [15, 35, 0, 30],  # Distances from City 2 to other cities
    [20, 25, 30, 0],  # Distances from City 3 to other cities
]

# Function to calculate the total distance of a given route
def calculate_total_distance(route, distance_matrix):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance_matrix[route[i]][route[i+1]]
    total_distance += distance_matrix[route[-1]][route[0]]  # Return to the start city
    return total_distance

# Function to solve the TSP using brute force
def travelling_salesman_bruteforce(distance_matrix):
    num_cities = len(distance_matrix)
    cities = list(range(num_cities))  # List of city indices (0, 1, 2, ...)
    
    # Generate all possible permutations of the cities (except the start city)
    possible_routes = itertools.permutations(cities)
    
    # Initialize the minimum distance to a large number
    min_distance = float('inf')
    best_route = None
    
    # Check all possible routes
    for route in possible_routes:
        # Calculate the total distance for this route
        current_distance = calculate_total_distance(route, distance_matrix)
        
        # If the current distance is smaller than the minimum distance, update
        if current_distance < min_distance:
            min_distance = current_distance
            best_route = route
    
    return best_route, min_distance

# Solve the TSP problem using brute force
best_route, min_distance = travelling_salesman_bruteforce(distance_matrix)

# Print the result
print("Optimal Route:", best_route)
print("Minimum Distance:", min_distance)
