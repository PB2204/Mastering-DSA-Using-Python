# Overloading

class MMV:
    def printing(self, name=" "):
        print("Welcome To Manbhum Mahavidyalaya " + name + "!")

manbhum = MMV()
manbhum.printing() # Output: Welcome To Manbhum Mahavidyalaya !
manbhum.printing("Pabitra") # Output: Welcome To Manbhum Mahavidyalaya Pabitra!


# Overriding

class CS(MMV):
    def printing(self, name=" "):
        super().printing(name)
        print("Welcome To CS Dept of Manbhum Mahavidyalaya " + name + "!")

cs = CS()
cs.printing() # Output: Welcome To CS Dept of Manbhum Mahavidyalaya !
cs.printing("Pabitra") # Output: Welcome To CS Dept of Manbhum Mahavidyalaya Pabitra!