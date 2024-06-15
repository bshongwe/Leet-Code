class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        # Step 1: Create adjacency list representation of the graph
        adj = defaultdict(list)
        degree = [0] * n
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1
        
        # Step 2: Initialize queue with leaf nodes (degree == 1)
        queue = deque()
        for i in range(n):
            if degree[i] == 1:
                queue.append(i)
        
        remaining_nodes = n
        while remaining_nodes > 2:
            current_size = len(queue)
            remaining_nodes -= current_size
            
            for _ in range(current_size):
                leaf = queue.popleft()
                for neighbor in adj[leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        queue.append(neighbor)
        
        # Whatever is left in the queue are the roots of MHTs
        return list(queue)
