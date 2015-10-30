import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class DeckOfCards:
    ranks = []
    for n in range(2, 11):
        ranks.append(n)
    for p in 'JQKA':
        ranks.append(p)
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = []
        for suit in self.suits:
            for rank in self.ranks:
                self._cards.append(Card(rank, suit))

deck = DeckOfCards()
print(deck.ranks)
print(deck.suits)
