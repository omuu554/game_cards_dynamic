from DeckOfCards import DeckOfCards
from Card import Card
import random
import re
class Player:
    "A player object"

    def __init__(self,PlayerName:str = "GuestPlayer", PlayerDeckStartSize:int = 26):
        "creates the name,deck,and decksize at instantiation"
        PlayerDeckSize = self.__PlayerDeckSizeNotInteger(PlayerDeckStartSize)#reset decksize to 26 if given decksize is not an integer
        PlayerDeckSize = self.__PlayerDeckSizeBad(PlayerDeckSize)#reset decksize to 26 if decksize is smaller than 10 or bigger than 26
        PlayerName = self.__PlayerNameIsEmpty(PlayerName)

        self.PlayerName = str(PlayerName)
        self.DeckSize = int(PlayerDeckSize)
        self.PlayerCards = []


    def __RaiseErrorIfNotDeckOfCards(self, Deck:DeckOfCards):
        "function raises exeption if deck size if Deck is not of type DeckOfCards"
        if(type(Deck) != DeckOfCards):
            raise TypeError("The Deck you have entered is not of type DeckOfCards")
    def __RaiseErrorIfNotCard(self,card:Card):
        "function raises exeption if deck size if card is not of type Card"
        if(type(card) != Card):
            raise TypeError("The card you have entered is not of type Card")
    def __ActionAddCard(self,Card:Card):
        "function adds a card to the deck of the player"
        self.PlayerCards.append(Card)

    def __PlayerDeckSizeNotInteger(self, DeckSize:int):
        "function returns fixed decksize if the given one is not an integer"
        if(not str(DeckSize).isdigit()):
            DeckSize = 26

        return DeckSize

    def __PlayerDeckSizeBad(self, DeckSize:int):
        "function returns fixed decksize if the given one is smaller than 10 or bigger than 26"
        if(int(DeckSize) < 10 or int(DeckSize) > 26):
            DeckSize = 26

        return DeckSize

    def __PlayerNameIsEmpty(self, NameOfPlayer):
        "function checks if the given player name is empty and changes it if it does"

        if(re.sub(' +', ' ',str(NameOfPlayer)) == ""):
            NameOfPlayer = "GuestPlayer"

        return " ".join(str(NameOfPlayer).split())


    def __str__(self):
        "function returns player status"
        return f"Player: {self.PlayerName}\nCardsAmount: {len(self.PlayerCards)} "
    def IsPlayerDeckNotEmpty(self):
        "function checks if the deck of the player is empty"
        return self.PlayerCards


    def Set_Hand(self, CardsDeck:DeckOfCards):
        "function fills the deck of the player from a given DeckOfCards"
        self.__RaiseErrorIfNotDeckOfCards(CardsDeck) # checks if CardsDeck is of type DeckOfCards

        for i in range(self.DeckSize):
            card = CardsDeck.Deal_One()
            if(card is not None): #Deal_One could return None so check for it is required before adding a card
             self.Add_Card(card) # function adds a card to the deck of the player

    def __Set_Hand_WhatsLeft(self , CardsDeck:DeckOfCards):
        "function takes whats left of the deck and fills the hand of the player"
        for i in range(len(CardsDeck.DeckCards)):
            card = CardsDeck.Deal_One()
            if (card is not None):
                self.Add_Card(card)

    def IsDeckSizeSmallerCurrDeck(self , CardsDeck:DeckOfCards):
        return self.DeckSize < len(CardsDeck.DeckCards)
    def Reset_Hand(self, CardsDeck:DeckOfCards):
        "function fills the deck of the player with the same amount if it is not in the deck than with what that is left"
        self.__RaiseErrorIfNotDeckOfCards(CardsDeck)

        if(self.IsDeckSizeSmallerCurrDeck(CardsDeck)):
                self.Set_Hand(CardsDeck)
        else:
                self.__Set_Hand_WhatsLeft(CardsDeck)

    def Get_Card(self):
       "funtion returns a card and removes the card for the players deck if no card is found returns None"
       if(self.IsPlayerDeckNotEmpty()):# checks if the player deck is empty
        card = random.choice(self.PlayerCards)
        self.PlayerCards.remove(card)
        return card

       return None

    def Add_Card(self, card:Card):
        "function adds a card to the players deck"
        self.__RaiseErrorIfNotCard(card)# checks if the card given to add is of type Card
        self.__ActionAddCard(card) #an action to add the card to the players deck




