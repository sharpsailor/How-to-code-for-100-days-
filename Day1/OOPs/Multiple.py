class Prey:

    def flee(self):
        print("This animal flees")
    
    def run(self):
        print("This animal can runn")

class Predators:
    def hunt(self):
        print("This animal is a Hunter")

    def run(self):
        print("This animal can Fly")

class Rabbit(Prey):
    pass

class Hawk(Predators):
    pass

class Fish(Predators,Prey):
    pass

Rabbit = Rabbit()
Hawk= Hawk()
Fish= Fish()

Rabbit.flee()
Hawk.hunt()
Fish.run()