# # SECTION--1: MODULES

# Challenge 1: Create a module named calculator.py containing functions add(), subtract(), multiply(), divide(). 
# Import the module in another file and perform all operations.


# Challenge 2: Create a module named employee.py. Store employee name and salary. Create a function to display employee details. 
# Import and use the function in another file.


# Challenge 3: Import the math module and write a program to find square root of 144, value of pi, and factorial of 6.


# Challenge 4: Import the random module and generate a random number between 1 and 100 and a random choice from ['Python', 'Java', 'React', 'Django'].


# Challenge 5: Create a custom module area.py with functions area_circle() and area_rectangle(). Import the module and calculate areas.

# # SECTION--2: CLASSES & OBJECTS

# #Challenge 6: Create a class Student with attributes name and age. Create an object and display the values.
# class Student:
#     pass

# # Create object
# s1 = Student()

# # Assign values
# s1.name = "Ishwari"
# s1.age = 19

# # Display values
# print("Name:", s1.name)
# print("Age:", s1.age)
    
# # Challenge 7: Create a class Car with attributes brand and model. Create two objects and display details.
# class Car:
#     pass

# #Create objects
# c1 = Car()

# #Assign values
# c1.brand = "Toyota"
# c1.model = "Fortuner"

# c2 = Car()
# c2.brand = "Mahindra"
# c2.model = "Scorpio N"

# #Display value
# print("Brand:",c1.brand)
# print("Model:",c1.model)
# print()

# print("Brand:",c2.brand)
# print("Model:",c2.model)

# Challenge 8: Create a class Book with attributes title, author, and price. Create three objects and display details.
# class Book:
#     pass

# b1 = Book()
# b1.title = "The Alchemist"
# b1.author = "Paulo Coelho"
# b1.price = 350

# b2 = Book()
# b2.title = "Think and Grow Rich"
# b2.author = "Napoleon Hill"
# b2.price = 400

# b3 = Book()
# b3.title = "Pride and Prejudice"
# b3.author = "Jane Austen"
# b3.price = 300

# Books = [b1, b2, b3]

# for Book in Books:
#     print("Title:",Book.title)
#     print("Author:",Book.author)
#     print("Price:",Book.price)
#     print()

# # Challenge 9: Create a class Laptop with attributes brand, RAM, and price. Create two objects and print information.
# class Laptop:
#     pass

# l1 = Laptop()
# l1.brand = "Lenovo LOQ"
# l1.ram = "16 GB"
# l1.price = 75000

# l2 = Laptop()
# l2.brand = "HP Victus"
# l2.ram = "16GB"
# l2.price = 70000

# print("Brand:",l1.brand)
# print("RAM:",l1.ram)
# print("Price:",l1.price)
# print()

# print("Brand:",l2.brand)
# print("RAM:",l2.ram)
# print("Price:",l2.price)

# # Challenge 10: Create a class Mobile with attributes company, model, and storage. Create multiple objects and display details
# class Mobile:
#     pass

# m1 = Mobile()
# m1.company = "Apple"
# m1.model = "iphone 17"
# m1.storage = "128 GB"

# m2 = Mobile()
# m2.company = "Samsung"
# m2.model = "Galaxy S24"
# m2.storage = "256 GB"

# m3 = Mobile()
# m3.company = "Vivo"
# m3.model = "V50"
# m3.storage = "256 GB"

# Mobiles = [m1,m2,m3]

# for Mobile in Mobiles:
#     print("Company:",Mobile.company)
#     print("Model:",Mobile.model)
#     print("Storage:",Mobile.storage)
#     print()

# # SECTION--3: CONSTRUCTOR (__init__)

# Challenge 11: Create a class Employee. Use constructor to initialize emp_id, emp_name, and salary. Display employee information.
# class Employee:
#     #Constructor
#     def __init__(self,emp_id,emp_name,salary):
#         #Instance variable
#         self.emp_id = emp_id
#         self.emp_name = emp_name
#         self.salary = salary
        
#     def display_details(self):
#         print("Emp ID:",self.emp_id)
#         print("Emp Name:",self.emp_name)
#         print("Salary:",self.salary)
        
# e1 = Employee(101,"Ishwari",25000)
# e1.display_details()
# print()

# e2 = Employee(102,"Rushikesh",30000)
# e2.display_details()
# print()

# Challenge 12: Create a class BankAccount. Initialize account_number, holder_name, and balance.Create two accounts and display details.
# class BankAccount:
#     #Constructor
#     def __init__(self,account_number,holder_name,balance):
#         self.account_number = account_number
#         self.holder_name = holder_name
#         self.balance = balance
        
#     def display_details(self):
#         print("Account number:",self.account_number)
#         print("Holder name:",self.holder_name)
#         print("Balance:",self.balance)
        
