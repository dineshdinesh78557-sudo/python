# #if elif:

a=9087
b=928
c=123
if(a>b and a>c):
    print("a is big")
elif b>c:
    print("b is big")
else:
    print("c is big")

mark =56
mark2 =90
mark3=78

if(mark>=50 and mark2>=50 and mark3>=50):
    print("pass")

else:
    print("fail")



proof = input("enter your type of proof")

if(proof=="aadhar"):
    print("aadhar card accepted")

elif(proof=="voter id"):
    print("voter id accepted")
elif(proof=="passport"):
    print("passport accepted")
else:
    print("invalid proof")


import math

array=[0,1, False, 2,'',3,None,float('nan'),'welcome']
values=[x for x in array if x and not (isinstance(x, float) and math.isnan(x))]
print(values)





