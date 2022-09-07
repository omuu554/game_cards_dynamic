from Card import Card
import random

class DeckOfCards:

    def __init__(self):
        self.DeckCards = self.CreateDeck()


    def CardShuffle(self):
       random.shuffle(self.DeckCards)

    def IsDeckNotEmpty(self):
        return self.DeckCards


    def CreateDeck(self):
       CardList = []

       for i in range(1, 5):
          for j in range(1, 14):
             NewCard = Card(j,i)
             CardList.append(NewCard)

       return CardList

    def Deal_One(self):
       if(self.IsDeckNotEmpty()):
        Card = random.choice(self.DeckCards)
        self.DeckCards.remove(Card)
        return Card
       return None


