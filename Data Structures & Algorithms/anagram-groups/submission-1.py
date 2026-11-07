class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouping = {}
        
        for string in strs:
            key = "".join(sorted(string))

            if key not in grouping:
                grouping[key] = []
            
            grouping[key].append(string)
        
        return list(grouping.values())


        