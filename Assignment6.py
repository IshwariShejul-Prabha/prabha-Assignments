##SECTION 1: HYBRID INHERITANCE 

#Question 1:Create a School Management System using Person, Student, Teacher and TeachingAssistant classes. Display complete details of a Teaching Assistant.
class Person:
    def person_details(self):
        print("Name: Ishwari")
        print("Age: 21")

class Student(Person):
    def student_details(self):
        print("Course: AIML")
        print("Roll No: 101")

class Teacher(Person):
    def teacher_details(self):
        print("Subject: Python")
        print("Experience: 3 Years")

class TeachingAssistant(Student, Teacher):
    def display(self):
        self.person_details()
        self.student_details()
        self.teacher_details()
        print("Role: Teaching Assistant")

ta = TeachingAssistant()
ta.display()
print()

#Question 2:Create a Vehicle Management System using Vehicle, Car, Bike, ElectricCar and SportsElectricCar classes. 
class Vehicle:
    def show(self):
        pass
    
class Car(Vehicle):
    def show(self):
        print("Vehicle Car")
        
class Bike(Vehicle):
    def show(self):
        print("Vehicle Bike")
        
class ElectricCar(Vehicle):
    def show(self):
        print("Vehicle Electric Car")
        
class SportsElectricCar(Vehicle):
    def show(self):
        print("Vehicle Sports Electric Car")
        
v1 = Car()
v2 = Bike()
v3 = ElectricCar()
v4 = SportsElectricCar()

v1.show()
v2.show()
v3.show()
v4.show()
print()
        
#Question 3:Create an Employee System using Employee, Developer, Manager and TechLead classes.Show coding and team-management functionalities.
class Employee:
    def employee(self):
        print("Employee works in the company")

class Developer(Employee):
    def coding(self):
        print("Developer writes code")

class Manager(Employee):
    def manage_team(self):
        print("Manager manages the team")

class TechLead(Developer, Manager):
    def display(self):
        self.employee()
        self.coding()
        self.manage_team()
        print("Tech Lead handles coding and team management")

t1 = TechLead()
t1.display()
print()

#Question 4: Create a Hospital System using Person, Doctor, Nurse and HeadNurse classes.
class Person:
    def person(self):
        print("Person visits the hospital")

class Doctor(Person):
    def treat(self):
        print("Doctor treats patients")

class Nurse(Person):
    def care(self):
        print("Nurse cares for patients")

class HeadNurse(Nurse):
    def manage(self):
        print("Head Nurse manages all nurses")

h1 = HeadNurse()

h1.person()
h1.care()
h1.manage()
print()
        

#SECTION 2: HIERARCHICAL INHERITANCE 

#Question 5:Create an Animal class and derive Dog, Cat and Cow classes.Implement sound() method in each class.
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog: bhowww bhoww")
        
class Cat(Animal):
    def sound(self):
        print("Cat: Meow Meow")
        
class Cow(Animal):
    def sound(self):
        print("Cow: Mahhhhh Mahhhhh")
        
d = Dog()
c = Cat()
cw = Cow()

d.sound()
c.sound()
cw.sound()
print()

#Question 6:Create a BankAccount class and derive SavingsAccount, CurrentAccount and FixedDepositAccount classes. 
class BankAccount:
    def balance(self):
        pass

class SavingAccount(BankAccount):
    def balance(self):
        print("Saving Account Balance")
        
class CurrentAccount(BankAccount):
    def balance(self):
        print("Current Account Balance")
        
class FixedDepositAccount(BankAccount):
    def balance(self):
        print("Fixed Deposite Account Balance")

s = SavingAccount()
c = CurrentAccount()
f = FixedDepositAccount()

s.balance()
c.balance()
f.balance()
print()

#Question 7:Create an Employee class and derive Developer, Tester and Designer classes.Override work() method.
class Employee:
    def work(self):
        pass
    
class Developer(Employee):
    def work(self):
        print("Developer writes code")
        
class Tester(Employee):
    def work(self):
        print("Tester tests the code")
        
class Designer(Employee):
    def work(self):
        print("Designer creates UI design")
        
d = Developer()
t = Tester()
ds = Designer()

d.work()
t.work()
ds.work()
print()

