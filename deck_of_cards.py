from random import shuffle

class Card:
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def __repr__(self):
		# return f'A {self.value} of {self.suit}'
		return '{} of {}'.format(self.suit, self.value)

class Deck:

	def __init__(self):
		suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
		values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
		self.cards = [Card(value, suit) for suit in suits for value in values ]
		# print(self.cards)

	def __repr__(self):
		#return information on how many cards are in the deck
		return 'Deck of {} cards'.format(self.count())

	def count(self):
		#eturns a count of how many cards remain in the deck
		return len(self.cards)

	def _deal(self, num):
		#accepts a number and removes at most that many cards from the deck (it may need to remove fewer if you request more cards than are currently in the deck!). 
		#If there are no cards left, this method should return a ValueError  with the message "All cards have been dealt"
		count = self.count()
		actual = min(count, num)
		
		if count == 0:
			raise ValueError('All cards have been dealt')
		deal_cards = self.cards[-actual:]
		self.cards = self.cards[:-actual]
		return deal_cards

	def deal_card(self):
		#uses the _deal  method to deal a single card from the deck and return that single card
		return self._deal(1)[0]

	def deal_hand(self, hand_size):
		#accepts a number and uses the _deal  method to deal a list of cards from the deck and return that list of cards
		return self._deal(hand_size)

	def shuffle(self):
		#shuffle a full deck of cards. If there are cards missing from the deck, this method should return a ValueError  with the message "Only full decks can be shuffled".  
		#shuffle should return the shuffled deck.
		if self.count() < 52:
			raise ValueError('Only full decks can be shuffled')
		shuffle(self.cards)
		return self

d = Deck()
# print(d.cards)
d.shuffle()
# print(d.cards)
card = d.deal_card()
print(card)
hand = d.deal_hand(50)
print(hand)
print(d.cards)

