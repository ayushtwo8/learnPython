# class is like a blueprint for creating objects.

#creating a class
class Person:
    def __init__(self,name,age): #__init__ function is always initialized when a class is created. 
        self.name = name 
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age}"

# creating object
p1 = Person("John",25)

#printing name and age
print(p1.name)
print(p1.age)

#printing name and age after using __str__
print(p1)


# Example with method..

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}")    

p1 = Person("John",25)
p1.greet()        

del p1.age # age property of p1 object deleted


# Inheritance property

class Person1:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printName(self):
        print(self.fname, self.lname)    

x = Person1("John", "Doe")
x.printName()        

class Student(Person1):
    pass # use pass if you do not want to add content

y = Student("Ram","Mohan")
y.printName()

# when you add the __init__() function, the child class will no longer 
# inherit the parent's __init__() function.

# you can also use super keyword


# Polymorphism property

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model 

    def move(self):
        print("Sail!")

class Plane:       
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model     

    def move(self):
        print("Fly!")


car1 = Car("Ford", "Mustang")                                 
boat1 = Boat("Ibiza", "Touring 20")                                 
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    x.move()