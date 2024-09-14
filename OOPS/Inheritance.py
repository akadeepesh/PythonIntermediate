class Person:

    def __init__(self, name, age, height): # Constructor
        self.name = name
        self.age = age
        self.height = height

    def __str__(self): # This method will be called when we print the object
        return f"Name: {self.name}, Age: {self.age}, Height: {self.height}"

    def getOlder(self, years):
        self.age += years

class Worker(Person):

    def __init__(self, name, age, height, salary):
        super().__init__(name, age, height)
        self.salary = salary

    def __str__(self):
        return super().__str__() + f", Salary: {self.salary}"
    
    def calc_yearly_salary(self):
        return self.salary * 12

Worker1 = Worker("Deepesh", 21, 6.3, 30000)
print(Worker1) # Name: Deepesh, Age: 21, Height: 6.3, Salary: 30000
print(Worker1.calc_yearly_salary()) # 360000
