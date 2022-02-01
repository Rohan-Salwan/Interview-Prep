class Solution:
    def solver(self,aa,a,b):
        if a>=len(aa) or b >= len(aa[a]) or a<0 or b<0 or aa[a][b]=="X" or aa[a][b]=="1":
            return
        if aa[a][b]=="O":
            aa[a][b]="1"
        self.solver(aa,a+1,b) or self.solver(aa,a,b+1) 
        self.solver(aa,a-1,b) or self.solver(aa,a,b-1)
    def solve(self, board: List[List[str]]) -> None:
        j=i=0
        while i<len(board):
            if board[i][j]=="O":
                self.solver(board,i,j)
            if i+1==len(board):
                while j<len(board[i]):
                    if board[i][j]=="O":
                        self.solver(board,i,j)
                    j+=1
            i+=1
        j=i=0
        while j<len(board[i]):
            if board[i][j]=="O":
                self.solver(board,i,j)
            if j+1==len(board[i]):
                while i<len(board):
                    if board[i][j]=="O":
                        self.solver(board,i,j)
                    i+=1
                i=0
            j+=1
        i=0
        while i<len(board):
            j=0
            while j<len(board[i]):
                if board[i][j]=="O":
                    board[i][j]="X"
                if board[i][j]=="1":
                    board[i][j]="O"
                j+=1           
            i+=1