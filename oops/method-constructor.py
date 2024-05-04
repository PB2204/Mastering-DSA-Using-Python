class DemoClass:
    def __init__(self):
        self.a = 10

    def printValue(self):
        self.c = self.a * self.a  # Define c as an attribute of the class
        print(self.c)

    def valueOfC(self):
        print(self.c)

obj = DemoClass()
obj.printValue()
obj.valueOfC()