from typing import List
from collections import Counter

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        total_chars = Counter()
        for w in words:
            for c in w:
                total_chars[c] += 1
        n = len(words)
        for count in total_chars.values():
            if count % n != 0:
                return False
        return True