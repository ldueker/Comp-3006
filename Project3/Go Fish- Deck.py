import random

def MakeDeck():
    deck = []
    card_values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    card_suits = ["Hearts", "Spades", "Diamonds", "Clubs"]

    for x in card_values:
        for y in card_suits:
            deck.append(str(x)+'-'+str(y))

    random.shuffle(deck)

    return deck
