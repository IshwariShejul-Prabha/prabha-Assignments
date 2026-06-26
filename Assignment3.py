# #Challenge 1: Student Management System
# # Create a Student class.
# # Requirements:
# # - Create instance variables: name, age, course.
# # - Create a class variable school_name = "ABC College".
# # - Create an instance method display_student() to display student details.
# # - Create a class method change_school_name() to change the school name.
# # - Create 2 student objects and demonstrate the class method

# class Student:
#     # Class variable
#     school_name = "ABC College"
    
#     def __init__(self, name, age, course):
#         # Instance variable
#         self.name = name
#         self.age = age
#         self.course = course
        
#     # Class method
#     @classmethod
#     def change_school_name(cls,new_school_name):
#         cls.school_name = new_school_name
        
    
#     # Constructor
#     def display_student(self):
#         # Instance Method
#         print("Name:",self.name)
#         print("Age:",self.age)
#         print("Course:",self.course)
#         print("School name:", Student.school_name)
            
# s1 = Student("Ishwari",19,"AIML")
# s1.display_student()
# print()

# s2 = Student("Rushii",21,"Java")
# s2.display_student()
# print()
    
# Student.change_school_name("IMS College")
# s2.display_student()

# Challenge 2: Employee Counter
# Create an Employee class.
# Requirements:
# - Create instance variables: emp_id, emp_name, salary.
# - Create a class variable employee_count to count total employees.
# - Increment the count whenever a new employee object is created.
# - Create an instance method display_employee().
# - Create a class method show_total_employees() to display the total employee count.

# class Employee:
#     #Class variable
#     employee_count = 0
    
#     def __init__(self,emp_id,emp_name,salary):
#         self.emp_id = emp_id
#         self.emp_name = emp_name
#         self.salary = salary
        
#     # Increment employee count
#         Employee.employee_count += 1
        
#     def display_employee(self):
#         #Instance Method
#         print("Emp id:",self.emp_id)
#         print("Emp name:",self.emp_name)
#         print("Emp Salary:",self.salary)
        
#     @classmethod
#     def show_total_employees(cls):
#         print("Total Employees:", cls.employee_count)
        
# #Creating objects        
# e1 = Employee(101,"Ishwari",25000)
# e1.display_employee()
# print()

# e2 = Employee(102,"Atharv",40000)
# e1.display_employee()
# print()

# e3 = Employee(103,"Rushikesh",45000)
# e3.display_employee()
# print()

# Employee.show_total_employees()

# Challenge 3: Bank Account System
# Create a BankAccount class.
# Requirements:
# - Create instance variables: account_number, holder_name, balance.
# - Create a class variable bank_name = "State Bank of India".
# - Create instance methods deposit(amount), withdraw(amount), check_balance().
# - Create a class method change_bank_name() to update the bank name.
# - Create multiple account objects and test all methods.

# class BankAccount:
#     #Class variable
#     bank_name = "State Bank of India"
    
#     def __init__(self,account_number,holder_name,balance):
#         self.account_number = account_number
#         self.holder_name = holder_name
#         self.balance = balance
        
#     # Instance Method for Deposit
#     def deposit(self, amount):
#         self.balance += amount
#         print(self.holder_name,"Deposited:", amount)

#     # Instance Method for Withdraw
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(self.holder_name,"Withdrawn:", amount)
#         else:
#             print("Insufficient Balance")

#     # Instance Method for Checking Balance
#     def check_balance(self):
#         print(self.holder_name,"Current Balance:", self.balance)
        
#     #Class Method
#     @classmethod
#     def change_bank_name(cls,new_bank_name):
#         cls.bank_name = new_bank_name
        
# acc1 = BankAccount(101,"Ishwari",25000)
# acc2 = BankAccount(102,"Atharv",5000)
# acc3 = BankAccount(106,"Rushikesh",10000)
# acc4 = BankAccount(104,"Dipak",20000)
# acc5 = BankAccount(115,"Jyoti",4000)
    
# acc1.deposit(2000)
# acc4.deposit(1000)
    
# acc2.withdraw(3000)
    
# acc1.check_balance()
    
# BankAccount.change_bank_name("SBI Bank")
# print("New Bank Name:", BankAccount.bank_name)

#Challenge 4: Mobile Store Inventory
# Create a Mobile class.
# Requirements:
# - Create instance variables: brand, model, price.
# - Create a class variable discount_percentage = 10.
# - Create an instance method display_mobile().
# - Create an instance method calculate_discount_price().
# - Create a class method change_discount(new_discount) to update the discount percentage for all mobiles
# class Mobile:
#     #Class variable
#     discount_percentage = 10
    
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price

#     # Instance method
#     def display_mobile(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)
#         print("Price:", self.price)
#         print("Discount:", Mobile.discount_percentage,"%")

#     # Instance method
#     def calculate_discount_price(self):
#         discount_amount = (self.price * Mobile.discount_percentage) / 100
#         final_price = self.price - discount_amount
#         return final_price

#     # Class method
#     @classmethod
#     def change_discount(cls, new_discount):
#         cls.discount = new_discount

# # Create objects
# m1 = Mobile("Samsung", "Galaxy S24", 80000)
# m2 = Mobile("Apple", "iPhone 16", 100000)

# m1.display_mobile()
# print("Discount Price:", m1.calculate_discount_price())
# print()

# m2.display_mobile()
# print("Discount Price:", m2.calculate_discount_price())
# print()

# # Change discount for all mobiles
# Mobile.change_discount(20)

#Challenge 5: Library Book Management
#Create a Book class.
# Requirements:
# - Create instance variables: book_id, title, author.
# - Create a class variable library_name = "City Library".
# - Create an instance method display_book_info().
# - Create a class method change_library_name() to change the library name.
# - Create at least 3 book objects and display their information before and after changing the library name.
# class Book:
#     #Class variable
#     library_name = "City Library"
    
#     def __init__(self,book_id,title,author):
#         self.book_id = book_id
#         self.title = title
#         self.author = author
        
#     def display_book_info(self):
#         print("Library Name:",Book.library_name)
#         print("Book ID:",self.book_id)
#         print("Title:",self.title)
#         print("Author:",self.author)
        
#     @classmethod
#     def change_library_name(cls,new_library_name):
#         cls.library_name = new_library_name
        
# # Create 3 book objects
# b1 = Book(101, "Think and Grow Rich", "Napoleon Hill")
# b2 = Book(102, "The Alchemist", "Paulo Coelho")
# b3 = Book(103, "Pride and Prejudice", "Jane Austen")

# print("Before changing library name")
# b1.display_book_info()
# print()
# b2.display_book_info()
# print()
# b3.display_book_info()

# # Change library name
# Book.change_library_name("Poor Library")

# print("\nAfter changing library name")
# b1.display_book_info()
# print()
# b2.display_book_info()
# print()
# b3.display_book_info()



