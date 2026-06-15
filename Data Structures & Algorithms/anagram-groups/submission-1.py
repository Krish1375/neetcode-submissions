class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictmap = defaultdict(list)
        result = []
        for word in strs:
            sorted_word = "".join(sorted(word))
            dictmap[sorted_word].append(word)
        
        return list(dictmap.values())