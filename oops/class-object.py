class DemoClass:
    a = 10

    def sum2Nums(self, a, b):
        print(a + b)

showValue = DemoClass()
print(showValue.a)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

showValue.sum2Nums(x, y)