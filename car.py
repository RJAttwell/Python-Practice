class Car:
    
    def __init__(self, make, model, year, colour):     #Can pass in some arguments and assign them to each object attribute
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour
    

    def drive(self):                #self refers to object using this method (e.g: car)
        print ("This "+self.model+ " is driving")

    def stop(self):
        print("This "+self.model+ " has stopped")