# #Create 2 accounts 
# acc1 = BankAccount(100,"Ishwari",2000)
# acc1.display_details()
# print()

# acc2 = BankAccount(110,"Atharv",25000)
# acc2.display_details()
# print()

# #Challenge 13: Create a class Movie. Initialize movie_name, hero, and rating. Display movie details.
# class Movie:
#     #Constructor
#     def __init__(self,movie_name,hero,rating):
#         self.movie_name = movie_name
#         self.hero = hero
#         self.rating = rating
        
#     def display_details(self):
#         print("Movie name:",self.movie_name)
#         print("Hero:",self.hero)
#         print("Rating:",self.rating)
        
# m1 = Movie("Cocktail 2","Ritik roshan",1.0)
# m1.display_details()

# #Challenge 14: Create a class Product. Initialize product_id, product_name, and price. Create multiple products and print details.
# class Product:
    
#     def __init__(self,product_id,product_name,price):
#         self.product_id = product_id
#         self.product_name = product_name
#         self.price = price
        
#     def display_details(self):
#         print("Product ID:",self.product_id)
#         print("Product name:",self.product_name)
#         print("Price:",self.price)
        
# p1 = Product(101,"Smart Watch",2999)
# p1.display_details()
# print()

# p2 = Product(102,"USB Keyboard",1299)
# p2.display_details()
# print()

# p3 = Product(103,"Laptop Stand",899)
# p3.display_details()
# print()

# p4 = Product(104,"Bluetooth Headphones",1999)
# p4.display_details()
# print()

# #Challenge 15: Create a class College. Initialize college_name, city, and students_count. Display details using objects
# class College:
    
#     def __init__(self,college_name,city,students_count):
#         self.college_name = college_name
#         self.city = city
#         self.students_count = students_count
        
#     def display_details(self):
#         print("College Name:",self.college_name)
#         print("City:",self.city)
#         print("Students Count:",self.students_count)
        
# c1 = College("Zeal Polytechnic","Pune",12000)
# c1.display_details()
# print()

# c2 = College("Wadiya College","Pune",8000)
# c2.display_details()
# print()

# c3 = College("VJTI","Mumbai",3500)
# c3.display_details()
# print()

##SECTION--4: SELF KEYWORD

# #Challenge 16: Create a class Person. Use self to store name and age. Display values using a method.
# class Person:
    
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age 
        
#     def display(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
        
# p1 = Person("Ishwari",19)
# p1.display()
# print()

# p2 = Person("Atharv",20)
# p2.display()
# print()

# #Challenge 17: Create a class Animal. Store animal_name and color. Print values using self
# class Animal:
    
#     def __init__(self,animal_name,color):
#         self.animal_name = animal_name
#         self.color = color
        
#     def display(self):
#         print("Animal Name:",self.animal_name)
#         print("Animal Color:",self.color)
        
# a1 = Animal("Tiger","Orange")
# a1.display()
# print()

# a2 = Animal("Parrot","Green")
# a2.display()
# print()

# #Challenge 18: Create a class Vehicle. Store company and model. Display details using a method and self.
# class Vehicle:
    
#     def __init__(self,company,model):
#         self.company = company
#         self.model = model
        
#     def display(self):
#         print("Company:",self.company)
#         print("Model:",self.model)
        
# v1 = Vehicle("Hyundai","Creta")
# v1.display()
# print()

# #Challenge 19: Create a class Teacher. Store teacher_name and subject. Display teacher information using self.
# class Teacher:
    
#     def __init__(self,teacher_name,subject):
#         self.teacher_name = teacher_name
#         self.subject = subject
        
#     def display(self):
#         print("Teacher Name:",self.teacher_name)
#         print("Subject:",self.subject)
        
# t1 = Teacher("Ashok Kale","Marathi")
# t1.display()
# print()

# t2 = Teacher("Sushmita","English")
# t2.display()
# print()

# #Challenge 20: Create a class Player. Store player_name and team. Print details using self.
# class Player:
    
#     def __init__(self,player_name,team):
#         self.player_name = player_name
#         self.team = team
    
#     def display(self):
#         print("Player Name:",self.player_name)
#         print("Team:",self.team)
        
# p1 = Player("Virat Kholi","Mumbai Indian")
# p1.display()
# print()

# p2 = Player("Rohit Shrama","CSK")
# p2.display()
# print()

##SECTION--5: INSTANCE ATTRIBUTES

# #Challenge 21: Create a class Student with instance attributes name, roll_no, and marks. Create three students and display details.
# class Student:
    
#     def __init__(self,name,roll_no,marks):
#         self.name = name
#         self.roll_no = roll_no
#         self.marks = marks
        
