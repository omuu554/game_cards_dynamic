from unittest import TestCase,mock
from Player import Player
from Card import Card
from DeckOfCards import DeckOfCards

class TestPlayer(TestCase):


    def setUp(self) :
        self.player = Player("Omer", 10)
        self.Deck = DeckOfCards()

    def test_Player_init_valid(self):
        player1 = Player("ron123@#",17)
        self.assertEqual(player1.PlayerName,'ron123@#')
        self.assertEqual(player1.DeckSize, 17)
        self.assertEqual(type(player1.PlayerCards),list)
        self.assertFalse(player1.PlayerCards)

        player2 = Player('Jhonatan',13)
        self.assertEqual(player2.PlayerName, 'Jhonatan')
        self.assertEqual(player2.DeckSize, 13)
        self.assertEqual(type(player2.PlayerCards), list)
        self.assertFalse(player2.PlayerCards)

        player3 = Player(123, 22)
        self.assertEqual(player3.PlayerName, '123')
        self.assertEqual(player3.DeckSize, 22)
        self.assertEqual(type(player3.PlayerCards), list)
        self.assertFalse(player3.PlayerCards)

    def test_Player_init_validLimit(self):
        player1 = Player()
        self.assertEqual(player1.PlayerName, 'GuestPlayer')
        self.assertEqual(player1.DeckSize, 26)

        player2 = Player(PlayerDeckStartSize=10)
        self.assertEqual(player2.PlayerName, 'GuestPlayer')
        self.assertEqual(player2.DeckSize, 10)

        player3 = Player(PlayerDeckStartSize=26)
        self.assertEqual(player3.PlayerName, 'GuestPlayer')
        self.assertEqual(player3.DeckSize, 26)

    def test_Player_init_invalidDeckSize(self):
        player1 = Player(PlayerDeckStartSize= 'abcd')
        self.assertEqual(player1.PlayerName, 'GuestPlayer')
        self.assertEqual(player1.DeckSize, 26)

        player2 = Player(PlayerDeckStartSize=15.7)
        self.assertEqual(player2.PlayerName, 'GuestPlayer')
        self.assertEqual(player2.DeckSize, 26)

        player2 = Player(PlayerDeckStartSize=-1)
        self.assertEqual(player2.PlayerName, 'GuestPlayer')
        self.assertEqual(player2.DeckSize, 26)

        player2 = Player(PlayerDeckStartSize=30)
        self.assertEqual(player2.PlayerName, 'GuestPlayer')
        self.assertEqual(player2.DeckSize, 26)

        player2 = Player(PlayerDeckStartSize="14")
        self.assertEqual(player2.PlayerName, 'GuestPlayer')
        self.assertEqual(player2.DeckSize, 14)

    def test_Player_init_invalidDeckSizeLimit(self):
        player1 = Player(PlayerDeckStartSize=27)
        self.assertEqual(player1.PlayerName, 'GuestPlayer')
        self.assertEqual(player1.DeckSize, 26)

        player2 = Player(PlayerDeckStartSize=9)
        self.assertEqual(player2.PlayerName, 'GuestPlayer')
        self.assertEqual(player2.DeckSize, 26)

    def test_Player_IsPlayerDeckNotEmpty_valid(self):
        self.player.Set_Hand(self.Deck)
        self.assertTrue(self.player.IsPlayerDeckNotEmpty())

    def test_Player_IsPlayerDeckNotEmpty_valid(self):
        self.assertFalse(self.player.IsPlayerDeckNotEmpty())

    def test_Player_Set_Hand_valid(self):
        self.player.Set_Hand( self.Deck)
        self.assertEqual(len(self.player.PlayerCards), 10)
        self.assertEqual(len( self.Deck.DeckCards),42)
        for i in range(self.player.DeckSize):
         self.assertEqual(type(self.player.PlayerCards[i]), Card)

    def test_Player_Set_Hand_invalidLimit(self):
        self.Deck.DeckCards = []
        self.player.Set_Hand( self.Deck)
        self.assertFalse(self.player.PlayerCards)

    def test_Player_Set_Hand_invalid(self):
        i = [2,4]
        List = [1,2,3,4,5,6]
        with self.assertRaises(TypeError):
         self.player.Set_Hand(List)

        with self.assertRaises(TypeError):
         self.player.Set_Hand(i)

        with self.assertRaises(TypeError):
         self.player.Set_Hand(12)

        with self.assertRaises(TypeError):
         self.player.Set_Hand('abc')

    def test_Player_GetCard_valid(self):
        self.player.Set_Hand(self.Deck)
        card = self.player.Get_Card()
        self.assertEqual(type(card), Card)
        self.assertIn(card, self.Deck.CreateDeck())


    @mock.patch('Player.Player.IsPlayerDeckNotEmpty', return_value = False)
    def test_Player_GetCard_invalidLimit(self, PlayerDeckEmpty):
        self.player.Set_Hand(self.Deck)
        self.assertIsNone(self.player.Get_Card())

    def test_Player_Add_Card_valid(self):
        card = Card(1,2)
        self.player.Add_Card(card)

        card2 = Card(2, 3)
        self.player.Add_Card(card2)

        card3 = Card(13,1)
        self.player.Add_Card(card3)

        self.assertIn(card, self.player.PlayerCards)
        self.assertIn(card2, self.player.PlayerCards)
        self.assertIn(card3, self.player.PlayerCards)
        self.assertEqual(len(self.player.PlayerCards),3)

    def test_Player_Add_Card_invalid(self):
      with self.assertRaises(TypeError):
         self.player.Add_Card(2)

      with self.assertRaises(TypeError):
          self.player.Add_Card("abc")

      with self.assertRaises(TypeError):
          self.player.Add_Card([1,2,3])

      with self.assertRaises(TypeError):
          self.player.Add_Card(["a","b","c"])

    def tearDown(self):
        pass
