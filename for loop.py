#for loop:

for i in range(1,11):  # start,end
    print(i)


for i in range(11): #end value
    print(i)

for i in range(1,11,2): # start, end, step
    print(i)

#string iteration

name = "Dinesh"

for i in name:
    print(i)

for i in range(0,len(name)):
    print(i, name[i])


name="python"
count=0
for i in name:
    if i=="a" or i=="e" or i=="o" or i=="u" or i=="i":
        print(i)
        count=count+1
print(count)



    