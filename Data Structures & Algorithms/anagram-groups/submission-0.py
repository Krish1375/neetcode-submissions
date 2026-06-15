from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictmap = defaultdict(list)
        
        for word in strs:
            # Create a frequency list of size 26
            count = [0] * 26
            for char in word:
                # Map 'a' to 0, 'b' to 1, ..., 'z' to 25
                count[ord(char) - ord('a')] += 1
            
            # Convert list to tuple to make it hashable for the dictionary
            dictmap[tuple(count)].append(word)
            
        return list(dictmap.values())