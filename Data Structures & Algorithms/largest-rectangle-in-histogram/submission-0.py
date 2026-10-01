from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] 
        max_area = 0
        n = len(heights)
        for i in range(n + 1):
            curr_height = heights[i] if i < n else 0
            while stack and curr_height < heights[stack[-1]]:
                h = heights[stack.pop()]
                left_boundary = stack[-1] if stack else -1
                width = i - left_boundary - 1
                max_area = max(max_area, h * width)
            stack.append(i)
        return max_area