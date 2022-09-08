from Card import Card
from CardGame import CardGame
import inquirer

def ActionsOnRoundWinner(card1:Card, card2:Card,cardGame:CardGame):

    if (card1 > card2):
        cardGame.Player1.Add_Card(card1)
        cardGame.Player1.Add_Card(card2)
        print(f"\n{cardGame.Player1.PlayerName} won in: {card1} vs {card2}\n")
    else:
        cardGame.Player2.Add_Card(card1)
        cardGame.Player2.Add_Card(card2)
        print(f"\n{cardGame.Player2.PlayerName} won in: {card2} vs {card1}\n")

def ActionsRefillPlayerDeck(card1:Card, card2:Card, cardGame:CardGame):
    if (card1 is None and cardGame.DeckOfCards.DeckCards):
        cardGame.Player1.Reset_Hand(cardGame.DeckOfCards)
        card1 = cardGame.Player1.Get_Card()

    if (card2 is None and cardGame.DeckOfCards.DeckCards):
        cardGame.Player2.Reset_Hand(cardGame.DeckOfCards)
        card2 = cardGame.Player2.Get_Card()

    return card1,card2

def EndGame(cardGame:CardGame):
    Player1Confirm = {inquirer.Confirm('confirmed1',message=f"{cardGame.Player1.PlayerName} do you want to end the game ?", default=True), }
    confirm1 = inquirer.prompt(Player1Confirm)
    Player2Confirm = {inquirer.Confirm('confirmed2', message=f"{cardGame.Player2.PlayerName} do you want to end the game ?", default=True), }
    confirm2 = inquirer.prompt(Player2Confirm)
    return confirm1['confirmed1'] and confirm2['confirmed2']



def CardGameManager(cardGame:CardGame):
    Round = 0
    while(True):
        p1Card = cardGame.Player1.Get_Card()
        p2Card = cardGame.Player2.Get_Card()
        Round += 1
        p1Card,p2Card = ActionsRefillPlayerDeck(p1Card, p2Card, cardGame)

        if (p1Card is None and not cardGame.DeckOfCards.DeckCards):
            cardGame.Player2.Add_Card(p2Card)
            break
        if (p2Card is None and not cardGame.DeckOfCards.DeckCards):
            cardGame.Player1.Add_Card(p1Card)
            break
        print(f"\nRound: {Round}")
        print(f"(Player: {cardGame.Player1.PlayerName} | card: {p1Card})       vs       (Player: {cardGame.Player2.PlayerName} | card: {p2Card})\n")
        ActionsOnRoundWinner(p1Card, p2Card, cardGame)
        if(EndGame(cardGame)):
            break

        # if(p1Card > p2Card ): # THE FUNCTION ABOVE DOES THE SAME THING
        #     cardGame.Player1.Add_Card(p1Card)
        #     cardGame.Player1.Add_Card(p2Card)
        #     print(f"\n{cardGame.Player1.PlayerName} won in: {p1Card} vs {p2Card}\n")
        # else:
        #     cardGame.Player2.Add_Card(p1Card)
        #     cardGame.Player2.Add_Card(p2Card)
        #     print(f"\n{cardGame.Player2.PlayerName} won in: {p1Card} vs {p2Card}\n")

    return cardGame.Get_Winner()


if __name__ == "__main__":
    playerName1 = input("Please enter the name of the first player: ")
    playerName2 = input("Please enter the name of the second player: ")

    playerDeckSize = input("Please enter an integer for the decksize of the first player (10-26): ")


    cardGame = CardGame(playerName1,playerName2,playerDeckSize)
    GameWinner = CardGameManager(cardGame)

    if(GameWinner is not None):
     print(f"\nThe player that won is \n{GameWinner}")
    else:
     print(f"Its a tie no one won")





