from typing import Any
from clases.deck import Deck

class Player():
    """This class manages the player logic
    """
    def __init__(self, name: str, deck: Deck) -> None:
        """Initializes the player

        Args:
            name (str): Name of the player
            deck (list): The deck of the player
        """
        self.__name = name
        self.__deck = deck
        self.__loose = False
    
    def print_deck(self) -> None:
        """Prints the deck of the player
        """

        self.__deck.print_deck()
    
    def get_name(self) -> str:
        """Gets the name of the player

        Returns:
            str: The name of the player
        """

        return self.__name
    
    def validate_loose(self) -> bool:
        """Gets player loose validation

        Returns:
            bool: The loose validation
        """

        if self.__deck.get_deck_len() == 0:
            self.__loose=True

        return self.__loose