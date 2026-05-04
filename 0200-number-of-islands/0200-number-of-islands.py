class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        num_of_islands = 0

        def dfs(r, c):                          # define BEFORE calling
            if r < 0 or r >= m or c < 0 or c >= n:
                return
            if grid[r][c] != '1':              # check for string '1'
                return
            grid[r][c] = '0'                   # sink the land
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':          # string '1'
                    dfs(r, c)
                    num_of_islands += 1        # consistent name

        return num_of_islands
            

        