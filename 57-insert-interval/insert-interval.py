class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        lenintervals = len(intervals)
        result = []
        curr = 0 

        while curr < lenintervals and intervals[curr][1] < newInterval[0]:
            result.append(intervals[curr])
            curr += 1
        
        while curr < lenintervals and intervals[curr][0] <= newInterval[1]:
            newInterval[0] = min(intervals[curr][0], newInterval[0])
            newInterval[1] = max(intervals[curr][1], newInterval[1])
            curr += 1
        
        result.append(newInterval)

        while curr < lenintervals:
            result.append(intervals[curr])
            curr += 1
        
        return result
