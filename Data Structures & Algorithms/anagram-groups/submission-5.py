class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        for char in strs:
            sort = ''.join(sorted(char))
            if sort in groups:
                groups[sort].append(char)
            else:
                groups[sort] = [char]
            
        return list(groups.values())