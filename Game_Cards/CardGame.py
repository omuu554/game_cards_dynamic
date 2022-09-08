from Player import Player
from DeckOfCards import DeckOfCards

class CardGame:
    "creates an object of CardGame"

    def __init__(self,PlayerName1:str = "GuestPlayer", PlayerName2:str = "GuestPlayer", PlayerDeckSize:int = 26):
        "card game instantiates 2 players and a deck of cards at instantiation"
        PlayerName1,PlayerName2 = self.__IsNamesTheSame(PlayerName1,PlayerName2)

        self.Player1 = Player(PlayerName1, PlayerDeckSize)
        self.Player2 = Player(PlayerName2, PlayerDeckSize)
        self.DeckOfCards = DeckOfCards()

        self.Player1.PlayerName,self.Player2.PlayerName = self.__IsNamesTheSame( self.Player1.PlayerName, self.Player2.PlayerName)

        self.__New_Game()

    def __IsNamesTheSame(self,NamePlayer1:str, NamePlayer2:str):
        "checks if the players name is the same and changes it if it does"
        if(str(NamePlayer1) == str(NamePlayer2)):
            NamePlayer1 = NamePlayer1 + "(1)"
            NamePlayer2 = NamePlayer2 + "(2)"

        return NamePlayer1,NamePlayer2


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




