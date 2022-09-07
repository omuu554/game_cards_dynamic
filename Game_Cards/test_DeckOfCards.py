from DeckOfCards import DeckOfCards
from Card import Card
import random
from unittest import TestCase,mock


class TestDeckOfCards(TestCase):

    def setUp(self):
        self.Deck1 = DeckOfCards()

    def test_DeckOfCards_CreateDeck_valid(self):
        self.Deck1 = DeckOfCards()
        ShowDeck = self.Deck1.CreateDeck()
        self.assertEqual(len(ShowDeck),52)
        for i in range(1,5):
            for j in range(1,14):
                NewCard = Card(j,i)
                self.Deck1.DeckCards.remove(NewCard)

        self.assertFalse(self.Deck1.DeckCards)



    def test_DeckOfCards_init_valid(self):
        Deck2 = DeckOfCards()
        self.assertEqual(self.Deck1.DeckCards, Deck2.DeckCards)
        for i in range(52):
         self.assertIn(Deck2.DeckCards[i],self.Deck1.DeckCards)

    def test_DeckOfCards_CardShuffle_valid(self):
        Deck2 = DeckOfCards()
        Deck2.CardShuffle()
        self.assertNotEqual(Deck2.DeckCards,self.Deck1.DeckCards)
        for i in range(52):
         self.assertIn(Deck2.DeckCards[i],self.Deck1.DeckCards)


    def test_DeckOfCards_Deal_One_valid(self):
        card1 = self.Deck1.Deal_One()
        self.assertNotIn(card1,self.Deck1.DeckCards)
        self.assertEqual(len(self.Deck1.DeckCards),51)
        card2 = self.Deck1.Deal_One()
        self.assertNotIn(card2, self.Deck1.DeckCards)
        self.assertEqual(len(self.Deck1.DeckCards), 50)
        card3 = self.Deck1.Deal_One()
        self.assertNotIn(card3, self.Deck1.DeckCards)
        self.assertEqual(len(self.Deck1.DeckCards), 49)
        card4 = self.Deck1.Deal_One()
        self.assertNotIn(card4, self.Deck1.DeckCards)
        self.assertEqual(len(self.Deck1.DeckCards), 48)

    def test_DeckOfCards_Deal_One_validLimit(self):
        for i in range(52):
            self.Deck1.Deal_One()

        self.assertFalse(self.Deck1.DeckCards)
        self.assertIsNone(self.Deck1.Deal_One())







    def tearDown(self):
        pass