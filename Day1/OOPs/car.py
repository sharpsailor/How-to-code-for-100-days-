class Car:
    wheels = 4 # Class Varibale 
    def __init__(self,make,model,year,color):
        self.make = make # Instance varible --> can be given Unique Values and always declared inside constructors
        self.model=model
        self.year = year
        self.color = color
    
    def drive(self):
        print("This "+self.model +" is driving")

    def stop(self):
        print("This "+self.model+" is stopped")