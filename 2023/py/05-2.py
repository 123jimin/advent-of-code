class Interval:
    __slots__ = ('start', 'end', 'data')
    def __init__(self, start, end, data=None):
        self.start = start
        self.end = end
        self.data = data
    def __bool__(self):
        return self.start < self.end
    def __and__(self, other):
        return Interval(max(self.start, other.start), min(self.end, other.end))
    def __repr__(self):
        return f"({repr(self.start)}, {repr(self.end)}: {repr(self.data)})"

class Intervals:
    # intervals: (start, end)
    def __init__(self, intervals=[]):
        self.intervals = []
        for interval in sorted(intervals, key=lambda interval: interval.start):
            if not interval: continue
            if len(self.intervals) > 0:
                last_interval = self.intervals[-1]
                if interval.start <= last_interval.end:
                    last_interval.end = interval.end
                    continue
            self.intervals.append(interval)
        
    def __repr__(self):
        return f"Intervals({repr(self.intervals)})"

class ConvertMap:
    def __init__(self):
        self.ranges = []

    def add_range(self, dst_start:int, src_start:int, range_len:int):
        self.ranges.append(Interval(src_start, src_start + range_len, dst_start - src_start))

    def map_intervals(self, intervals: Intervals):
        ranges = sorted(self.ranges, key=lambda range: range.start)

        for interval in intervals.intervals:
            prev_range_end = None
            # Could do binary search, but too lazy to do it
            for range in ranges:
                if interval.end <= range.start:
                    break
                if range.end <= interval.start:
                    continue
                if prev_range_end is None:
                    yield Interval(interval.start, min(interval.end, range.start))
                intersected = range & interval
                if intersected:
                    intersected.start += range.data
                    intersected.end += range.data
                    yield intersected
                prev_range_end = range.end
            if prev_range_end is None:
                yield interval
            else:
                yield Interval(prev_range_end, interval.end)

    def __repr__(self):
        return f"ConvertMap(ranges={repr(self.ranges)})"

class Problem:
    def __init__(self, f):
        self.seeds = None
        self.convert_maps = []

        curr_convert_map = None

        for line in f:
            line = line.strip()
            if not line: continue
            if line.startswith("seeds:"):
                seed_nums = [int(x) for x in line.split(':')[1].split() if x]
                self.seeds = Intervals([Interval(seed_nums[i], seed_nums[i]+seed_nums[i+1]) for i in range(0, len(seed_nums), 2)])
                continue
            if line.endswith(":"):
                curr_convert_map = ConvertMap()
                self.convert_maps.append(curr_convert_map)
                continue
            curr_convert_map.add_range(*(int(x) for x in line.split() if x))
        
    def get_dst_values(self):
        seeds = self.seeds
        for convert_map in self.convert_maps:
            seeds = Intervals(convert_map.map_intervals(seeds))
        return seeds
            

with open("../input/05.txt") as f:
    problem = Problem(f)
    
print(problem.get_dst_values().intervals[0].start)