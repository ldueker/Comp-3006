'''
The Game designed here is based on the popular game go fish.  In this game, player1(user) plays against the Computer who
is randomly guessing cards.  The game alters from the well-known game in that the player has to specifically ask for the suit
as well as the card value for the program to work effectively.  The user must input, for example, "9-Spades" for the program
to accurately check if the computer has the 9 of Spades in its hand.  At the end of the game, the program adds the sets of the player
and the computer and outputs the winner (who has more sets of 4 cards of the same value).  Deck.py is used to create a deck of cards
in a list format while Game.py executes the game.
'''

import Deck
import random

#Making the deck for the game
game_deck = Deck.MakeDeck()

#Full deck for computer to make guesses out of
full_deck = Deck.MakeDeck()


#Class to keep track of player's (and Computer's) name, hand, and sets
class Player():
#Creation of Shallow Copies
    def __init__(self):
        self.name = ""
        self.hand = []
        self.sets = []
#Function for asking Computer for a card
def ask(player, gameCount=0):
    while gameCount != 1:
        askP = input("What card would you like to ask for?")
        #Player1 adds 1 card to its hand from game_deck if Computer doesnt have asked for card
        if askP not in Computer.hand:
            print("Computer does not have ",askP,", you must go fish")
            draw(player1)
            gameCount += 1
            print(player1.hand)
        #Player1 takes asked for card from Computers hand
        if askP in Computer.hand:
            print("Computer has ",askP)
            Computer.hand.remove(askP)
            player1.hand.append(askP)
            print(player1.hand)


#Function for Computer Asking Player for a card
def askComp(player,gameCount=0):
    while gameCount != 1:
        #Ensures computer guesses random card every time
        random.shuffle(full_deck)
        askC = full_deck[3]
        print("Computer asks for",askC)

        #Computer adds 1 card to its hand from game_deck if player1 doesnt have asked for card
        if askC not in player1.hand:
            print(player1.name," does not have ",askC,", Computer must go fish")
            draw(Computer)
            gameCount += 1
        #Computer takes asked for card from player1's hand
        if askC in player1.hand:
            print(player1.name," has ",askC)
            player1.hand.remove(askC)
            Computer.hand.append(askC)



#Function for drawing 1 card from the game deck
def draw(player):
    card = game_deck.pop()
    player.hand.append(card)

#Game Function
def playGame(player1,Computer,deck):
    #references for rules of the game
    hand_size = 7
    card_dealt = 0
    gameCount = 0

    #Dealing of first hand
    while card_dealt < hand_size:
        draw(player1)
        draw(Computer)
        card_dealt+=1
    print(player1.name,"Hand:")
    print(player1.hand)
    print(player1.name,"Goes First")
    while len(game_deck) != 0:
        ask(player1)
        askComp(Computer)

#initializing the players using the Player() class
player1 = Player()
player1.name = input ("Enter name of Player 1")

Computer = Player()
Computer.name = "Computer"

playGame(player1,Computer,game_deck)

#Empty sets to be populated with groups of 4 cards to signify a point
player1_sets =[]
Computer_sets = []
#Checking if Player hand has sets
if 'Ace-Spades' and 'Ace-Diamonds' and 'Ace-Clubs' and 'Ace-Hearts' in player1.hand:
    player1_sets.append('Aces')
if '2-Spades' and '2-Diamonds' and '2-Clubs' and '2-Hearts' in player1.hand:
    player1_sets.append('2s')
if '3-Spades' and '3-Diamonds' and '3-Clubs' and '3-Hearts' in player1.hand:
    player1_sets.append('3s')
if '4-Spades' and '4-Diamonds' and '4-Clubs' and '4-Hearts' in player1.hand:
    player1_sets.append('4s')
if '5-Spades' and '5-Diamonds' and '5-Clubs' and '5-Hearts' in player1.hand:
    player1_sets.append('5s')
if '6-Spades' and '6-Diamonds' and '6-Clubs' and '6-Hearts' in player1.hand:
    player1_sets.append('6s')
if '7-Spades' and '7-Diamonds' and '7-Clubs' and '7-Hearts' in player1.hand:
    player1_sets.append('7s')
if '8-Spades' and '8-Diamonds' and '8-Clubs' and '8-Hearts' in player1.hand:
    player1_sets.append('8s')
if '9-Spades' and '9-Diamonds' and '9-Clubs' and '9-Hearts' in player1.hand:
    player1_sets.append('9s')
if '10-Spades' and '10-Diamonds' and '10-Clubs' and '10-Hearts' in player1.hand:
    player1_sets.append('10s')
if 'Jack-Spades' and 'Jack-Diamonds' and 'Jack-Clubs' and 'Jack-Hearts' in player1.hand:
    player1_sets.append('Jacks')
if 'Queen-Spades' and 'Queen-Diamonds' and 'Queen-Clubs' and 'Queen-Hearts' in player1.hand:
    player1_sets.append('Queens')
if 'King-Spades' and 'King-Diamonds' and 'King-Clubs' and 'King-Hearts' in player1.hand:
    player1_sets.append('Kings')



#Checking if Computer has sets
if 'Ace-Spades' and 'Ace-Diamonds' and 'Ace-Clubs' and 'Ace-Hearts' in Computer.hand:
            Computer_sets.append('Aces')
if '2-Spades' and '2-Diamonds' and '2-Clubs' and '2-Hearts' in Computer.hand:
            Computer_sets.append('2s')
if '3-Spades' and '3-Diamonds' and '3-Clubs' and '3-Hearts' in Computer.hand:
            Computer_sets.append('3s')
if '4-Spades' and '4-Diamonds' and '4-Clubs' and '4-Hearts' in Computer.hand:
            Computer_sets.append('4s')
if '5-Spades' and '5-Diamonds' and '5-Clubs' and '5-Hearts' in Computer.hand:
            Computer_sets.append('5s')
if '6-Spades' and '6-Diamonds' and '6-Clubs' and '6-Hearts' in Computer.hand:
            Computer_sets.append('6s')
if '7-Spades' and '7-Diamonds' and '7-Clubs' and '7-Hearts' in Computer.hand:
            Computer_sets.append('7s')
if '8-Spades' and '8-Diamonds' and '8-Clubs' and '8-Hearts' in Computer.hand:
            Computer_sets.append('8s')
if '9-Spades' and '9-Diamonds' and '9-Clubs' and '9-Hearts' in Computer.hand:
            Computer_sets.append('9s')
if '10-Spades' and '10-Diamonds' and '10-Clubs' and '10-Hearts' in Computer.hand:
            Computer_sets.append('10s')
if 'Jack-Spades' and 'Jack-Diamonds' and 'Jack-Clubs' and 'Jack-Hearts' in Computer.hand:
            Computer_sets.append('Jacks')
if 'Queen-Spades' and 'Queen-Diamonds' and 'Queen-Clubs' and 'Queen-Hearts' in Computer.hand:
            Computer_sets.append('Queens')
if 'King-Spades' and 'King-Diamonds' and 'King-Clubs' and 'King-Hearts' in Computer.hand:
            Computer_sets.append('Kings')

print(player1_sets)
print(Computer_sets)

#Winner is selected by who has more sets of the same value (ie 4 Aces, 4 Kings, etc.)
if len(player1_sets) > len(Computer_sets):
    print(player1.name,"wins")
if len(Computer_sets) < len(player1_sets):
    print("Computer wins")
if len(player1_sets) == len(Computer_sets):
    print("Game is a Draw")
