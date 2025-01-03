import collections

# BFS algorithm
def bfs(graph, root):
    visited, queue = set(), collections.deque([root]) 
    visited.add(root) 
    
    while queue:
        # Dequeue a vertex from queue 
        vertex = queue.popleft()
        print(str(vertex) + " ", end=" ")
        
        # Iterate through the neighbors of the dequeued vertex
        for neighbour in graph[vertex]: 
            if neighbour not in visited: 
                visited.add(neighbour) 
                queue.append(neighbour)

if __name__ == '__main__': 
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]} 
    print("Following is Breadth First Traversal: ") 
    bfs(graph, 0)
