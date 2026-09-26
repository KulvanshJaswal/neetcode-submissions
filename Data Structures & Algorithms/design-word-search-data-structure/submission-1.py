class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        d = self.trie

        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]

        d["."] = "."

    def search(self, word: str) -> bool:
        def search2(node, index):
            if index == len(word) and "." in node:
                return True
            if index == len(word):
                return False

            if word[index] == ".":
                for key, child in node.items():
                    if key == ".":
                        continue
                    if search2(child, index + 1):
                        return True
                return False
            else:
                if word[index] in node:
                    return search2(node[word[index]], index + 1)
                return False
            

        d = self.trie

        return search2(d, 0)

