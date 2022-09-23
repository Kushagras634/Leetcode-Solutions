class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        @lru_cache(None)
        def recurse(i,j):
            if i==n-1 and j==m-1:
                return 1
            if i>=n or j>=m:
                return 0
            if obstacleGrid[i][j]==1:
                return 0
            return recurse(i,j+1)+recurse(i+1,j)
        if obstacleGrid[-1][-1]==1 or obstacleGrid[0][0]==1:
            return 0
        return recurse(0,0)
        