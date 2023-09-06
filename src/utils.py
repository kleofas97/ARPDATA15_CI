class Calculator:

    def __init__(self, a, b):
        if isinstance(a, (int,float)):
            self._a = a
        else:
            raise Exception('wrong parameter a please use only int or float')
        if isinstance(b, (int, float)):
            self._b = b
        else:
            raise Exception('wrong parameter a please use only int or float')

    def dodawanie(self):
        return self._a + self._b
