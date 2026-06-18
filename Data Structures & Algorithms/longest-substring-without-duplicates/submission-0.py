class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dictmap = {}
        left = 0
        result = 0

        for right in range(len(s)):
            char = s[right]
            
            if char in dictmap and dictmap[char] >= left:
                left = dictmap[char] + 1
            
            result = max(result, right - left + 1)
            
            dictmap[char] = right
            
        return result