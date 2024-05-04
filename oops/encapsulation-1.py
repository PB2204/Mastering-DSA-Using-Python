class Student:
    def __init__(self):
        self.__name = "Bokachoda"

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def display(self):
        print("Hello", self.__name, "!")

student = Student()
boka = student.getName()
print(boka)
student.setName("Pabitra")
student.display()
