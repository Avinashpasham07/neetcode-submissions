class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1
        window = {}
        have = 0
        required = len(need)
        left = 0
        best_len = float("inf")
        best_start = 0
        for right, ch in enumerate(s):
            window[ch] = window.get(ch, 0) + 1
            if ch in need and window[ch] == need[ch]:
                have += 1
            while have == required:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_start = left
                left_char = s[left]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                left += 1
        return "" if best_len == float("inf") else s[best_start:best_start + best_len]