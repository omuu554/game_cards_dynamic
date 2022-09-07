from Card import Card
from CardGame import CardGame
from Player import Player

def ActionsOfWinner(card1:Card, card2:Card, player1:Player ,player2:Player):
    if (card1 > card2):
        cardGame.Player1.Add_Card(card1)
        cardGame.Player1.Add_Card(card2)
        print(f"\n{player1.PlayerName} won in: {card1} vs {card2}\n")
    else:
        cardGame.Player2.Add_Card(card1)
        cardGame.Player2.Add_Card(card2)
        print(f"\n{player2.PlayerName} won in: {card1} vs {card2}\n")


def CardGameManager(cardGame:CardGame):
    for Round in range(10):
        p1Card = cardGame.Player1.Get_Card()
        p2Card = cardGame.Player2.Get_Card()
        print(f"\n(Player: {cardGame.Player1.PlayerName} | card: {p1Card})       vs       (Player: {cardGame.Player2.PlayerName} | card: {p2Card})\n")
        ActionsOfWinner(p1Card, p2Card, cardGame.Player1, cardGame.Player2)
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

    playerDeckSize1 = input("Please enter an integer for the decksize of the first player (10-26): ")
    playerDeckSize2 = input("Please enter an integer for the decksize of the second player (10-26): ")

    cardGame = CardGame(playerName1,playerName2,playerDeckSize1,playerDeckSize2)
    GameWinner = CardGameManager(cardGame)

    if(GameWinner is not None):
     print(f"\nThe player that won is \n{GameWinner}")
    else:
     print(f"Its a tie no one won")



