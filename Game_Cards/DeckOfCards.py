from Card import Card
import random

class DeckOfCards:
    "A deck of cards object"

    def __init__(self):
        "creates a deck of cards at instantiation"
        self.DeckCards = self.CreateDeck()


    def CardShuffle(self):
       "the function shuffles the deck"
       random.shuffle(self.DeckCards)

    def IsDeckNotEmpty(self):
        "function checks if the deck is not empty"
        return self.DeckCards


    def CreateDeck(self):
       "function creates a deck of cards"
       CardList = []

       for i in range(1, 5):
          for j in range(1, 14):
             NewCard = Card(j,i)
             CardList.append(NewCard)

       return CardList

    def Deal_One(self):
       "function returns a card and removes the card from the deck"
       if(self.IsDeckNotEmpty()):
        Card = random.choice(self.DeckCards)
        self.DeckCards.remove(Card)
        return Card
       return None


