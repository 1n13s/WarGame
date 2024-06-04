from clases.cards import Cards
from typing import Dict,List
import random
class Deck():
    """This class manages the Deck logic
    """

    def __init__(self, list_deck: list) -> None:
        """Initializes the deck

        Args:
            list_deck (list): A list of a deck
        """

        self.__deck=list_deck
    
    def print_deck(self) -> None:
        """Prints the deck
        """

        for card in self.__deck:
            card.print_card()

    def get_deck_len(self) -> int:
        """Gets the len of the deck

        Returns:
            int: The len of the deck
        """

        return len(self.__deck)

    def add_card(self, card: list[Cards]) -> None:
        self.__deck.extend(card)

    def obtain_card(self) -> Cards:
        """Obtains a card from the deck

        Returns:
            Cards: The card obtained
        """

        return self.__deck.pop()

    def divide_complete_deck(self) -> Dict[str,List[Cards]]:
        """Divides a complete deck

        Returns:
            Dict[str,List[Cards]]: A dict with the deck of player_1 and player_2
        """
        
        print("Dividiendo el maso inicial...")
        random.shuffle(self.__deck)
        return {
                "player_1": self.__deck[:(len(self.__deck)//2)],
                "player_2": self.__deck[(len(self.__deck)//2):]
        }

    
    

    
    
