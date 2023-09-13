from collections import namedtuple
from random import choices

#Similar to class with its attributes this are all classes of objects
Card = namedtuple('Card' , ['rank' , 'suit'])

#Use of above class as  eg below
# four_of_heart = Card(4,'heart')
# print(four_of_heart) #OP -->Card(rank=4, suits='heart')
# print(four_of_heart.rank, " " , four_of_heart.suits)

class FrenchDeck:
  ranks = [str(n) for n in range(2,11)]+list('JQKA')
  suits = 'spades diamonds clubs hearts'.split()

  # print(ranks)
  # print(suits)

  def __init__(self):
    #Creating 52 cards
    self._cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]
    #print(self._cards)
  def __len__(self):
    return len(self._cards)
  def __getitem__(self,position):
    return self._cards[position]
  

deck = FrenchDeck()
# print(deck.ranks)
# print(deck.suits)
# print(len(deck))

# print(deck[0], " ", deck[-1])

#picking an arbitary card
card_1 = choices(deck)
print(card_1)
