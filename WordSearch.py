class Solution:
    def exist(self, board: List[List[str]], word: str,i=0,j=0) -> bool:
        result=False
        i=0
        while i < len(board):
            j=0
            while j < len(board[i]):
                if board[i][j]==word[0]:
                    pos=0
                    result=self.bhai(board,word,i,j,pos)
                    if result==True:
                        return True
                        break
                j+=1
            if result==True:
                break
            i+=1
    def bhai(self,board,word,i,j,pos):
        if len(word)==pos:
            return True
        if i >= len(board) or i < 0 or j >= len(board[0]) or j < 0  or board[i][j]!=word[pos]:
            return False
        temp=board[i][j]
        board[i][j]='#'
        if self.bhai(board,word,i,j+1,pos+1):
            board[i][j]=temp
            return True
        if self.bhai(board,word,i+1,j,pos+1):
            board[i][j]=temp
            return True
        if self.bhai(board,word,i-1,j,pos+1):
            board[i][j]=temp
            return True
        if self.bhai(board,word,i,j-1,pos+1):
            board[i][j]=temp
            return True
        board[i][j]=temp
        return False