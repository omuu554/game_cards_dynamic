from CardGame import CardGame
from Card import Card
import inquirer


class GameManger:

    def __init__(self,Player1Name:str = "GuestPlayer", Player2Name:str = "GuestPlayer", PDeckSize:int = 26):
        self.cardGame = CardGame(Player1Name, Player2Name, PDeckSize)

    def ShowMatch(self, card1: Card, card2: Card):
        print(f"(Player: {self.cardGame.Player1.PlayerName} | card: {card1})       vs       (Player: {self.cardGame.Player2.PlayerName} | card: {card2})\n")


    def DecideRoundWinner(self, card1:Card, card2:Card):
        if (card1 > card2):
            self.cardGame.Player1.Add_Card(card1)
            self.cardGame.Player1.Add_Card(card2)
            print(f"\n{self.cardGame.Player1.PlayerName} won in: {card1} vs {card2}\n")
        else:
            self.cardGame.Player2.Add_Card(card1)
            self.cardGame.Player2.Add_Card(card2)
            print(f"\n{self.cardGame.Player2.PlayerName} won in: {card1} vs {card2}\n")

    def EndGame(self):
        Player1Confirm = {inquirer.Confirm('confirmed1', message=f"{self.cardGame.Player1.PlayerName} do you want to end the game ?",default=True), }
        confirm1 = inquirer.prompt(Player1Confirm)
        Player2Confirm = {inquirer.Confirm('confirmed2', message=f"{self.cardGame.Player2.PlayerName} do you want to end the game ?",default=True), }
        confirm2 = inquirer.prompt(Player2Confirm)
        return confirm1['confirmed1'] and confirm2['confirmed2']

    def refillPlayersDeck(self, card1:Card, card2:Card):
        if (card1 is None and self.cardGame.DeckOfCards.DeckCards):
            self.cardGame.Player1.Reset_Hand(self.cardGame.DeckOfCards)
            card1 = self.cardGame.Player1.Get_Card()

        if (card2 is None and self.cardGame.DeckOfCards.DeckCards):
            self.cardGame.Player2.Reset_Hand(self.cardGame.DeckOfCards)
            card2 = self.cardGame.Player2.Get_Card()

        return card1, card2




    def WinByDefault(self, card1:Card, card2:Card):
        if (card1 is None and not self.cardGame.DeckOfCards.DeckCards):
            self.cardGame.Player2.Add_Card(card2)
            return True
        if (card2 is None and not self.cardGame.DeckOfCards.DeckCards):
            self.cardGame.Player1.Add_Card(card1)
            return True
        return False




    def DecideWinner(self):
        GameWinner = self.cardGame.Get_Winner()
        if(GameWinner is not None):
            print(f"The player that won is \n{GameWinner}")
        else:
            print(f"Its a tie no one won")

    def DrawCards(self):
        return self.cardGame.Player1.Get_Card(), self.cardGame.Player2.Get_Card()





