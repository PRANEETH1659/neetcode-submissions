from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        queue=deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j]==0:
                    queue.append((i,j))
        
    
        while queue:

            i,j = queue.popleft()

            drs=[(0,1),(0,-1),(1,0),(-1,0)]

            for x,y in drs:
                    nx=i+x
                    ny=j+y
                    if 0<=nx<len(grid) and 0<=ny <len(grid[0]) and grid[nx][ny]==2147483647:
                        grid[nx][ny]=grid[i][j]+1
                        queue.append((nx,ny))

        