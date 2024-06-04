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
        

def divide_deck(deck:list[Cards]):
        random.shuffle(deck)
        deck_player_1 = deck[:(len(deck)//2)]
        deck_player_2 = deck[(len(deck)//2):]
        return {
                "player_1": deck_player_1,
                "player_2": deck_player_2
        }

def print_deck(deck:list[Cards]):
        for card in deck:
                card.get_card()