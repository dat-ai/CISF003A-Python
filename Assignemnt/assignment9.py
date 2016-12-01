"""
Playing Card

Define a class where one object of the class represents one playing card. Your class should have the following methods:

__init__(self, rank, suit)
rank is a number in the range 1-13 indicating the ranks Ace through King, and suit is a single character "d" "c", "h",
or "s" indicating the suit (diamonds, clubs, hearts, or spades). This method creates a card of rank and suit.

getRank(self)
Returns the rank of the card as a word, eg "Three"

getSuit(self)
Returns the suit of the card as a word, eg "Hearts"

bjValue(self)
Returns the Blackjack value of a card. Ace has a blackjack value of 1, face cards all have blackjack value 10. The rest
of the cards have blackjack values that are the same as their rank. The returned value from this method will always be
a number.

__str__(self)
Returns a string containing the full name of the card. For example. "Ace of Spades".

Note that a method named __str__(self), is special in Python. If asked to convert an object into a string, Python calls
this method automatically to do the conversion. For example,

c = PlayingCard(1, "s")
print (c) # automatically calls your __str__() method,
# which returns "Ace of Spades" (without quotes)
Here is a test program that verifies that all of the above methods work:

 c1 = PlayingCard(5,"c") # constructs the card object
 print (c1.getRank()) # outputs "Five"
 print (c1.getSuit()) # outputs "Clubs"
 print (c1.bjValue()) # outputs "5"
 print (c1) # outputs "Five of Clubs"

 c2 = PlayingCard(13, "h") # constructs the card object
 print (c2.getRank()) # outputs "King"
 print (c2.getSuit()) # outputs "Hearts"
 print (c2.bjValue()) # outputs "10"
 print (c2) # outputs "King of Hearts"
In order to receive full credit:
There will be no user input in the entire program
class PlayingCard must have a comment that tells what one object of class PlayingCard represents.
Every method in class PlayingCard must have a comment that tells what the method does.
None of the methods in class PlayingCard will do any printing.
The dictionary that translates from rank numbers and suit letters to words should be a class variable
Rubric

"""


class PlayingCard:
    def __init__(self, rank, suit):
        """

        :param rank:
        :param suit:
        """
        self.ranks = {1: "Ace", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
                      6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
                      11: "Jack", 12: "Queen", 13: "King"}

        self.suits = {'d': "Diamonds", 'c': "Clubs", 'h': "Heart", 's': "Spades"}

        self.rank_value = self.ranks[rank]
        self.suit_value = self.suits[suit]

    def getRank(self):
        """

        :return:
        """
    def getSuit(self):
        """

        :return:
        """

    def bjValue(self):
        """

        :return:
        """
    def __str__(self):
        """

        :return:
        """