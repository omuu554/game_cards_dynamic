from unittest import TestCase,mock
from CardGame import CardGame


class TestCardGame(TestCase):

    def setUp(self) :
        self.cardgame = CardGame()

    def test_CardGame_init_valid(self):
        cardgame = CardGame("josh","emnuel",12,17)
        self.assertEqual(len(cardgame.Player1.PlayerCards),12)
        self.assertEqual(len(cardgame.Player2.PlayerCards),17)
        self.assertEqual(cardgame.Player1.PlayerName, 'josh')
        self.assertEqual(cardgame.Player2.PlayerName, 'emnuel')
        self.assertEqual(len(cardgame.DeckOfCards.DeckCards),23)

        cardgame2 = CardGame("josh", "emnuel", 11, 23)
        self.assertEqual(len(cardgame2.Player1.PlayerCards), 11)
        self.assertEqual(len(cardgame2.Player2.PlayerCards), 23)
        self.assertEqual(cardgame2.Player1.PlayerName, 'josh')
        self.assertEqual(cardgame2.Player2.PlayerName, 'emnuel')
        self.assertEqual(len(cardgame2.DeckOfCards.DeckCards), 18)

    def test_CardGame_init_validLimit(self):
        self.assertEqual(len(self.cardgame.Player1.PlayerCards), 26)
        self.assertEqual(len(self.cardgame.Player2.PlayerCards), 26)
        self.assertEqual(self.cardgame.Player1.PlayerName, 'GuestPlayer(1)')
        self.assertEqual(self.cardgame.Player2.PlayerName, 'GuestPlayer(2)')
        self.assertEqual(len(self.cardgame.DeckOfCards.DeckCards), 0)

        cardgame2 = CardGame(PlayerDeckSize1= 10, PlayerDeckSize2=10)
        self.assertEqual(len(cardgame2.Player1.PlayerCards), 10)
        self.assertEqual(len(cardgame2.Player2.PlayerCards), 10)
        self.assertEqual(cardgame2.Player1.PlayerName, 'GuestPlayer(1)')
        self.assertEqual(cardgame2.Player2.PlayerName, 'GuestPlayer(2)')
        self.assertEqual(len(cardgame2.DeckOfCards.DeckCards), 32)

        cardgame3 = CardGame(PlayerDeckSize1=26, PlayerDeckSize2=26)
        self.assertEqual(len(cardgame3.Player1.PlayerCards), 26)
        self.assertEqual(len(cardgame3.Player2.PlayerCards), 26)
        self.assertEqual(cardgame3.Player1.PlayerName, 'GuestPlayer(1)')
        self.assertEqual(cardgame3.Player2.PlayerName, 'GuestPlayer(2)')
        self.assertEqual(len(cardgame3.DeckOfCards.DeckCards), 0)


    def test_CardGame_init_invalid(self):
        cardgame = CardGame(123,2.23,59,-9)
        self.assertEqual(len(cardgame.Player1.PlayerCards), 26)
        self.assertEqual(len(cardgame.Player2.PlayerCards), 26)
        self.assertEqual(cardgame.Player1.PlayerName, '123')
        self.assertEqual(cardgame.Player2.PlayerName, '2.23')
        self.assertEqual(len(cardgame.DeckOfCards.DeckCards), 0)

        cardgame2 = CardGame(PlayerDeckSize1="abcd", PlayerDeckSize2="12")
        self.assertEqual(len(cardgame2.Player1.PlayerCards), 26)
        self.assertEqual(len(cardgame2.Player2.PlayerCards), 12)
        self.assertEqual(cardgame2.Player1.PlayerName, 'GuestPlayer(1)')
        self.assertEqual(cardgame2.Player2.PlayerName, 'GuestPlayer(2)')
        self.assertEqual(len(cardgame2.DeckOfCards.DeckCards), 14)

    def test_CardGame_init_invalidLimit(self):
        cardgame = CardGame(PlayerDeckSize1=27, PlayerDeckSize2=27)
        self.assertEqual(len(cardgame.Player1.PlayerCards), 26)
        self.assertEqual(len(cardgame.Player2.PlayerCards), 26)
        self.assertEqual(cardgame.Player1.PlayerName, 'GuestPlayer(1)')
        self.assertEqual(cardgame.Player2.PlayerName, 'GuestPlayer(2)')
        self.assertEqual(len(cardgame.DeckOfCards.DeckCards), 0)

        cardgame = CardGame(PlayerDeckSize1= 9, PlayerDeckSize2= 9)
        self.assertEqual(len(cardgame.Player1.PlayerCards), 26)
        self.assertEqual(len(cardgame.Player2.PlayerCards), 26)
        self.assertEqual(cardgame.Player1.PlayerName, 'GuestPlayer(1)')
        self.assertEqual(cardgame.Player2.PlayerName, 'GuestPlayer(2)')
        self.assertEqual(len(cardgame.DeckOfCards.DeckCards), 0)


    def test_CardGame_GetWinner_validPlayer1(self):
        with mock.patch('CardGame.CardGame.GameStatus') as gameStatus:
            gameStatus.return_value = 1
            self.assertEqual(self.cardgame.Get_Winner(),self.cardgame.Player1)

    def test_CardGame_GetWinner_validPlayer2(self):
        with mock.patch('CardGame.CardGame.GameStatus') as gameStatus:
            gameStatus.return_value = 2
            self.assertEqual(self.cardgame.Get_Winner(),self.cardgame.Player2)

    def test_CardGame_GetWinner_validPlayer2(self):
        with mock.patch('CardGame.CardGame.GameStatus') as gameStatus:
            gameStatus.return_value = None
            self.assertIsNone(self.cardgame.Get_Winner())





    def tearDown(self):
        pass
