class Solution:

    def encode(self, strs: List[str]) -> str:
        return_string = ""
        for word in strs:
            return_string += str(len(word)) + "#" + word
        return return_string

    def decode(self, s: str) -> List[str]:
        return_list = []
        i = 0
        number = ""
        while i<len(s):
            if s[i].isdigit():
                number = number + s[i]
                i+=1
            else:
                if s[i] == "#":
                    return_list.append(s[i+1:i+1+int(number)])
                    i+=(int(number)+1)
                    number = ""
                else:
                    return[""]
        return return_list
                