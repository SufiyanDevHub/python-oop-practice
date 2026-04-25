class Calculator:
    def __init__(self):
        self.result = 0

    def __validate(self,num):
        if not isinstance(num,(int,float)):
            return False
        
        return True

    def add(self,num):
        if self.__validate(num):
            self.result = self.result + num
        else:
            print("Invalid number")

calc = Calculator()
calc.add(20)
calc.add(30)
print(calc.result)
