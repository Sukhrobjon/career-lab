class Calculator():
    
    def __init__(self):
        pass

    def add(self, val1, val2):
        try:
            return val1 + val2
        except:
            raise ValueError("Not int")

    def subtract(self, val1, val2):
        val1 = self._checker(val1)
        val2 = self._checker(val2)
        if val1 and val2:
            return val1 - val2

    def multiply(self, val1, val2):
        val1 = self._checker(val1)
        val2 = self._checker(val2)
        if val1 and val2:
            return val1 * val2

    def divide(self, val1, val2):
        if val2 == 0:
            raise ValueError("0 division error.")
        val1 = self._checker(val1)
        val2 = self._checker(val2)
        if val1 and val2:
            return val1 / val2

    def _checker(self, val):
        
        if type(val) is int:
            return val
        elif type(val) is float:
            return val
        # convert string representation of number to float
        try:
            return float(val)
        except ValueError:
            return False
        # # convert string number to float
        # try:
        #     return int(val)
        # except ValueError:
        #     return False
        


obj = Calculator()
result = obj._checker("2.0")
print(result)

