class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def backtrack(i, j, target, used):
            if target == len(word):
                return True

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for di, dj in directions:
                ni, nj = i + di, j + dj
                if (ni >= 0 and ni < len(board)) and (nj >= 0 and nj < len(board[0])) and (ni,nj) not in used and board[ni][nj] == word[target]:
                    used.add((ni, nj))
                    found = backtrack(ni, nj, target + 1, used)
                    used.discard((ni, nj))
                    if found:
                        return True

            return False
        
        if board[0][0] == word:
            return True
        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0, set()):
                    return True
        return False