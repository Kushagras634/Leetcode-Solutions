class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp={}
        def recurse(grid,i,j):
            if i==len(grid)-1 and j==len(grid[0])-1:
                return grid[i][j]
            if i==len(grid) or j==len(grid[0]):
                return float('inf')
            if (i,j) in dp:
                return dp[(i,j)]
            x=recurse(grid,i+1,j)
            y=recurse(grid,i,j+1)
            dp[(i,j)]=grid[i][j]+min(x,y)
            return dp[(i,j)]
        return recurse(grid,0,0)
        