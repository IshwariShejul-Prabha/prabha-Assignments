##Question 1: Abstract Class & Abstract Method
#Create an abstract class Vehicle.
# • Create an abstract method start().
# • Create a child class Car.
# • Implement the start() method in Car.
# • Create an object of Car and call start()

#from abc import ABC, abstractmethod 
# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass
    
# class Car(Vehicle):
#     def start(self):
#         print("Car is starting...")
        
# obj = Car()
# obj.start()    

#Question 2: Abstract Class with Multiple Child Classes
# Create an abstract class Animal.
# • Create an abstract method sound().
# • Create two child classes: Dog and Cat.
# • Implement the sound() method in both classes.
# • Create objects and call sound()

#from abc import ABC, abstractmethod 
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
    
# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")
        
# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")
        
# D = Dog()
# C = Cat()
# D.sound()
# C.sound()
        
#Question 3: Polymorphism Using Method Overriding
#Create a class Shape.
# • Create a method draw().
# • Create child classes: Circle and Rectangle.
# • Override the draw() method in both child classes.
# • Call the draw() method using objects.
# class Shape:
#     def draw(self):
#         pass
        
# class Circle(Shape):
#     def draw(self):
#         print("Drawing Circle")

# class Rectangle(Shape):
#     def draw(self):
#         print("Drawing Rectangle")
        
# C = Circle()
# R = Rectangle()

# C.draw()
# R.draw()

#Question 4: Polymorphism with Loop
# Create a class Bird.
# • Create a method fly().
# • Create child classes: Sparrow and Eagle.
# • Override the fly() method.
# • Store objects in a list and call fly() using a loop

##Parent class
# class Bird:
#     def fly(self):
#         pass
    
# #Child Class    
# class Sparrow:
#     def fly(self):
#         print("Sparrow flies low")

# #Child Class        
# class Eagle:
#     def fly(self):
#         print("Eagle flies high")
    
# #Create objects        
# S = Sparrow()
# E = Eagle()

# #Store objects in a list
# Birds = [Sparrow(), Eagle()]

# #call fly() using a loop
# for Bird in Birds:
#     Bird.fly()
    
# Question 5: Abstract Class + Polymorphism
# Create an abstract class Employee.
# • Create an abstract method work().
# • Create two child classes: Developer and Designer.
# • Implement the work() method in both classes.
# • Store objects in a list and call work() using a loop.

# from abc import ABC, abstractmethod
# #Abstract Class
# class Employee:
#     @abstractmethod
#     def work(self):
#         pass
    
# #Child Classes
# class Developer:
#     def work(self):
#         print("Developer writes code")
        
# class Designer:
#     def work(self):
#         print("Designer creates UI design")
        
# #Create objects
# dev = Developer()
# des = Designer()
        
# #Store objects in a list
# Employees = [Developer(), Designer()]

# #Call work() using loop
# for Employee in Employees:
#     Employee.work()
