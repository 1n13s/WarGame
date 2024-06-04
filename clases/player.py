from typing import Any
from clases.deck import Deck
from clases.cards import Cards

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
        self.__deck.print_deck()

    def get_name(self) -> str:
        """Gets the name of the player

        Returns:
            str: The name of the player
        """

        return self.__name
    
    def add_card(self, card: list[Cards]) -> None:
        self.__deck.add_card(card)

    def obtain_card(self) -> Cards:
        """Obtains a card from the deck

        Returns:
            Cards: A card of the deck
        """
        card=self.__deck.obtain_card()
        card.print_card()

        return card
    
    def validate_loose(self) -> bool:
        """Gets player loose validation

        Returns:
            bool: The loose validation
        """

        if self.__deck.get_deck_len() == 0:
            self.__loose=True

        return self.__loose