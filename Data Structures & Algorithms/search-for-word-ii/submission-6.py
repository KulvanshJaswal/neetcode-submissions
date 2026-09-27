class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.is_word = False

        class Trie:
            def __init__(self):
                self.root = TrieNode()

            def insert(self, word):
                node = self.root
                for letter in word:
                    if letter not in node.children:
                        node.children[letter] = TrieNode()
                    node = node.children[letter]
                node.is_word = True

        ans = set()

        def backtrack(i, j, node, used, temp):
            if node.is_word and temp not in ans:
                ans.add(temp)

            if not node.children:
                return

            directions = [(-1,0), (0,1), (1,0), (0,-1)]
            for di, dj in directions:
                ni, nj = i + di, j + dj

                if (ni >= 0 and ni < len(board)) and (nj >= 0 and nj < len(board[0])) and (ni,nj) not in used and board[ni][nj] in node.children:
                    used.add((ni,nj))
                    backtrack(ni,nj,node.children[board[ni][nj]],used,temp + board[ni][nj])
                    used.discard((ni,nj))

                    if not node.children[board[ni][nj]].children:
                        del node.children[board[ni][nj]]
        
        rows = len(board)
        cols = len(board[0])

        trie = Trie()
        for word in words:
            trie.insert(word)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] in trie.root.children:
                    backtrack(i, j, trie.root.children[board[i][j]], {(i,j)}, "" + board[i][j])
                    
        return list(ans)
                
            
            