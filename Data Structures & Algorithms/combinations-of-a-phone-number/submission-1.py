class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []
        
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        ans = []

        def backtrack(letters, path, dig_index):
            if dig_index == len(digits): 
                ans.append(path)
                return

            digit = digits[dig_index]
            digit_letters = letters[digit]

            for i in range(len(digit_letters)):
                path = path + digit_letters[i]
                backtrack(letters, path, dig_index + 1)
                path = path[:-1]
        
        backtrack(letters, "", 0)
        return ans