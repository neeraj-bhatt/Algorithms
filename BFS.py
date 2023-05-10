from collections import deque

# Define the graph
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['H'],
    'E': [],
    'F': ['I', 'J'],
    'G': ['K'],
    'H': ['L'],
    'I': [],
    'J': ['M'],
    'K': [],
    'L': [],
    'M': ['N'],
    'N': []
}

def bfs(graph, start):
    visited = set()     # Create an empty set to keep track of visited nodes
    queue = deque([start])  # Create a queue and add the starting node
    visited.add(start)  # Mark the starting node as visited
    
    while queue:    # Loop until the queue is empty
        node = queue.popleft()  # Get the next node from the queue
        
        print(node)     # Do something with the node (e.g. print it)
        
        for neighbor in graph[node]:   # Iterate over the neighbors of the node
            if neighbor not in visited:     # If the neighbor hasn't been visited yet
                visited.add(neighbor)       # Mark it as visited
                queue.append(neighbor)      # Add it to the queue

# Call the BFS function with the graph and starting node
bfs(graph, 'A')
