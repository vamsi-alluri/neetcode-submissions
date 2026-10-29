class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = len(board[0])
        c = len(board)
        r_sets = [set() for _ in range(9)]
        c_sets = [set() for _ in range(9)]
        box_sets = [set() for _ in range(9)]

        for i in range(r):
            for j in range(c):
                curr = board[i][j]
                if board[i][j] == '.':
                    continue

                if board[i][j] in r_sets[j]:
                    return False
                if board[i][j] in c_sets[i]:
                    return False
                square = ((i//3) * 3) + (j // 3)
                if board[i][j] in box_sets[square]:
                    return False
                
                r_sets[j].add(curr)
                c_sets[i].add(curr)
                box_sets[square].add(curr)

        return True