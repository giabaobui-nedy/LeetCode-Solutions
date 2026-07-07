class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
    
        # Edge case: start or end is blocked
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        
        # initialise all adjacent directions
        directions = [(-1,-1), (-1,0), (-1,1),
                      (0,-1),           (0,1),
                      (1,-1),  (1,0),   (1,1)]
        
        queue = deque([(0, 0, 1)])  # (row, col, path_length)
        visited = {(0, 0)}
        
        while queue:
            row, col, dist = queue.popleft()
            
            if row == n - 1 and col == n - 1:
                return dist # from the leftest, basically this is when the shortest path wins
            
            for dr, dc in directions: # it is like a sweep circle, to add the neighborhood grid nodes into queue
                r, c = row + dr, col + dc 
                if 0 <= r < n and 0 <= c < n and grid[r][c] == 0 and (r, c) not in visited:
                    visited.add((r, c))
                    queue.append((r, c, dist + 1))
        
        return -1