#Question 8:Create a Shape class and derive Circle, Rectangle and Square classes.Display area calculations. 
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        radius = 5
        print("Area of Circle =", 3.14 * radius * radius)

class Rectangle(Shape):
    def area(self):
        length = 10
        width = 5
        print("Area of Rectangle =", length * width)

class Square(Shape):
    def area(self):
        side = 4
        print("Area of Square =", side * side)

c = Circle()
r = Rectangle()
s = Square()

c.area()
r.area()
s.area()
print()

#SECTION 3: POLYMORPHISM :

#Question 9:Create Shape, Circle, Rectangle and Triangle classes. Override area() method and call it using a loop. 
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        radius = 5
        print("Area of Circle =", 3.14 * radius * radius)

class Rectangle(Shape):
    def area(self):
        length = 10
        width = 5
        print("Area of Rectangle =", length * width)

class Triangle(Shape):
    def area(self):
        base = 10
        height = 5
        print("Area of Triangle =", 0.5 * base * height)

shapes = [Circle(), Rectangle(), Triangle()]

for shape in shapes:
    shape.area()
print()

#Question 10:Create Payment, CreditCardPayment, UPIPayment and NetBankingPayment classes.Override pay() method. 
class Payment:
    def pay(self):
        pass

class CreditCardPayment(Payment):
    def pay(self):
        print("Payment done using Credit Card")

class UPIPayment(Payment):
    def pay(self):
        print("Payment done using UPI")

class NetBankingPayment(Payment):
    def pay(self):
        print("Payment done using Net Banking")

p1 = CreditCardPayment()
p2 = UPIPayment()
p3 = NetBankingPayment()

p1.pay()
p2.pay()
p3.pay()
print()

#Question 11:Create Notification, EmailNotification, SMSNotification and PushNotification classes.Override send() method. 
class Notification:
    def send(self):
        pass
    
class EmailNotification(Notification):
    def send(self):
        print("Send Email Notification")
        
class SMSNotification(Notification):
    def send(self):
        print("Send SMSNotification")
        
class PushNotification(Notification):
    def send(self):
        print("Send PushNotification")
        
n1 = EmailNotification()
n2 = SMSNotification()
n3 = PushNotification()

n1.send()
n2.send()
n3.send()
print()

#Question 12:Create Animal, Dog, Cat and Lion classes. Override make_sound() method. 
class Animal:
    def make_sound(self):
        pass
    
class Dog(Animal):
    def make_sound(self):
        print("Dog Barks")
        
class Cat(Animal):
    def make_sound(self):
        print("Cat Meows")
        
class Lion(Animal):
    def make_sound(self):
        print("Lion : King of animals")
        
D = Dog()
D.make_sound()

C = Cat()
C.make_sound()

L = Lion()
L.make_sound()
print()

#Question 13:Create Employee, Developer, Tester and Manager classes. Override role() method. 
class Employee:
    def role(self):
        pass
    
class Developer(Employee):
    def role(self):
        print("Developer writes code")
        
class Tester(Employee):
    def role(self):
        print("Tester tests the code")
        
class Manager(Employee):
    def role(self):
        print("Manager manage the team")
        
dev = Developer()
dev.role()

tes = Tester()
tes.role()

man = Manager()
man.role()
print()

#Question 14:Create Vehicle, Car, Bike and Bus classes. Override start() method. 
class Vehicle:
    def start(self):
        pass
    
class Car(Vehicle):
    def start(self):
        print("Car is starting")
        
class Bike(Vehicle):
    def start(self):
        print("Bike is starting")
        
class Bus(Vehicle):
    def start(self):
        print("Bus is starting")
        
c = Car()
b = Bike()
bs = Bus()

c.start()
b.start()
bs.start()
print()


# SECTION 4: POLYMORPHISM + INHERITANCE :

#Question 15:Create Device, Camera, Phone and SmartPhone classes. Demonstrate runtime polymorphism.
class Device:
    def use(self):
        pass

class Camera(Device):
    def use(self):
        print("Taking photos with Camera")

class Phone(Device):
    def use(self):
        print("Making calls with Phone")

class SmartPhone(Device):
    def use(self):
        print("Using SmartPhone for calls, photos and apps")

devices = [Camera(), Phone(), SmartPhone()]

for device in devices:
    device.use()

print()