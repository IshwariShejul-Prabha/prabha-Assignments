##Topics: Abstract Class, Abstract Method, Polymorphism 

##Question 1: Abstract Class & Abstract Method:
# Create an abstract class Vehicle. 
# Requirements: 
# ● Create an abstract method start(). 
# ● Create a child class Car. 
# ● Implement the start() method in Car. 
# ● Create an object of Car and call start(). 

# from abc import ABC, abstractmethod
# #Abstract Class
# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass
    
# class Car(Vehicle):
#     def start(self):
#         print("Car is starting...")
        
# obj = Car()
# obj.start()

# Question 2: Abstract Class with Multiple Child Classes: 
# Create an abstract class Animal. 
# Requirements: 
# ● Create an abstract method sound(). 
# ● Create two child classes: 
# ○ Dog 
# ○ Cat 
# ● Implement the sound() method in both classes. 
# ● Create objects and call sound().

# from abc import ABC,abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
    
# class Dog(Animal):
#     def sound(self):
#         print("Dog Barks")
        
# class Cat(Animal):
#     def sound(self):
#         print("Cat Meows")
        
# D = Dog()
# C = Cat()
# D.sound()
# C.sound()

#Question 3: Polymorphism Using Method Overriding :
# Create a class Shape. 
# Requirements: 
# ● Create a method draw(). 
# ● Create child classes: 
# ○ Circle 
# ○ Rectangle 
# ● Override the draw() method in both child classes. 
# ● Call the draw() method using objects. 

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

#Question 4: Polymorphism with Loop :
# Create a class Bird. 
# Requirements: 
# ● Create a method fly(). 
# ● Create child classes: 
# ○ Sparrow 
# ○ Eagle 
# ● Override the fly() method. 
# ● Store objects in a list and call fly() using a loop.

# class Bird:
#     def fly(self):
#         pass
    
# class Sparrow(Bird):
#     def fly(self):
#         print("Sparrow flies low")
        
# class Eagle(Bird):
#     def fly(self):
#         print("Eagle flies high")
        
# Birds = [Sparrow(), Eagle()]

# for Bird in Birds:
#     Bird.fly()
    
# Question 5: Abstract Class + Polymorphism :
# Create an abstract class Employee. 
# Requirements: 
# ● Create an abstract method work(). 
# ● Create two child classes: 
# ○ Developer 
# ○ Designer 
# ● Implement the work() method in both classes. 
# ● Store objects in a list and call work() using a loop.

# from abc import ABC, abstractmethod
# class Employee(ABC):
#     def work(self):
#         pass
    
# class Developer(Employee):
#     def work(self):
#         print("Developer writes code")
        
# class Designer(Employee):
#     def work(self):
#         print("Designer creates Ui design")
        
# dev = Developer()
# des = Designer()

# Employees = [Developer(), Designer()]

# for Employee in Employees:
#     Employee.work()