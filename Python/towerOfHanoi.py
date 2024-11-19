def tower_of_hanoi(n, source, destination, auxiliary):
    """
    Solve the Tower of Hanoi problem using recursion.
    
    :param n: Number of disks
    :param source: The source peg (from where disks need to be moved)
    :param destination: The destination peg (where disks need to be moved)
    :param auxiliary: The auxiliary peg (used for intermediate storage)
    """
    # Base case: If there is only one disk, move it from source to destination
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    
    # Move n-1 disks from source to auxiliary, using destination as auxiliary
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    
    # Move the nth disk from source to destination
    print(f"Move disk {n} from {source} to {destination}")
    
    # Move n-1 disks from auxiliary to destination, using source as auxiliary
    tower_of_hanoi(n - 1, auxiliary, destination, source)

# Driver code to test the solution
n = 3  # Number of disks
tower_of_hanoi(n, 'A', 'C', 'B')  # A, B, C are the names of the pegs
