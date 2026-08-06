from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # ans is just nums followed by nums again
        return nums + nums