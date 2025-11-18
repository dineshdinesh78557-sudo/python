# 1. Grade Calculator
# Input marks → Output grade using multiple conditions:

# 90–100 → “A+”

# 80–89 → “A”

# 70–79 → “B”

# 60–69 → “C”

# Below 60 → “Fail”

# mark = 79

mark=int(input("enter the marks"))


if mark>=90 <=100:
    print("a")  
elif mark>=80 <=89:
    print("a")
elif mark>=70 <=79:
    print("b") 
elif mark>=60 <=69:
    print("c")  
else:
    print("fail")

# #     Day of the Week
# # Input a number (1–7) → Output the corresponding day.
# # 1 → Monday 2 → Tuesday ... 7 → Sunday

day=int(input("enter day number (1-7):"))

if day ==1:
    print("monday")

elif day ==2:
    print("thuesday")    
elif day ==3:
    print("wesnesday")
elif day ==4:
    print("thuesday")
elif day ==5:
    print("friday")  
elif day ==6:
    print("sataday") 
elif day ==7:
    print("sunday")   

# #     . Leap Year Checker
# # Check if a year is a leap year:

# # Divisible by 4

# # Not divisible by 100 unless divisible by 400  
# # 

year=int(input("enter the number")) 

if year %4==0 and 100!=0 or year %400==0:
    print("leap year")

else:
    print("not leap year")  

#     4. Find the Largest of Three Numbers
# Use if-elif-else to determine the largest number among three inputs.  

a= int(input("first number"))
b= int(input("second number"))
c= int(input("three number"))

if a>=b and a<=c:
    print("a largest")
elif b>=a and b<=c:
    print("b largest")
else:
    print("c largest")  
# 
# 

# # Basic Calculator
# # Take two numbers and an operator (+, -, *, /) → Perform the operation using if-elif-else.

a= float(input("first number"))
b= float(input("second number"))
op=(input("operators + - / *"))

if op == '+':
    print("a+b")
elif op == 'a-b':
    print("subtraction")
elif op == 'a/b':
    print("moduls")  
elif op =='a*b':
    print("multiplication")          



# # . Traffic Signal
# # Input signal color → Output action:

# Red → “Stop”

# Yellow → “Get ready”

# # Green → “Go”

signal= int(input("signal color red yellow green"))

if signal =="red":
    print("stop")
elif signal =="yellow":
    print("get reddy") 
elif signal =="green":
    print("go")
else:
    print("invaild color1")     

  
# #   . BMI Calculator
# # Input weight (kg) and height (m) → Calculate BMI and classify:

# BMI < 18.5 → “Underweight”

# 18.5 ≤ BMI < 24.9 → “Normal”

# 25 ≤ BMI < 29.9 → “Overweight”

# BMI ≥ 30 → “Obese”

weight =float(input("weight(kg) height(m)"))

if weight <18.5:
    print("underweight")
elif weight <24.9:
    print("normal")  
elif weight <29.9:
    print("over weight")
else:
    ("obese")        


# # Input month number (1–12) → Output month name using if-elif.

month =int(input("enter the month (1-12):"))

if month ==1:
    print("jan")
elif month ==2:
    print("feb")  
elif month ==3:
    print("mar")  
elif month ==4:
    print("apr")  
elif month ==5:
    print("may")   
elif month ==6:
    print("june") 
elif month ==7:
    print("july") 
elif month ==8:
    print("aug") 
elif month ==9:
    print("sep") 
elif month ==10:
    print("oct")  
elif month ==11:
    print("nov") 
elif month ==12:
    print("dec")                               


# Day Type
# Input day name → Output:

# “Weekend” → if Saturday or Sunday

# “Weekday” → else

day =int(input("enter a day"))

if day =="saturday" or day =="sunday":
    print("weekend")
else:
    print("weekend")  

#     Character Classification
# Input a character → Check if:

# Vowel

# Consonant

# Digit

# Special character  

ch =int(input("@ # $ %"))

if ch=="special character":
    print("@ # $" "%")

elif ch=="1,2,3":
    print("digit") 




