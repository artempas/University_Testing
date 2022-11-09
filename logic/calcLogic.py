class CalcLogic:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def sum(self) -> float:
        if type(self.a) in [float, int] and type(self.b) in [float, int]:
            return self.a + self.b
        raise TypeError

    def subtract(self) -> float:
        if type(self.a) in [float, int] and type(self.b) in [float, int]:
            return self.a - self.b
        raise TypeError

    def multiply(self) -> float:
        if type(self.a) in [float, int] and type(self.b) in [float, int]:
            return self.a * self.b
        raise TypeError

    def divide(self) -> float:
        if type(self.a) in [float, int] and type(self.b) in [float, int]:
            if self.b != 0:
                return self.a / self.b
            else:
                raise ZeroDivisionError
        else:
            raise TypeError
