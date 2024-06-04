class Cards():
    """This class manages the card logic
    """    
    def __init__(self, value:str, suit:str) -> None:
        """Initialices the card class

        Args:
            value (str): The value of the card
            suit (str): The suit of the card
        """

        self.__value_print=value
        self.__suit=suit
        self.__value=self.value_int(value)
    
    def print_card(self) -> None:
        """Prints the card
        """

        print(f"{self.__suit} {self.__value_print}")
    
    def get_value(self) -> int:
        """Gets the value of the card

        Returns:
            int: The value of the card
        """

        return self.__value

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

