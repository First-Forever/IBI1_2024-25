class patients:                                                 #Define the class
    def __init__(self, name, age, date, history):               #Initialize the object
        self.name = name                                        #Give value to the variables
        self.age = age
        self.date = date
        self.history = history
    
    def getinfo(self):                                          #Define the method to give values of the object
        print(f"Patient's name: {self.name}, patient's age: {self.age}, date of latest admission: {self.date}, medical history: {self.history}")

#Now we give an example to show how to use the class
patient = patients('Alex Lee', 20, '2025-04-01', 'Trouble in urine')
patient.getinfo()