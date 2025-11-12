class person: #This is comman class--->super class, parent class

    def __init__(self,name,age,gmail,id):#constructors
        self.name=name
        self.age=age
        self.gmail=gmail
        self.id=id

    def __str__(self):
        return  f'name---{self.name} age----{self.age}   gmail----{self.gmail}  id-----{self.id}'
    
    def greet(self):
        return f'hello {self.name}'
    

class student(person):
    def __init__(self, name, age, gmail,id, course,fees,details):
        super().__init__(name, age, gmail,id)
        self.course=course
        self.fees=fees
        self.details=details

    def __str__(self):
        return  f'name---{self.name} age----{self.age}   gmail----{self.gmail}  id-----{self.id} {self.course} {self.fees} {self.details}'
    
    def providDetails(self):
        return f" your course is {self.course} with fees {self.fees}. you choosed {self.details}"


st1=student('dinesh',20,'din@gmail.com',123456,'btech it',60000,'hostel')

print(st1)
    

print(st1.course)

print(st1.providDetails())