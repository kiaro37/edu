
class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            raise ZeroDivisionError("На ноль делить нельзя")
        return a / b

if __name__ == "main":
    a = int(input("Input first number"))
    b = int(input("Input second number"))
    calc = Calculator()
    print(calc.add(a, b))



