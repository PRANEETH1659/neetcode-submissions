class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        m=len(grid[0])
        n=len(grid)

        visited=[[False for _ in range(m)] for _ in range(n)]


        for i in range(m):

            if grid[0][i]==1:
                self.dfs(0,i,visited,grid)

        for i in range(m):

            if grid[n-1][i]==1:
                self.dfs(n-1,i,visited,grid)
        
        for i in range(n):

            if grid[i][0]==1:
                self.dfs(i,0,visited,grid)
        
        for i in range(n):

            if grid[i][m-1]==1:
                self.dfs(i,m-1,visited,grid)
        
        count=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and not visited[i][j]:
                    count+=1
        
        return count
    
    def dfs(self,i,j,visited,grid):

        if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or visited[i][j] or grid[i][j]==0:
            return 
        
        visited[i][j]=1 

        drs=[(0,1),(0,-1),(1,0),(-1,0)]

        for x,y in drs:
            self.dfs(i+x,j+y,visited,grid)