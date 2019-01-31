class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            return [newInterval]
        new_intervals = []
        is_selected = True
        for interval in intervals:
            if newInterval.start > interval.end or newInterval.end < interval.start:
                if is_selected and newInterval.end < interval.start:
                    new_intervals.append(newInterval)
                    is_selected = False
                new_intervals.append(interval)
            else:
                newInterval.start = min(newInterval.start, interval.start)
                newInterval.end = max(newInterval.end, interval.end)
                is_selected = True
        if is_selected:
            new_intervals.append(newInterval)
        return new_intervals

interval = Interval(6,8)
intervals = [Interval(1,5)]
d = Solution()
print(d.insert(intervals, interval))