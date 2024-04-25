class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l_int = len(intervals)
        result = []
        n = 0

        while n < l_int and intervals[n][1] < newInterval[0]:
            result.append(intervals[n])
            n += 1
        
        while n < l_int and intervals[n][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[n][0])
            newInterval[1] = max(newInterval[1], intervals[n][1])
            n += 1
        
        result.append(newInterval)

        while n < l_int:
            # the interval beginning is not less than new interval ending and 
            # the interval ending is >= new interval beginning
            result.append(intervals[n])
            n += 1
        
        return result 
        