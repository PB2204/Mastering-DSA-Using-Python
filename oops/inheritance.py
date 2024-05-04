# Single Inheritance
class A1:
    def methodA1(self):
        print("Method A1 !")

class B1(A1): # Passing A1 class to B1
    def methodB1(self):
        print("Method B1 !")

singleInheritance = B1()
singleInheritance.methodA1()
singleInheritance.methodB1()

# Multi-Level Inheritance
class A2:
    def methodA2(self):
        print("Method A2 !")

class B2(A2):
    def methodB2(self):
        print("Method B2 !")

class C2(B2):
    def methodC2(self):
        print("Method C2 !")

multiLevelInheritance = C2()
multiLevelInheritance.methodA2()
multiLevelInheritance.methodB2()
multiLevelInheritance.methodC2()

# Multiple inheritance

class A3:
    def methodA3(self):
        print("Method A3 !")

class B3:
    def methodB3(self):
        print("Method B3 !")

class C3(A3, B3):
    def methodC3(self):
        print("Method C3 !")

multipleInheritance = C3()
multipleInheritance.methodA3()
multipleInheritance.methodB3()
multipleInheritance.methodC3()