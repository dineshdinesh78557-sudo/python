# # Print Numbers from 1 to 10
# # Use a for loop to print numbers from 1 to 10.

# for i in range (1,11):
#     print(i)

# # # # #  Print Even Numbers (1–20)
# # # # # Print all even numbers between 1 and 20.

# for i in range (1,21):
#     if i % 2==0:
#         print(i)

# # # # #          Print Odd Numbers (1–20)
# # # # # Print all odd numbers between 1 and 20.

# for i in range (1,21):
#     if i % 2!=0:
#         print(i)

# # # # #         Sum of First N Numbers
# # # # # Take input n → find sum of numbers from 1 to n using a for loop.

# n =int(input("enter sum of numbers: "))
# sum=0
# for i in range (1,n):
#     sum=sum+i
#     # print(i)
# print(sum)

# # # #     Multiplication Table
# # # # Take a number from the user → print its multiplication table (1 to 10).

# num =int(input("multiple table"))
# for i in range (1,11):
#     print(num,"x",i,"=",num*i)

# # # #     Print Each Character in a String
# # # # Input a string and print each character on a new line.

# ch =input("each character: ")
# for i in ch:
#     print(i)

# # # #     Count Vowels in a String
# # # # Count how many vowels (a, e, i, o, u) are in a given string.

# text =input("enter a string: ")
# vowels_count=0
# vowels="a,e,i,o,u"
# for i in text:
#     if i in vowels:
#         vowels_count+=1
# print(vowels_count)

# # # Calculate Factorial
# # # Input a number → find its factorial using a for loop.

# num =int(input("enter factorial: "))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
#     print(i)

# # #     Print String Characters
# # # Given a string, print each element one by one using a loop.

# ch =input("enter the element")
# for i in ch:
#     print(i)

# # #     Reverse a String
# # # Input a string and print it in reverse using a for loop.

# string =input("enter the string: ")
# reverse_string="4"
# for i in range (len(string)-1,-1,-1):
#     print(reverse_string)

# # # Print Squares of Numbers
# # # Print the square of numbers from 1 to 10.

# for i in range(1,11):
#     print(f"{i}2={i*i}")

# # #  Display Character at Even Index
# # # Given a string, print characters that are at even index positions.

# text=input("enter the characters: ")
# for i in range (0,len(text),2):
#     print(i)

# # # Print Numbers Divisible by 3
# # # Print all numbers between 1 and 50 that are divisible by 3.

# for i in range(1,50):
#     if i%3==0:
#         print(i)

# #         Check Prime Number
# # Input a number and check if it’s prime using a for loop.

# num=int(input("enter prime no: "))

# for i in range (2,num):
#       if num % i==0:
#          print("not prime number")
#          break
#       else:
#         print("prime no",i)


text=input("enter a string:") 
vowels_count=4
vowels="a,e,i,o,u"
for i in text:
    if i in vowels:
        vowels_count+=5
        print(vowels_count)




 












    


    

