class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        index = 0
        word_len = len(word)


        def backt(i, j, index):
            print(i, j, index)
            if i > row - 1 or j > col - 1 or i < 0 or j < 0:
                return False

            if index > word_len - 1:
                return False
            elif index == word_len:
                return True
            
            revert = board[i][j]
            if board[i][j] == word[index]:  
                board[i][j] = '#'
                index += 1
            else:
                return False


            res = backt(i-1, j, index) or backt(i, j+1, index) or backt(i+1, j, index) or backt(i, j-1, index)
            board[i][j] = revert
            return res
        

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[index]:
                    if backt(i, j, index):
                        return True
        return False




