class ConvertMap:
    def __init__(self):
        self.ranges = []

    def add_range(self, dst_start:int, src_start:int, range_len:int):
        # Naive
        self.ranges.append((dst_start, src_start, range_len))
    
    def map_value(self, value:int):
        # Naive
        for (dst_start, src_start, range_len) in self.ranges:
            if src_start <= value < src_start + range_len:
                return dst_start + (value - src_start)
        return value

    def __repr__(self):
        return f"ConvertMap(ranges={repr(self.ranges)})"

class Problem:
    def __init__(self, f):
        self.seeds = []
        self.convert_maps = []

        curr_convert_map = None

        for line in f:
            line = line.strip()
            if not line: continue
            if line.startswith("seeds:"):
                self.seeds = [int(x) for x in line.split(':')[1].split() if x]
                continue
            if line.endswith(":"):
                curr_convert_map = ConvertMap()
                self.convert_maps.append(curr_convert_map)
                continue
            curr_convert_map.add_range(*(int(x) for x in line.split() if x))
        
    def get_dst_values(self):
        values = self.seeds
        for convert_map in self.convert_maps:
            values = list(convert_map.map_value(value) for value in values)
        return values
            

with open("../input/05.txt") as f:
    problem = Problem(f)

print(min(problem.get_dst_values()))