#     def display(self):
#         print("Name:",self.name)
#         print("Roll No:",self.roll_no)
#         print("Marks:",self.marks)
        
# s1 = Student("Ishwari",19,84.42)
# s1.display()
# print()

# s2 = Student("Atharv",26,72.89)
# s2.display()
# print()

# #Challenge 22: Create a class Employee with instance attributes emp_id, emp_name, and department. Display all employee details.
# class Employee:
    
#     def __init__(self,emp_id,emp_name,department):
#         self.emp_id = emp_id
#         self.emp_name = emp_name
#         self.department = department
        
#     def display(self):
#         print("Emp ID:",self.emp_id)
#         print("Emp Name:",self.emp_name)
#         print("Department:",self.department)
        
# e1 = Employee(100,"Ishwari","AIML")
# e1.display()
# print()

# e2 = Employee(101,"Atharv","Autorobotics")
# e2.display()
# print()

# e3 = Employee(102,"Rushikesh","Civil")
# e3.display()
# print()

# #Challenge 23: Create a class Hospital with instance attributes doctor_name and specialization.Create multiple objects and display details.
# class Hospital:
    
#     def __init__(self,doctor_name,specialization):
#         self.doctor_name = doctor_name
#         self.specialization = specialization
        
#     def display(self):
#         print("Doctor Name:",self.doctor_name)
#         print("Specialization:",self.specialization)
        
# h1 = Hospital("Dr.Dipak Patil","Kidney Specialization")
# h1.display()
# print()

# h2 = Hospital("Dr.Ashok Kale","Surgery Specialization")
# h2.display()
# print()

# h3 = Hospital("Dr.Nikita Sign","Teeth Specialization")
# h3.display()
# print()

# #Challenge 24: Create a class Course with instance attributes course_name, duration, and fees.Display course details.
# class Course:
    
#     def __init__(self,course_name,duration,fees):
#         self.course_name = course_name
#         self.duration = duration
#         self.fees = fees
        
#     def display(self):
#         print("Course Name:",self.course_name)
#         print("Duration:",self.duration)
#         print("Fees:",self.fees)
        
# c1 = Course("Jave","1 Month",5000)
# c1.display()
# print()

# c2 =Course("Python Full Stack","2 Month",10000)
# c2.display()
# print()

# c3 = Course("C++","1.5 Month",3000)
# c3.display()
# print()
        
# #Challenge 25: Create a class CricketPlayer with instance attributes player_name, runs, and matches. Display player details.
# class CricketPlayer:
    
#     def __init__(self,player_name,runs,matches):
#         self.player_name = player_name
#         self.runs = runs
#         self.matches = matches
        
#     def display(self):
#         print("Player Name:",self.player_name)
#         print("Runs:",self.runs)
#         print("Matches:",self.matches)
        
# Player1 = CricketPlayer("Virat Kholi",200,5)
# Player1.display()
# print()

##SECTION--6: INSTANCE METHODS

# #Challenge 26: Create a class Rectangle with an instance method calculate_area(). Take length and width from constructor.
# class Rectangle:
    
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
        
#     #Instance method    
#     def calculate_area(self):
#         area = self.length * self.width
#         print("Area of Rectangle:", area)

# r1 = Rectangle(10, 5)
# r1.calculate_area()

# #Challenge 27: Create a class Circle with an instance method calculate_area(). Take radius from constructor.
# class Circle:
    
#     def __init__(self,radius):
#         self.radius = radius
        
#     def calculate_area(self):
#         radius = 3.14*self.radius*self.radius
#         print("Radius of Circle:",radius)
        
# c1 = Circle(7)
# c1.calculate_area()

# #Challenge 29: Create a class Student with an instance method calculate_percentage(). Calculate percentage from marks.
# class Student:
    
#     def __init__(self,marks):
#         self.marks = marks
        
#     def calculate_percentage(self):
#         percentage = (self.marks / 500) * 100
#         print("Percentage:", percentage, "%")


# s1 = Student(425)
# s1.calculate_percentage()

# #Challenge 30: Create a class BankAccount with methods deposit() and withdraw(). Update account balance.
# class BankAccount:
    
#     #Instance Attribute(Variable)
#     def __init__(self,balance):
#         self.balance = balance
    
#     #Instance Method
#     def deposit(self, amount):
#         self.balance = self.balance + amount
#         print("Balance after deposit:", self.balance)
        
#     #Instance Method
#     def withdraw(self, amount):
#         self.balance = self.balance - amount
#         print("Balance after withdrawal:", self.balance)

# #Objects
# acc1 = BankAccount(10000)

# acc1.deposit(5000)
# acc1.withdraw(2000)