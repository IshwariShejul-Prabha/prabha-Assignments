# # SECTION--1: print(), input(), Variables & Naming Rules 

##Q1.Write a program to display your name, college name, and favorite programming language using print().
# Name = "Ishwari"
# College_name = "Zeal Polytechnic"
# Favorite_programming_language = "Python"
# print("Name:",Name)
# print("College_name:",College_name)
# print("Favorite_programming_language:",Favorite_programming_language)

## Q2.Take user input for name and age, then display:"Hello Sham, you are 22 years old."
# Name = str(input("Enter your name:"))
# Age = int(input("Enter your age:"))
# print(Name,Age)

## Q3.Create variables for: ● Student name ● Roll number ● Percentage ● Passed status. Print all values in a formatted way. 
# Student_name = "Ishwari"
# Roll_number = 54
# Percentage = 94.04
# Passed_status = True
# print("Student Details:")
# print("___________________________________________")
# print("Student name:",Student_name)
# print("Roll number:",Roll_number)
# print("Percentage:",Percentage)
# print("Passed status:",Passed_status)

## Q4.identify which of the following variable names are invalid and rewrite them correctly: ●1name ●student-name ●class ●total marks ●user_name
# print("Invalid variables: 1name, total name, student-name, class")
# print("Corect variables: name1, total_name, student_name, Class, user_name ")
# name1 = "Ishwari"
# student_name = "Ishwari"
# class_name = "AIML"
# total_marks = 450
# user_name = "ishwari123"
# print(name1)
# print(student_name)
# print(class_name)
# print(total_marks)
# print(user_name)


## SECTION--2: Data Types & Type Conversion 

#Q5. Create variables of type: ● int ● float ● str ● bool Print each variable with its data type using type(). 
# Integer = 19
# Float = 26.1
# String = "Ishwari"
# Boolean = True
# print(type(Integer))
# print(type(Float))
# print(type(String))
# print(type(Boolean))

#Q6. Take two numbers as input from the user and display their sum. 
# a = int(input("Enter first number:"))
# b = int(input("Enter second number:"))
# print("Sum =",a + b)

#Q7. Take a decimal number as input and convert it into: ● integer ● string Display all converted values.
# a = float(input("Enter decimal number:"))
# Integer = int(a)
# String = str(a)
# # Display converted values
# print("Original Decimal Value:",a)
# print("Integer Value:", Integer)
# print("String Value:", String)

#Q8. Take user input for age and check whether the input type is string or integer. 
# Age = input("Enter a age:")
# print(type(Age))


##SECTION--3: Operators 

#Q9. Write a program to perform: ●Addition ●Subtraction ●Multiplication ●Division ●Modulus on two user-input numbers. 
# a = int(input("Enter first number:"))
# b = int(input("Enter second number:"))
# print("Arithmetic Operator:")
#print("__________________________________________")
# print("Addition:", a + b)
# print("Subtraction:", a - b)
# print("Multiplication:", a * b)
# print("Division:", a / b)
# print("Modulus:", a % b)

#Q10.Take two numbers and display: ● Greater than ● Less than ● Equal to ● Not equal to comparison results.
# a = 10
# b = 20
# print("Comparison/Relational Operator:")
# print("________________________________________________________")
# print("a =",a)
# print("b =",b)
# print("Greater than:", a > b)
# print("Less than:", a < b)
# print("Equal to:", a == b)
# print("Not equal to:", a != b)

#Q11.Create a login system using logical operators: ● Username must be "admin" ● Password must be "1234".Display login success or failure.
# Username = input("Username : ")
# Password = input("Password : ")
# if Password == "1234" and Username == "admin":
#     print("Login successful")
# else:
#     print("Incorrect password or username")
    
#Q12.Write a program to check whether a number is: ● Positive ● Negative ● Zero    
# num = float(input("Enter the number:"))
# if num >= 0:
#     if num == 0:
#         print("Given number is zero")
#     else:
#         print("Given number is positive")
# else:
#         print("Given number is negative")


##SECTION--4: Conditional Statements (if / elif / else) 

#Q13. Take marks as input and print grade: ● A → 90 and above ● B → 75 to 89 ● C → 50 to 74 ● Fail → below 50
# Marks = float(input("Enter marks:"))
# if Marks >= 90:
#     print("Grade : A")
# elif Marks >= 75:
#     print("Grade : B")
# elif Marks >= 50:
#     print("Grade : C")
# else:
#     print("Fail")

#Q14.Write a program to check whether a number is even or odd. 
# Num = int(input("Enter Number:"))
# if Num%2==0:
#     print("Given number is EVEN")
# else:
#     print("Given number is ODD ")

