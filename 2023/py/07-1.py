from collections import Counter

CARD_STRENGTH = dict((c, i) for (i, c) in enumerate("23456789TJQKA"))

HT_FIVE_OF_A_KIND = 6
HT_FOUR_OF_A_KIND = 5
HT_FULL_HOUSE = 4
HT_THREE_OF_A_KIND = 3
HT_TWO_PAIR = 2
HT_ONE_PAIR = 1
HT_HIGH_CARD = 0

class Hand:
    hand_type = None
    bid: int = 0
    def __init__(self, cards, bid):
        self.cards = Counter(cards.strip())
        self.bid = bid
        self.card_strengths = tuple(CARD_STRENGTH[c] for c in cards)

        self.hand_type = self._compute_hand_type()
    
    def _compute_hand_type(self):
        max_cards = max(self.cards.values())
        if max_cards == 5: return HT_FIVE_OF_A_KIND
        if max_cards == 4: return HT_FOUR_OF_A_KIND
        if max_cards == 3:
            if len(self.cards) == 2: return HT_FULL_HOUSE
            else: return HT_THREE_OF_A_KIND
        if max_cards == 2:
            if len(self.cards) == 3: return HT_TWO_PAIR
            else: return HT_ONE_PAIR
        return HT_HIGH_CARD

    def __repr__(self):
        return f"Hand({self.card_strengths}, {self.bid})"

hands = []
with open("../input/07.txt") as f:
    for line in f:
        line = line.strip()
        if not line: continue
        cards, bid = line.split(' ')
        hands.append(Hand(cards, int(bid)))

hands.sort(key=lambda card: (card.hand_type, card.card_strengths))
print(sum(hand.bid * (i+1) for (i, hand) in enumerate(hands)))