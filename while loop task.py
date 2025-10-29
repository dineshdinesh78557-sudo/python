# 1. Print 1 to 10
# Write a program to print numbers from 1 to 10 using a while loop

i=1
while (i<=10):
    print(i)
    i=i+1

#      Print Even Numbers
# Print even numbers from 2 to 20 using a while loop.

i=2
while (i<=20):
    print(i)
    i=i+2

#     Print Odd Numbers
# Print odd numbers from 1 to 19 using a while loop.

i=1
while(i<=20):
    print(i)
    i=i+1

#     Sum of First N Numbers
# Take an integer input n and find the sum of numbers from 1 to n.

n =int(input('enter the number'))
sum=0
i=2
while(i<n):
    sum=sum+i
    print(sum)
    i=i+2



#     Multiplication Table
# Take a number from the user and print its multiplication table (up to 10).


num =int(input('enter multiple number'))
sum=1
while(sum<=6):
    # print(sum,"x",num,"=",sum*num)
    print(f"{sum} X {num} = {sum*num}")
    sum=sum+1
    

#     Reverse Counting
# Print numbers from 10 to 1 using a while loop.

i=10

while(i>=2):
    print(i)
    i=i-3











