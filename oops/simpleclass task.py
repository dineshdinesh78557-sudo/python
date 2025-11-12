# # Simple Class Tasks

# # Car Class

# # Create a class Car with instance variables: brand, model, year.

# # Add a method car_info() to display details.

# # Create 2â€“3 objects and print their details.

class car:
    

    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def car_info(self):
        print(f"brand:{self.brand}, model:{self.model}, year:{self.year}")  

car1=car("toyoto","hp",2002) 
car2=car("swift","suzki",2022)    
car3=car("bmw","b",2025)   

car1.car_info()
car2.car_info()
car3.car_info()

# # # Bank Account

# # # Create a class BankAccount with instance variables: owner, balance.

# # # Add methods:

# # # deposit(amount) â†’ increases balance

# # # withdraw(amount) â†’ decreases balance if funds available

# # # Test with different transactions.


class bank:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit (self,amount):
        self.balance+=amount
        print(f"{amount}: balance:{self.balance}")
    def withdraw(self,amount):
       if amount < self.balance:
           self.balance  -=amount
           print(f" {amount}:remaing balance: {self.balance}")
       else:
           print("inficcent balance")
              
bank1=bank("dinesh",1000)

bank1.deposit(1000)
bank1.withdraw(100)
bank1.withdraw(100)


# # Student Marks

# # Create a class Student with instance variables: name, marks (list).

# # Add a method to calculate average marks.

# # Add another method to check grade (A, B, C).

class Mark:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"{self.name}, {self.marks}"
    def average(self):
        total=0
        for mark in self.marks:
            total=total+mark
            avg=total/len (self.marks)
            return avg

    def grade(self):
        avg = self.average()
        if avg >= 80:
            return "A"
        elif avg >= 50:
            return "B"
        else:
            return "C"

m1 = Mark("Dinesh", [80, 90, 70])
m2 = Mark("Gokul", [85, 34, 78])
m3 = Mark("Ravi", [50, 70, 70])

print(m1.average())
print(m1.grade())

# # # Library Book

# # # Create a class Book with variables: title, author, available (True/False).

# # # Add methods:

# # # borrow_book() â†’ mark as not available

# # # return_book() â†’ mark as available

# # # Create multiple books and test borrowing/returning.

class book:

    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.available=True

    def  borrow_book(self):
         self.available=False
          
    def return_book(self):
       self.available=True
           
      
    def __str__(self):
        return f"{self.title}by{self.author}-{self.available}"
    
         
book1=book('python programming','guido van Rossum')
print(book1)
book1.borrow_book()
book1.return_book()
# # #

# Employee Salary

# Create a classC with instance variables: name, salary.

# Add a class variable company_name.

# Add a method to give a 10% bonus to salary.

# Print employee details before and after bonus.
        
class employe:
    company_name="a,b,c"

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def bouns_salary(self):
        self.salary +=self.salary*100.2
    def n (self):
        print(f"name:{self.name},salary:{self.salary},company:{self.company_name}") 

employe1=employe("dinesh",1000)
employe2=employe("rohit",2000)
print("Before bonus:1000")



print("After bonus:200")
           


        


        


 

        
        


        


        