#Q15.Take age as input and determine: ● Child ● Teenager ● Adult ● Senior Citizen
# Age = int(input("Enter age:"))
# if Age < 13:
#     print("Child")
# elif Age < 20:
#     print("Teenage")
# elif Age < 60:
#     print("Adult")
# else:
#     print("Senior citizen")

#Q16.Create a simple calculator using if-elif-else. Operations: ● Addition ● Subtraction ● Multiplication ● Division
# a = int(input("Enter first number:"))
# b = int(input("Enter second number:"))
# if +:
#     print(a+b)
# elif -:
#     print(a-b)
# elif *:
#     print(a*b)
# elif /:
#     print(a/b)


##SECTION--5: Loops (for & while) -------ALL FROM CHATGPT 

#Q17. Print numbers from 1 to 20 using a for loop.
# for i in range(1,21):               #range(1, 21) → 1 पासून 20 पर्यंत संख्या देते.         
#     print(i)
    
#Q18.Print all even numbers between 1 and 50. 
# for i in range(1,51)
#     if i %2==0:                     #i % 2 == 0 असेल तर number even असतो.
#         print(i)

#Q19.Print the multiplication table of a user-input number. 
# Num = int(input("Enter Multiplication table of:"))
# for i in range(1,11):
#     print(f"{Num} * {i} = {Num*i}")

#Q20.Use a while loop to print numbers from 10 to 1. 
# count = 1
# while(count<11):
#     print(count)
#     count = count + 1
    
#Q21.Write a program to calculate the sum of numbers from 1 to 100. 
# sum = 0                           #sum = 0 → initial value
#for i in range(1, 101):            #range(1, 101) → numbers from 1 to 100
#     sum = sum + i                 #sum = sum + i → adds each number to the total

# print("Sum =", sum)               #Finally prints the total sum

#Q22.Take a number from the user and count how many digits it contains. 
# num = int(input("Enter a number: "))
# count = 0                                         #Number 0 होईपर्यंत loop चालतो.

# while num > 0:
#     count += 1                                    #प्रत्येक वेळी count 1 ने वाढवतो.
#     num = num // 10                               #num // 10 केल्यावर शेवटचा digit काढला जातो.

# print("Number of digits =", count)

# #Same program as above in short
# num = input("Enter a number: ")
# print("Number of digits =", len(num))


##SECTION--6: break & continue 

#Q23. Print numbers from 1 to 20, but stop the loop when the number becomes 15.
# for i in range(1,21):
#     if i == 16:
#         break
#     print(i)

#Q24.Print numbers from 1 to 20, skipping all multiples of 3. 
# for i in range(1, 21):
#     if i % 3 == 0:               #i % 3 == 0 → number is a multiple of 3.
#         continue                 #continue → skips that iteration and moves to the next number.
#     print(i)
    
# #Q25.Create a password checking system that keeps asking until the correct password is entered. 
# password = "python123"
# while True:                                             #while True मुळे loop सतत चालू राहतो.
#     user_password = input("Enter password: ")

#     if user_password == password:
#         print("Access Granted!")
#         break                                          #Password बरोबर आला की break loop थांबवतो.
#     else:
#         print("Wrong Password. Try Again.")


# #SECTION--7: Nested Loops 

##Q26. Print the following pattern: 
## * 
## ** 
## *** 
## **** 
##z *****
# for i in range(0,5):
#     for j in range(i+1):
#         print("*",end = " ")
#     print()                              #print() मुळे पुढच्या line वर जातो.
    
##Q27.Print a multiplication table from 1 to 5 using nested loops.
# for i in range(1, 6):
#     print("Table of", i)       #Outer loop (i) → Tables from 1 to 5.

#     for j in range(1, 11):     #Inner loop (j) → Multiplication from 1 to 10 for each table.
#         print(i, "x", j, "=", i * j)
#     print()
    
## Q28.Create a number square pattern: 
## 1111 
## 2222 
## 3333 
## 4444 
# for i in range(1,5):         #Outer loop (i) → 1 ते 4 पर्यंत rows तयार करतो.
#     for i in range(1,5):     #Inner loop (j) → प्रत्येक row मध्ये तोच number 4 वेळा print करतो.
#         print(i, end="")     #end="" मुळे numbers एकाच line मध्ये print होतात.
#     print()                  #print() मुळे पुढच्या line वर जातो.


##SECTION--8: Lists 

