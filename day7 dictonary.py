'''a={
    "name":"emc",
    "age":"1",
    "location":"xyh"
    }
print(a)
#only for keys
print(a.keys())
#only for values
print(a.values())
a["age"]=2
print(a)'''
#functions
def painter():
    print("paint chey amma")
painter()
#functions still more
a=10
b=20
def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
def div():
    print(a/b)
add()
sub()
mul()
div()
#functions to find even or odd
'''num=int(input())
def findevenorodd():
    if(num%2==0):
        print("even")
    else:
        print("odd")
findevenorodd()'''
def findevenorodd(num):
    if(num%2==0):
        print("even",num)
    else:
        print("odd",num)
findevenorodd(8)
