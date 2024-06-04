class Cards():
    """This class manages the card logic
    """    
    def __init__(self, value:str, suit:str) -> None:
        """Initialices the card class

        Args:
            value (str): The value of the card
            suit (str): The suit of the card
        """
        self._value_print=value
        self._suit=suit
        self._value=self.value_int(value)
    
    def get_card(self):

        print(f"A {self._value_print} of {self._suit}")
    
    @staticmethod
    def compare_cards(value_card_one: int, value_card_two: int):
        if value_card_one>value_card_two:
            return 1
        elif value_card_one<value_card_two:
            return 2
        else: return 3

    @staticmethod
    def value_int(value_str: str) -> int:
        """Obtains the value of the card

        Args:
            value_str (str): Value with string type

        Returns:
            int: The value with int type
        """
        values={
            "J":10,
            "Q":11,
            "K":12,
            "A":13,
            "Jocker":14
        }
        if not values.get(value_str,False):
            return int(value_str)
        else: return values.get(value_str)