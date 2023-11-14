class Animal:

    alive = True
    def eat(self):
        print("This animal is eating")
    
    def slumber(self):
        print("This animal is slumber")

class Rabbit(Animal): # Child(Parent) --> This is how you inhrit parent class to child class    

    def run(self):
        print("This Rabbit is running")

class Fish(Animal):

    def Swim(self):
        print("This Fish is swimming")
class Hawk(Animal):

    def fly(self):
        print("This Hawk is flying")


rabbit = Rabbit()
fish = Fish()
Hawk = Hawk()

rabbit.run()
fish.Swim()
Hawk.fly()