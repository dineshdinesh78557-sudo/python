#set - ignore duplicate values, unoredered
marks={10,12,12,13,10,24,10,24} #set
print(marks)

marks.add(11)
print(marks)


marks.pop()
print(marks)



d={1,2}
a={1,2,3,4,5,6,7}
b={5,6,7,8,8,9}
c={90,89}

print(a.union(b))#provide all elements
print(a.intersection(b)) #common elements only

print(a.difference(b))#it will check which item missing in b

print(b.isdisjoint(c))#check wheather it is completely diff

print(d.issubset(a))


c.discard(89)#it will remove particular value
print(c)

marks={10,10,11,11,13,22}
print(marks)

marks.add(33)
print(marks)

marks.pop()
print(marks)

a={1,2,3,4,5,6,7,8,9}
b={6,7,8,9,10,11}
c={70,80}
d={21,33}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(b.isdisjoint(c))
print(d.issubset(a))