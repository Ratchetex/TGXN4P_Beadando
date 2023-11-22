
import math


class Calculate:
    x = 0
    y = 0
    operand = ""

    def add(self):
        value = float(self.x + self.y)
        return value

    def subtract(self):
        value = float(self.x - self.y)
        return value

    def multiply(self):
        value = float(self.x * self.y)
        return value

    def divide(self):
        value = float(self.x / self.y)
        return value

    def square(self):
        value = float(math.sqrt(self.x))
        return value

    def pow2(self):
        value = float(math.pow(self.x, 2))
        return value

    def pow3(self):
        value = float(math.pow(self.x, 3))
        return value

    def result(self):
        match self.operand:
            case '+':
                return self.add()
            case '-':
                return self.subtract()
            case '*':
                return self.multiply()
            case '/':
                return self.divide()
            case '2':
                return self.pow2()
            case '3':
                return self.pow3()
            case 's':
                return self.square()

