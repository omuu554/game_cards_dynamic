from GameManager import GameManger





if __name__ == "__main__":
    playerName1 = input("Please enter the name of the first player: ")
    playerName2 = input("Please enter the name of the second player: ")

    playerDeckSize = input("Please enter an integer for the decksize of the first player (10-26): ")

    gameManager = GameManger(playerName1, playerName2, playerDeckSize)
    Round = 0
    while(True):
      card1, card2 = gameManager.DrawCards()
      Round += 1
      card1, card2 = gameManager.refillPlayersDeck(card1, card2)
      if(gameManager.WinByDefault(card1, card2)):
          break
      print(f"\nRound: {Round}")
      gameManager.ShowMatch(card1, card2)
      gameManager.DecideRoundWinner(card1, card2)
      if(gameManager.EndGame()):
          break

    print(f"Game ended in Round: {Round}")
    gameManager.DecideWinner()



