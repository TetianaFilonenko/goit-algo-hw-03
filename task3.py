def move(n, source, target, auxiliary, rods):
    if n == 1:
        rods[target].append(rods[source].pop())
        print(f"Move disk from {source} to {target}: {rods[target][-1]}")
        print(f"Current state: {rods}")
        return
    move(n-1, source, auxiliary, target, rods)
    rods[target].append(rods[source].pop())
    print(f"Move disk from {source} to {target}: {rods[target][-1]}")
    print(f"Current state: {rods}")
    move(n-1, auxiliary, target, source, rods)

n = 3  # Number of disks
rods = {
    'A': list(range(n, 0, -1)),  # Larger numbers represent larger disks
    'B': [],
    'C': []
}
print(f"Initial state: {rods}")
move(n, 'A', 'C', 'B', rods)
