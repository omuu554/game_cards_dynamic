

class Card:
    "A card object"

    def __init__(self,value:int, suit:int):
        "creates a card with a symbol and a suit it also holds what kind of value a card is at instantiation"
        self.__RaiseErrorNotDigit(value, suit) #raises exeption if value or suit are not int digits
        self.__RaiseErrorBadValue(value)# raises execption if value is invalid
        self.__RaiseErrorBadSuit(suit) # raises execption if suit is invalid

        self.Value = value
        self.Suit = suit
        self.__StringValues = {'1': 'Ace', '2':'2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '10': '10', '11': 'Prince', '12': 'Queen', '13': 'King'}# dictionary with to convert value to string
        self.__StringSuits = {'1': 'Diamonds','2':'Spades', '3':'Hearts', '4': 'Clubs'} # dictionary with to convert suit to string

    def __RaiseErrorNotDigit(self, *Numbers):
        "function raises exeption if the values entered are not digits from the type int"
        for Num in Numbers:
            if (not str(Num).isdigit() or type(Num) != int):
                raise TypeError("Card can only get integer numbers")

    def __RaiseErrorBadValue(self, value):
        "function raises exeption if the value entered is smaller than 1 or is bigger than 13"
        if(value < 1 or value > 13):
            raise TypeError("value cannot be smaller than 1 or bigger than 13")

    def __RaiseErrorBadSuit(self, value):
        "function raises exeption if the suit entered is smaller than 1 or is bigger than 5"
        if(value < 1 or value > 5):
            raise TypeError("value cannot be smaller than 1 or bigger than 5")

    def __eq__(self, other):
        "function checks if the card equals to other card"
        return self.Value == other.Value and self.Suit == other.Suit


    def __gt__(self, other):
        "function checks if the card is greater than the other card"
        if(self.Value == other.Value):
            return self.Suit > other.Suit

        if(self.Value == 1):
            return True

        if(other.Value == 1):
            return False

        return self.Value > other.Value

    def __str__(self):
       "function returns a string value of the current card"
       return f"{self.__StringValues[str(self.Value)]} of {self.__StringSuits[str(self.Suit)]}"



    # def __repr__(self): #used for testing purposes
    #      return f"{self.Value},{self.Suit} "





# c = Card(13,2) used for testing purposes
# print(c)

