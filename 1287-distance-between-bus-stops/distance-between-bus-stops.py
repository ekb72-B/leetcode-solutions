class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        # make 2 dp lists one from front one from back. return min at certain index

        if start > destination:
            start, destination = destination, start 

        tot = sum(distance)
        clockwise = 0

        for i in range(start, destination):
            clockwise += distance[i]
        
        anticlockwise = tot - clockwise

        return clockwise if clockwise < anticlockwise else anticlockwise
        