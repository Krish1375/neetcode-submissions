import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right

        while left <= right:
            mid = (left + right) // 2
            result = 0
            for bananas in piles:
                result += math.ceil(bananas / mid)
            if result <= h:
                res = mid
                right = mid - 1
            
            else:
                left = mid + 1
            
        return res
