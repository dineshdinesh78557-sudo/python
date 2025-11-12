class student:

    def __init__(self,name,age,gmail):#constructors
        self.name=name
        self.age=age
        self.gmail=gmail

    def __str__(self):
        return  f'name---{self.name} age----{self.age}   gmail----{self.gmail}'
    
    def greetStudent(self):

        return f'Welcome!!!!!! {self.name}'
    

st1=student('dinesh',12,'dinesh@gmail.com')

print(st1)



st2=student('deepalk',12,'deepak@gmail.com')

print(st2)

print(st1.greetStudent())