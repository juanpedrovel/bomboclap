# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x: (x.start, x.end))
        current = None
        new_intervals = []
        for interval in intervals:
            if not current:
                current = interval
            elif current.end < interval.start:
                new_intervals.append(current)
                current = interval
            else:
                current.start = min(current.start, interval.start)
                current.end = max(current.end, interval.end)
        new_intervals.append(current)
        return new_intervals

interval = Interval(6,8)
intervals = [Interval(1,5)]
d = Solution()
print(d.insert(intervals, interval))