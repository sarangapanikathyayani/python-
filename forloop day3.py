'''for i in range(1,11):
    print(2,"*1=",2*i)
a=int(input())#for knowing how many numbers in the range u have to use range function
b=int(input())
for i in range(a+1,b):
    print(i)
#print even numbers b/w 1  to 10
for i in range(1,10):
    if(i%2==0):
        print(i)
print("odd numbers b/w 1 to 10")
count=0
j=0
for i in range(0,10):
    if(i%2==0):
        count=count+1
    else:
        j=j+1

print("even numbers:",count)
print("odd numbers:",j)
#count the numbers divisible by 3 and 5 in range 1 to 100
count=0
for i in range(1,100):
    if(i%3==0 and i%5==0): #if only both are true then and we will use
        print(i)
        count=count+1
print("numbers divisibke by 3 and 5:",count)
count=0
for i in range(0,5):
    count=count+i
print(count)
    
#T0 store collection of data for 10 inputs then we use list
a=[1,2,3,4,5]
for i in a:
    print(i)
a=[]
a.append(10)
a.append(20)#append says to print the element at last in the list
a.append(30)
a.append(40)
b=int(input())
a.append(b)
print(a)
print(b)
a=[]
sum=0
for i in range(5):
    num=int(input())
    a.append(num)
for i in a:
    sum=sum+i    
print(a)

print(sum)'''

