class Organism:
    alive = True

class Animal(Organism):
    
    def eat(self):
        print("Eating")

class Dog(Animal):

    def bark(self):
        print("Barking")

dog = Dog()
print(dog.alive)
dog.eat()