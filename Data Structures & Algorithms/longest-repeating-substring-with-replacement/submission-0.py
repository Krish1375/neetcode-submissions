class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        result = 0
        dictmap = {}

        for right in range(len(s)):
            dictmap[s[right]] = dictmap.get(s[right],0) + 1
            
            while (right - left + 1) - max(dictmap.values()) > k:
                dictmap[s[left]] -=1
                left+=1
            
            result = max(result, (right - left + 1))
        return result