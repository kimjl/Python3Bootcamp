import unittest
from deck_of_cards import Card, Deck

class CardTests(unittest.TestCase):
	def setUp(self):
		self.cards = Card("Hearts", "A")

	def test_init(self):
		"""cards should have a suit and value"""
		self.assertEqual(self.cards.suit, "Hearts")
		self.assertEqual(self.cards.value, "A")

	def test_repr(self):
		"""repr should return a string of the form VALUE of SUIT"""
		self.assertEqual(repr(self.cards), "A of Hearts")

class DeckTests(unittest.TestCase):
	def setUp(self):
		self.deck = Deck()

	def test_init(self):
		"""decks should have card attribute which is a list of size 52"""
		self.assertTrue(isinstance(self.deck.cards, list))
		self.assertEqual(len(self.deck.cards), 52)

	def test_repr(self):
		"""repr should return string of form Deck of count cards"""
		self.assertEqual(repr(self.deck), "Deck of 52 cards")

	def test_count(self):
		"""shouild return count of number of cards in deck"""
		self.assertEqual(self.deck.count(), 52)
		self.deck.cards.pop()
		self.assertEqual(self.deck.count(), 51)

	def test_deal_sufficient_cards(self):
		"""_deal should deal number of cards specified, if possible"""
		cards = self.deck._deal(10)
		self.assertEqual(len(cards), 10)
		self.assertEqual(self.deck.count(), 42)

	def test_deal_insufficient_cards(self):
		"""deal should deal the number of cards left in the deck"""
		cards = self.deck._deal(100)
		self.assertEqual(len(cards), 52)
		self.assertEqual(self.deck.count(), 0)

	def test_deal_no_cards(self):
		"""deal should throw ValueError if deck is empty"""
		self.deck._deal(self.deck.count())
		with self.assertRaises(ValueError):
			self.deck._deal(1)

	def test_deal_card(self):
		"""deal should deal a single card from deck"""
		card = self.deck.cards[-1]
		dealt_card = self.deck.deal_card()
		self.assertEqual(card, dealt_card)
		self.assertEqual(self.deck.count(), 51)

	def test_deal_hand(self):
		"""deal_hand should deal number of cards passed"""
		cards = self.deck.deal_hand(20)
		self.assertEqual(len(cards), 20)
		self.assertEqual(self.deck.count(), 32)

	def test_shuffle_hand(self):
		"""shuffle should shuffle the deck if the deck is full"""
		cards = self.deck.cards[:]
		self.deck.shuffle()
		self.assertNotEqual(cards, self.deck.cards)

	def test_shuffle_not_full_deck(self):
		"""shuffle should throw ValueError if deck is not full"""
		self.deck._deal(1)
		with self.assertRaises(ValueError):
			self.deck.shuffle()


if __name__ == '__main__':
	unittest.main()