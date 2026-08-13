class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        best = 0
        for num in s:
            if num - 1 not in s:
                length = 1
                current = num
                while current + 1 in s:
                    current += 1
                    length += 1
                best = max(best, length)
        return best