##Q29.Create a list of 5 student names and print: ● First student ● Last student ● Total number of students.
# list = ["Ishwari","Rushikesh","Atharv","Jyoti","Dipak"]
# print(list)
# print(list[0])
# print(list[4])
# print(len(list))

##Q30.Take 5 numbers from the user and store them in a list. 
# numbers = list(map(int, input("Enter 5 numbers: ").split()))
# print(numbers)

# #above program using for loop
# numbers = []                                               #numbers = [] → Empty list create केली.

# for i in range(5):
#     num = int(input("Enter a number: "))
#     numbers.append(num)                                    #append() → प्रत्येक input list मध्ये add करतो.

# print("List =", numbers)

##Q31.Perform the following operations on a list: ● append() ● remove() ● pop() ● sort() 
# number = [10,20,30,40,50]

# number.append(100)
# print(number)

# number.remove(20)
# print(number)

# number.pop()
# print(number)

# number.sort()           #List ascending order मध्ये arrange करतो.
# print(number)

##Q32.Print all elements of a list using a loop.
# numbers = [10, 20, 30, 40, 50]

# for i in numbers:
#     print(i)

##Q33.Find: ● Maximum value ● Minimum value ● Sum of all elements from a number list.
# num = [1,6,9,59,4,0,38,2.9]

# print("Maximum=", max(num))
# print("Minimum=", min(num))
# print("Sum =", sum(num))

#Q34. Create a list of 10 numbers and print: ● First 5 elements ● Last 3 elements ● Alternate elements using slicing
# list1 = [10,40,39,20,50,40,20,50,60,20]
# print(list1[0:5])
# print(list1[-3:])
# print(list1[::2])     #Alternate elements म्हणजे एक सोडून एक element.


##SECTION--9: Tuples

#Q35. Create a tuple containing: ● Name ● Age ● City Print all values separately.
# student = ("Ishwari", 19, "Nagpur")

# print("Name:", student[0])
# print("Age:", student[1])
# print("City:", student[2])

#Q36.Try changing a tuple value and observe what happens. 
# my_tuple = (10, 20, 30)
# my_tuple[1] = 50                   #Tuple तयार झाल्यानंतर त्यातील values बदलता येत नाहीत that's way tuple is immutable
# print(my_tuple)

#Q37. Create a tuple with 5 numbers and find: ● Maximum value ● Minimum value ● Total sum
# numbers = (10, 25, 5, 40, 15)

# print("Maximum Value:", max(numbers))
# print("Minimum Value:", min(numbers))
# print("Total Sum:", sum(numbers))

#Q38.Perform tuple packing and unpacking using student details.
# # Tuple Packing
# student = ("Ishwari", 19, "Nagpur")
# print("Packed Tuple:", student)

# # Tuple Unpacking
# name, age, city = student
# print("Name:", name)
# print("Age:", age)
# print("City:", city)

# #Q39. Create a mini ATM menu: ● Check balance ● Deposit ● Withdraw ● Exit Use loops and conditional statements.
# balance = 1000

# while True:
#     print("----- ATM MENU -----")
#     print()
#     print("1. Check Balance")
#     print("2. Deposit")
#     print("3. Withdraw")
#     print("4. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         print("Current Balance:", balance)

#     elif choice == 2:
#         amount = float(input("Enter deposit amount: "))
#         balance += amount
#         print("Amount Deposited Successfully!")
#         print("Updated Balance:", balance)

#     elif choice == 3:
#         amount = float(input("Enter withdrawal amount: "))
        
#         if amount <= balance:
#             balance -= amount
#             print("Amount Withdrawn Successfully!")
#             print("Remaining Balance:", balance)
#         else:
#             print("Insufficient Balance!")

#     elif choice == 4:
#         print("Thank You for Using ATM!")
#         break

#     else:
#         print("Invalid Choice! Please try again.")
        
# #Q40. Create a student result management program using lists and conditions. 
# # Requirements: 
# #   ● Store student marks 
# #   ● Calculate average 
# #   ● Display grade 
# #   ● Show highest marks

# # Store student marks in a list
# marks = [85, 78, 92, 88, 76]

# # Calculate average
# average = sum(marks) / len(marks)

# # Show highest marks
# highest_marks = max(marks)

# # Display grade
# if average >= 90:
#     grade = "A+"
# elif average >= 80:
#     grade = "A"
# elif average >= 70:
#     grade = "B"
# elif average >= 60:
#     grade = "C"
# else:
#     grade = "Fail"

# # Display result
# print("Student Marks:", marks)
# print("Average Marks:", average)
# print("Grade:", grade)
# print("Highest Marks:", highest_marks)