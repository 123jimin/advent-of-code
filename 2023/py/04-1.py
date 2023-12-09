class Card:
    def __init__(self, line):
        _, numbers = line.split(':')
        winning_numbers, have_numbers = numbers.split('|')
        self.winning_numbers = set(int(x) for x in winning_numbers.split() if x)
        self.have_numbers = set(int(x) for x in have_numbers.split() if x)
    
    def __repr__(self):
        return f"Card(winning={repr(self.winning_numbers)}, have={repr(self.have_numbers)})"

    def wins(self):
        return sum(num in self.winning_numbers for num in self.have_numbers)
    
    def point(self):
        wins = self.wins()
        if wins == 0: return 0
        return 2**(wins-1)

cards = []
with open("../input/04.txt") as f:
    for line in f:
        line = line.strip()
        if line: cards.append(Card(line))

print(sum(card.point() for card in cards))