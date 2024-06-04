import itertools
from clases.cards import Cards
import random
def create_complete_deck():
        suits=("Hearts","Diamonds","Spades","Clubs")
        values = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"}
        deck_cards= [
            Cards(value, suit)
            for suit, value in itertools.product(suits, values)
        ]
        deck_cards.extend([Cards("Jocker",""),Cards("Jocker","")])
        return deck_cards
