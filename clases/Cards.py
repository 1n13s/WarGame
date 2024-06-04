class Cards():
    _value:int
    _value_print:str
    _suit:str
    def __init__(self, value:str, suit:str) -> None:
        self._value_print=value
        self._suit=suit
        self._value=self.value_int(value)
    
    def get_card(self):
        print(f"A {self._value_print} of {self._suit}")
    
    @staticmethod
    def value_int(value_str: str) -> int:
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