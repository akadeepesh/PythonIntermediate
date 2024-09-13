class Person:

    numberOfPeople = 0 # Class variable

    def __init__(self, name, age, height): # Constructor
        self.name = name
        self.age = age
        self.height = height
        Person.numberOfPeople += 1

    def __del__(self): # Destructor
        Person.numberOfPeople -= 1
        print("Object is deleted")

    def __str__(self): # This method will be called when we print the object
        return f"Name: {self.name}, Age: {self.age}, Height: {self.height}"

person1 = Person("Deepesh", 21, 6.3)

print(person1.name)

person1.name = "Deepesh Kumar" # Modifying the object

print(person1.name) # This will print Deepesh Kumar

print(person1) # This will call __str__ method

person2 = Person("Deepesh", 21, 6.3)

print(Person.numberOfPeople) # This will print 2