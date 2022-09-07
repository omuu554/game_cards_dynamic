
from CardGame import CardGame


def RoundWinner():
    pass




if __name__ == "__main__":
    playerName1 = input("Please enter the name of the first player: ")
    playerName2 = input("Please enter the name of the second player: ")

    playerDeckSize1 = input("Please enter an integer for the decksize of the first player (10-26): ")
    playerDeckSize2 = input("Please enter an integer for the decksize of the second player (10-26): ")

    cardGame = CardGame(playerName1,playerName2,playerDeckSize1,playerDeckSize2)
    for Round in range(10):
        p1Card = cardGame.Player1.Get_Card()
        p2Card = cardGame.Player2.Get_Card()
        print(f"\n({cardGame.Player1.PlayerName} card: {p1Card}       vs       {cardGame.Player2.PlayerName} card: {p2Card})\n")
        if(p1Card > p2Card ):
            cardGame.Player1.Add_Card(p1Card)
            cardGame.Player1.Add_Card(p2Card)
            print(f"\n({cardGame.Player1.PlayerName} won: {p1Card}, {p2Card})\n")
        else:
            cardGame.Player2.Add_Card(p1Card)
            cardGame.Player2.Add_Card(p2Card)
            print(f"\n({cardGame.Player2.PlayerName} won: {p1Card}, {p2Card})\n")

    print(f"\nThe player that won is {cardGame.Get_Winner()}")



