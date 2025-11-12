
# #name =>upper
# #number, num2  multply
# #10  from 10....1
# #number even uh print
# #num postive neg


def name (s):
    print(s.upper())
    # print("dinesh")

name("dinesh")

def number (a,b):
    print(a*b)
number(10,10) 

def form ():
    for i in range(10,0,-1):
        print(i)   
form()  



def even ():
    for i in range(10,):
        if i% 2==0:
            print(i)
even()  


def num (num):
   if num >0:
      print("positive no")
   elif num<0:
      print("negative no")  
   else:
      print("zero") 
num(-8)    
num(5) 
num(-4)

num(0)



#area of rectangle
#area of circle

#ask for quantity from using multiply by 100
# ask for name connvert to upper



# area of rectangle
def areaofrec(l,w):
   print(4/4*(l*w))
areaofrec(50,4) 


# area of rectangle
def areaofrec(l,w):
   print(4/4*(l*w))
areaofrec(50,4) 


# #ask for quantity from using multiply by 100
def quantity_multiply():
    quantity=int(input("enter the multiply:"))
    multiply=quantity*100
    print("enter quality:",multiply)
quantity_multiply()   


# # # # ask for name connvert to upper

def name(s):
    print(s.upper())
name("dinesh")    



# create add function list 10 append

def add(num):
    add=[1,3,4,5]
    add.append(num)
    print(add)
add(int(input("enter num")))



# # #create a list, remove the given number

def list():
    list=[1,2,3,4,5]
    list.remove(4)
    print(list)   
# list()  

#  get two numbers from user and multiply and display it

def number():
    user1=int(input("enter multiply no:"))
    user2=int(input("enter multiply no:"))
    result=user1*user2
    print(print(f"{user1} X {user2} = {result}"))
number()   



# #get name from user and reverse it  

def reverse_name():
    name=input("enter a name:")
    print("reverse name:",name[::-1])

reverse_name()    
    
   