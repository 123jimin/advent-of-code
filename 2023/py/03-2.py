class SchematicNumber:
    number: str
    def __init__(self, pos, number):
        self.pos = pos
        self.number = number
    
    def neighbors(self):
        i, j = self.pos
        l = len(self.number)

        for k in range(-1, l+1):
            yield (i-1, j+k)
            if not (0 <= k < l):
                yield (i, j+k)
            yield (i+1, j+k)
    
    def __repr__(self):
        return f"SchematicNumber({repr(self.pos)}, {repr(self.number)})"

class SchematicSymbol:
    def __init__(self, pos, ch):
        self.pos = pos
        self.ch = ch
        self.adjacent_numbers = []
    
    def gear_power(self):
        if self.ch != '*': return 0
        if len(self.adjacent_numbers) != 2: return 0
        return self.adjacent_numbers[0] * self.adjacent_numbers[1]

    def __repr__(self):
        return f"SchematicSymbol({repr(self.pos)}, {repr(self.ch)})"

class EngineSchematic:
    symbols = dict()
    numbers = list()

    R: int
    C: int

    def __init__(self, lines):
        self.R = len(lines)
        self.C = len(lines[0])

        for (i, line) in enumerate(lines):
            self.parse_line(i, line)

    def parse_line(self, i, line):
        j = 0
        curr_number = None
        for (j, ch) in enumerate(line):
            if '0' <= ch <= '9':
                if curr_number is None:
                    curr_number = SchematicNumber((i, j), '')
                    self.numbers.append(curr_number)
                curr_number.number += ch
            else:
                curr_number = None
                if ch != '.':
                    self.symbols[(i, j)] = SchematicSymbol((i, j), ch)

with open("../input/03.txt") as f:
    schematic = EngineSchematic([line.strip() for line in f if line.strip()])

for number in schematic.numbers:
    for neighbor in number.neighbors():
        symbol = schematic.symbols.get(neighbor)
        if symbol:
            symbol.adjacent_numbers.append(int(number.number))

answer = sum(symbol.gear_power() for symbol in schematic.symbols.values())
print(answer)