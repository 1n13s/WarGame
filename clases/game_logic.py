from clases.cards import Cards
from clases.deck import Deck
from clases.player import Player
from tools.tools import *

class GameLogic():
    """This class manages the logic of the game
    """

    def __init__(self) -> None:
        
        self.__end_game=False
        self.start_game()

    def start_game(self) -> None:
        print("Inicia el juego")
        complete_deck = Deck(self.create_complete_deck())
        deck_divided = complete_deck.divide_complete_deck()

        self.turn_manager(
            Player(self.validate_player_name(1), Deck(deck_divided["player_1"])),
            Player(self.validate_player_name(2), Deck(deck_divided["player_2"]))
        )
    
    def validate_player_name(self, player: int) -> str:
        """Validates the name of the player

        Args:
            player (int): Number of player

        Returns:
            str: The name validated
        """

        try:
            name=input(f"Ingresa el nombre del jugador {player}: ")
            return f"player{player}" if name == "" else name
        except Exception:
            Exception
    
    def turn_manager(self, player_1: Player, player_2: Player):
        
        while not self.__end_game:

            print(f"{player_1.get_name()}:")
            card_1 = player_1.obtain_card()

            print(f"{player_2.get_name()}:")
            card_2 = player_2.obtain_card()

            winner=self.compare_cards(card_1.get_value(),card_2.get_value())

            if winner == 1:
                print("Player 1 wins")
                player_1.add_card([card_1,card_2])

            elif winner == 2:
                print("Player 2 wins")
                player_2.add_card([card_1,card_2])

            else: print("Draw")

            if player_1.validate_loose() or player_2.validate_loose():
                self.__end_game=True
        
        print("Player_1")
        player_1.print_deck()
        print("Player_2")
        player_2.print_deck()
    
    @staticmethod
    def compare_cards(value_card_one: int, value_card_two: int):
        if value_card_one>value_card_two:
            return 1
        elif value_card_one<value_card_two:
            return 2
        else: return 3

    @staticmethod
    def create_complete_deck():
        suits=("Hearts","Diamonds","Spades","Clubs")
        values = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"}
        deck_cards= [
            Cards(value, suit)
            for suit, value in itertools.product(suits, values)
        ]
        deck_cards.extend([Cards("Jocker",""),Cards("Jocker","")])
        return deck_cards
