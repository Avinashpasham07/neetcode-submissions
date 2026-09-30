from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleets = []
        for pos, spd in cars:
            time = (target - pos) / spd
            if not fleets or time > fleets[-1]:
                fleets.append(time)
        return len(fleets)