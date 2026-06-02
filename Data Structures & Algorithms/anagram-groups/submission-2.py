class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            sorted_word = sorted(word)

            if ''.join(sorted_word) in hashmap:
                hashmap[''.join(sorted_word)].append(word)
            else:
                hashmap[''.join(sorted_word)] = [word]
        return list(hashmap.values())
