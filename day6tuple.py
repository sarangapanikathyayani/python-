'''a=(1,2,3,4)
print(a)
print(type(a))
b=list(a)
print(b)
print(a)
c=a.index(4)
print(c)
#two built in methods in python
d=a.count(2)
print(d)

print(a)
#sets
#$1 Doesnot allow duplicate values
#$2 if you type duplicate values it will remove automaticaly
a={1,2,3,4,1}
print(a)
#$3 we cannot modify set item
a[2]=5
a.add(10)
print(a)
# $4 i can add and remove also
a.remove(4)
print(a)'
#$5 SETS ARE UNORDERED
a.pop()
print(a)

#clear() method
b=a.clear()
print(b)
a.clear()
print(a)
#copy()
a={1,2,3,4}
print(a)
b=a.copy() #in b set the element has been copied
print(b)
 #difference()
a={1,2,3,4}
b={3,4}
c=b.difference(a)
d=a.difference(b)
print(c)
print(d)

#difference_update()
a={1,2,3}
b={4,5,3}
a.difference_update(b)
#intersection()
c=a.intersection(b)


print(c)
print(a)


#discard()
#it removes the specifed item

a.discard(1)
print(a)'''

#intersection_update()

a={1,2,3,4}
b={3,4,5,2,1}
a.intersection_update(b)
print(a)


c=a.isdisjoint(b)
print(c)






















