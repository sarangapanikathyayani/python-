import keyword
keys=["kathyayani","bat","false","if","else","true","True"]
for i in range(len(keys)):
               
               if keyword.iskeyword(keys[i]):
                       print(keys[i],"is a keyword")
               else:
                   print(keys[i],"is not a keyword")
''' some times remembering all the keywords is a difficult task so we acan
use #keywords.kwlist'''
import keyword
print("The list of keywords:")
print(keyword.kwlist)  #keyword was already inbuilt in it so  use only keyword
a,b,c="geeks","for","geeke"
print(a,b,c)
print(a+b+c)
print("a=",a)
print("b=",b)
print("c=",c)
''' actualy they are 2 methods for initializing  the variables
1.direct initialization
2.using conditional operator'''
a=1 if 20>10 else 0
print("value of a:",a)
a=1 if 20<10 else 0
print("value of a:",a)
a=11 if 20<10 else 0
print("value of a:",a)
a=11 if 20>10 else 0
print("value of a:",a)
'''print without new line  in python
 people switching from C/C++ to Python wonder how to print
 two or more variables or statements without going into a new line in python'''
#1)comma operater
print("geeks")
print("geeksforgeeks")
'''by keeping , comma operator without goint to new line u can print in next line'''
print("geeks"),print("geeksforgeeks")
#2) for loop
a=[1,2,3,4]
for i in  range(4):
    print(a[i])
#now print without a new line
print("geeks",end=" ")
print("geeksforgeeks")

a=[1,2,3,4]
for i in range(4):
    print(a[i],end=" ")
#hence here we are using end parameter for not going to new line
print("hai")
'''    Print without newline in Python 3.x without using For Loop'''
# using * symbol prints the list
# elements in a single line
a=[1,2,3,4,5]
print(*a)
#Print without newline Using Python sys module
'''To use the sys module, first, import the module sys using the import keyword.
Then, make use of the stdout.write() method available inside the sys module, to print your strings.
It only works with string If you pass a number or a list, you will get a TypeError.'''
import sys
sys.stdout.write("geeksforgeeks ")
sys.stdout.write("govinda govinda  ")
print("hai")
i=10
print(True) if i<15 else print(False)
a, b, c, d, e, f = 0, 5, 12, 0, 15, 15
exp1 = a <= b < c > d is not e is f
exp2 = a is d > f is not c
print(exp1)
print(exp2)

'''basic calucator program'''
def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
def mod(num1,num2):
    return num1%num2
print("select any operation \n"\
      "1)Add"\
      "2)sub"\
      "3) mul"\
      "4)div" \
      "5)mod")

select=int(input("select any number from 1to 5: "))
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
if select==1:
           print(num1+num2)
elif select==2:
           print(num1-num2)
elif select==3:
           print(num1*num2)
elif select==4:
           print(num1/num2)
elif select==5:
           print(num1%num2)

else:
    print("what u had selected is out of the numbers")





               
            




               
            
