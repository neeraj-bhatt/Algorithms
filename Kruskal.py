# Define the graph
graph = {
    'A': [('B', 2), ('C', 3), ('D', 4)],
    'B': [('A', 2), ('E', 3), ('F', 4)],
    'C': [('A', 3), ('G', 4)],
    'D': [('A', 4), ('H', 5)],
    'E': [('B', 3)],
    'F': [('B', 4), ('I', 5), ('J', 6)],
    'G': [('C', 4), ('K', 5)],
    'H': [('D', 5), ('L', 6)],
    'I': [('F', 5)],
    'J': [('F', 6), ('M', 7)],
    'K': [('G', 5)],
    'L': [('H', 6)],
    'M': [('J', 7), ('N', 8)],
    'N': [('M', 8)]
}

def find(parent, node):
    # Find the root of the node's component using path compression
    if parent[node] != node:
        parent[node] = find(parent, parent[node])
    return parent[node]

def union(parent, rank, node1, node2):
    # Merge the components of the two nodes using union by rank
    root1 = find(parent, node1)
    root2 = find(parent, node2)
    
    if rank[root1] < rank[root2]:
        parent[root1] = root2
    elif rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root2] = root1
        rank[root1] += 1

def kruskal(graph):
    edges = []   # Create an empty list to store the edges
    for node in graph:
        for neighbor, weight in graph[node]:
            edges.append((weight, node, neighbor))   # Add each edge to the list
    
    edges.sort()   # Sort the edges by weight in ascending order
    
    parent = {node: node for node in graph}   # Initialize each node as a separate component
    rank = {node: 0 for node in graph}        # Initialize the rank of each component as 0
    mst = []                                   # Create an empty list to store the edges in the MST
    
    for weight, node1, node2 in edges:        # Iterate over the edges in ascending order of weight
        if find(parent, node1) != find(parent, node2):   # If the nodes are not in the same component
            union(parent, rank, node1, node2)   # Merge the components
            mst.append((node1, node2, weight))   # Add the edge to the MST
    
    return mst

# Call the kruskal function with the graph
mst = kruskal(graph)
print(mst)
