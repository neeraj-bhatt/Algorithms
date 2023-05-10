import heapq

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

def prim(graph, start):
    # Initialize the heap with the edges connected to the starting node
    heap = [(weight, start, neighbor) for neighbor, weight in graph[start]]
    heapq.heapify(heap)
    
    visited = set()     # Create an empty set to keep track of visited nodes
    visited.add(start)  # Mark the starting node as visited
    mst = []            # Create an empty list to store the edges in the MST
    
    while heap:     # Loop until the heap is empty
        weight, node1, node2 = heapq.heappop(heap)    # Get the edge with the smallest weight
        
        if node2 not in visited:    # If the second node is not visited
            visited.add(node2)      # Mark it as visited
            mst.append((node1, node2, weight))    # Add the edge to the MST
            
            # Add the edges connected to the new node to the heap
            for neighbor, weight in graph[node2]:
                if neighbor not in visited:
                    heapq.heappush(heap, (weight, node2, neighbor))
    
    return mst

# Call the prim function with the graph and starting node
mst = prim(graph, 'A')
print(mst)
