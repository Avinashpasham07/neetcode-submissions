from typing import List
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat_all(k: int) -> bool:
            hours = 0
            for p in piles:
                hours += (p + k - 1) // k
                if hours > h:
                    return False
            return True
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if can_eat_all(mid):
                right = mid
            else:
                left = mid + 1
        return left