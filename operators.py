#assignment operator =
#+=, -=, *=, /=, %=
a=90
b=10

a+=20  # a= a+10
a-=5  # a= a-5
a*=2 # a=a*2
a/=5 # a=a/5
a%=8 # a=a%3
print(a)


# if else

n=-90

if n>0:
    print("positive no")
    print(n+10)

else:
    print("negative no")
    print(n-10)

n=120
if n%5==0:
    print("yes,divisible")
else:
    print("not divisible ")

a=10
b=90

print(a+b)

a=130
b=5
print(a-b)

a=5
b=5
print(a*b)

a=5
b=5
print(a/b)

a=2
b=3
print(a%b)

# if else

n=-90

if n<0:
    print("positive no")
    print(n+10)

else:
    print("negitive no")
    print(n-10) 

n=120
if n%7==0:
    print("yes divisible")

else:    
    print("not divisible")

#     2. Odd or Even
# Check if a number is odd or even.
# Input: 8 → Output: “Even number”

n=8
if n%2==0:
    print("even numberr")

else:
    print("odd number")    

#     Largest of Two Numbers
# Take two numbers as input and print which one is greater.
# Input: 10, 20 → Output: “20 is greater”

n=10,20
if n==20:
    print("10 is greater")
else:
    print("20 is greater")  


#  4. Eligible to Vote
# Check if a person is eligible to vote. (Age ≥ 18)
# Input: 16 → Output: “Not eligible to vote”

n==16
if n==18: 
   print("eligble to vote")



# Check for Divisibility
# Check if a number is divisible by 5.
# Input: 25 → Output: “Divisible by 5”    

n=5
if n==5:
    print("divisible  by 5")



#  Check if a Number is Multiple of Both 3 and 5
# Input: 15 → Output: “Multiple of both 3 and 5”

n=5
if n==3:
    print("multiple of both 3 and 5")



#membership operator:in, not in

s = "Dinesh"

print("i" in s)
print("z" not in s )


#identity operator: is, is not, 
# is , will check the address of the variable 


a=90
b=90

li =[1,2,3]
li1=[1,2,3]

print( a is b)
print(li is li1)

# type(): returns data type

print(type(a))
print(type(li))


