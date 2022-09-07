from Card import Card
from unittest import TestCase

class TestCard(TestCase):

    def setUp(self) :
        pass

    def test_Card_init_valid(self):
        card = Card(13,2)
        self.assertEqual(card.Value,13)
        self.assertEqual(card.Suit,2)
        card2 = Card(1, 4)
        self.assertEqual(card2.Value, 1)
        self.assertEqual(card2.Suit, 4)

    def test_Card_init_validLimit(self):
        card = Card(13,1)
        self.assertEqual(card.Value,13)
        self.assertEqual(card.Suit,1)
        card2 = Card(1, 4)
        self.assertEqual(card2.Value, 1)
        self.assertEqual(card2.Suit, 4)

    def test_Card_init_invalidDigit(self):
      with self.assertRaises(TypeError): # limit test
          card = Card("2", 2)
      with self.assertRaises(TypeError):
          card = Card("abcd", 2)
      with self.assertRaises(TypeError):
          card = Card(2, "abcd")
      with self.assertRaises(TypeError):
          card = Card(2, "2")


    def test_Card_init_invalidValue(self):
        with self.assertRaises(TypeError):
            card = Card(-9, 2)
        with self.assertRaises(TypeError):
            card = Card(17, 2)
        with self.assertRaises(TypeError):
            card = Card(-1, 2)
        with self.assertRaises(TypeError):
            c = Card(20, 2)

    def test_Card_init_invalidValueLimit(self):
        with self.assertRaises(TypeError):
            card = Card(0, 2)
        with self.assertRaises(TypeError):
            card = Card(14, 2)

    def test_Card_init_invalidSuit(self):
        with self.assertRaises(TypeError):
            card = Card(2, -7)
        with self.assertRaises(TypeError): 
            card = Card(2, 22)
        with self.assertRaises(TypeError):
            card = Card(2, -5)
        with self.assertRaises(TypeError):
            card = Card(2, 17)

    def test_Card_init_invalidSuitLimit(self):
        with self.assertRaises(TypeError):
            card = Card(2, 0)
        with self.assertRaises(TypeError):
            card = Card(2, 14)

    def test_Card_eq_valid(self):
        card1 = Card(3,4)
        card2 = Card(3,4)
        self.assertEqual(card1,card2)
        self.assertTrue(card1 == card2)
        card1 = Card(13, 1)
        card2 = Card(13, 1)
        self.assertEqual(card1, card2)
        self.assertTrue(card1 == card2)

    def test_Card_eq_invalid(self):
        card1 = Card(3, 4)
        card2 = Card(3, 5)
        self.assertNotEqual(card1, card2)
        self.assertFalse(card1 == card2)
        card1 = Card(13, 1)
        card2 = Card(12, 1)
        self.assertNotEqual(card1, card2)
        self.assertFalse(card1 == card2)
        card1 = Card(11, 4)
        card2 = Card(6, 2)
        self.assertNotEqual(card1, card2)
        self.assertFalse(card1 == card2)

    def test_Card_gt_validValueUnequal(self):
        card1 = Card(9, 4)
        card2 = Card(6, 2)
        self.assertTrue(card1 > card2)
        card1 = Card(1, 1)
        card2 = Card(13, 2)
        self.assertTrue(card1 > card2)  # limit test


    def test_Card_gt_invalidValueUnequal(self):
        card1 = Card(2, 3)
        card2 = Card(6, 4)
        self.assertFalse(card1 > card2)
        card1 = Card(9, 2)
        card2 = Card(1, 2)
        self.assertFalse(card1 > card2)

    def test_Card_gt_validValueEqual(self):
        card1 = Card(9, 4)
        card2 = Card(9, 2)
        self.assertTrue(card1 > card2)
        card1 = Card(13, 3)
        card2 = Card(13, 1)
        self.assertTrue(card1 > card2)
    def test_Card_gt_invalidValueEqual(self):
        card1 = Card(6, 1)
        card2 = Card(6, 2)
        self.assertFalse(card1 > card2)
        card1 = Card(11, 2)
        card2 = Card(11, 3)
        self.assertFalse(card1 > card2)

def tearDown(self):
        pass