from SingletonMeta import SingletonMeta

class mysingleton(metaclass=SingletonMeta):
    a = None
    b = None
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b

s1 = mysingleton(1, 2)
print(s1.a, s1.b)
s2 = mysingleton()
print(s2.a, s2.b)
