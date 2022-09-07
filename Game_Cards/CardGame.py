from Player import Player
from DeckOfCards import DeckOfCards

class CardGame:
    "creates an object of CardGame"

    def __init__(self,PlayerName1:str = "GuestPlayer", PlayerName2:str = "GuestPlayer", PlayerDeckSize1:int = 26, PlayerDeckSize2:int = 26):
        "card game instantiates 2 players and a deck of cards at instantiation"
        self.Player1 = Player(PlayerName1, PlayerDeckSize1)
        self.Player2 = Player(PlayerName2, PlayerDeckSize2)
        self.DeckOfCards = DeckOfCards()
        self.__New_Game()

    def __New_Game(self):
        "function shuffles the deck of cards and fills the decks of the 2 players"
        self.DeckOfCards.CardShuffle()
        self.Player1.Set_Hand(self.DeckOfCards)
        self.Player2.Set_Hand(self.DeckOfCards)

    def GameStatus(self):
        "function returns 1 if player1 has got the most cards 2 if player2 has got the most cards"
        if (len(self.Player1.PlayerCards) > len(self.Player2.PlayerCards)):
            return 1
        if (len(self.Player1.PlayerCards) < len(self.Player2.PlayerCards)):
            return 2

    def Get_Winner(self):
        "function returns the game winner if its a tie returns None"
        if(self.GameStatus() == 1):
            return self.Player1
        if(self.GameStatus() == 2):
            return self.Player2
        return None


