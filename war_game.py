from clases.cards import Cards
from clases.deck import Deck
from tools.tools import *
from clases.player import Player

complete_deck = Deck(create_complete_deck())

player_1=Player("player1", Deck(complete_deck.divide_complete_deck()["player_1"]))
player_2=Player("player2", Deck(complete_deck.divide_complete_deck()["player_2"]))

print("Player 1")
player_1.print_deck()

print("\nPlayer 2")
player_2.print_deck()
