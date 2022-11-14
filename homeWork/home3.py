class Add:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return self.val + other.val


class Sub:
    def __init__(self, val):
        self.val = val

    def __sub__(self, other):
        return self.val - other.val


class Mul:
    def __init__(self, val):
        self.val = val

    def __mul__(self, other):
        return self.val * other.val


class TrueDiv:
    def __init__(self, val):
        self.val = val

    def __truediv__(self, other):
        return self.val / other.val


class Test(Add, Sub, Mul, TrueDiv):
    def __init__(self, val):
        Add.__init__(self, val)
        Sub.__init__(self, val)
        Mul.__init__(self, val)
        TrueDiv.__init__(self, val)


number1 = Test(12)
number2 = Test(4)

print(f'{number1 + number2}\n'
      f'{number1 - number2}\n'
      f'{number1 * number2}\n'
      f'{number1 / number2}\n')
