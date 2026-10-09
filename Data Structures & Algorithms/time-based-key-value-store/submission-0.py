from collections import defaultdict
class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        entries = self.store[key]
        left, right = 0, len(entries) - 1
        result_index = -1
        while left <= right:
            mid = (left + right) // 2
            mid_ts = entries[mid][0]
            if mid_ts <= timestamp:
                result_index = mid
                left = mid + 1
            else:
                right = mid - 1
        if result_index == -1:
            return ""
        return entries[result_index][1]