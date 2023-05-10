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

def dfs(graph, start, visited=set()):
    visited.add(start)  # Mark the starting node as visited
    print(start)    # Do something with the node (e.g. print it)
    
    for neighbor in graph[start]:   # Iterate over the neighbors of the node
        if neighbor not in visited:     # If the neighbor hasn't been visited yet
            dfs(graph, neighbor, visited)      # Recursively call DFS on the neighbor

# Call the DFS function with the graph and starting node
dfs(graph, 'A')
