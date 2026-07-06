class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        m=len(board[0])
        n=len(board)
        visited=[[False for _ in range(m)] for  _ in range(n)]
        for i in range(m):
            if board[0][i]=="O":
                self.dfs(0,i,visited,board)
            
        for i in range(m):
            if board[n-1][i]=="O":
                self.dfs(n-1,i,visited,board)
        

        for i in range(n):
            if board[i][0]=="O":
                self.dfs(i,0,visited,board)
            
        for i in range(n):
            if board[i][m-1]=="O":
                self.dfs(i,m-1,visited,board)
        

        for i in range(n):
            for j in range(m):
                if board[i][j]=="O" and not visited[i][j]:
                    board[i][j]="X"
        
    
    def dfs(self,i,j,visited,board):

        if i<0 or i>=len(board) or j <0 or j>=len(board[0]) or visited[i][j] or board[i][j]=="X":
            return 
        
        visited[i][j]=True

        drs=[(0,1),(0,-1),(1,0),(-1,0)]

        for x,y in drs:
            self.dfs(i+x,j+y,visited,board)