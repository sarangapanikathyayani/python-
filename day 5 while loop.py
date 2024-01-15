#while loop
'''i=0
while(i==0):
    print(i)
    i=1; #output 0 
while(False):
    print("true") #no output
#print numbers from 1 to 5 using while loop
i=0
while(i<=5):
    print(i)
    i=i+1
i=1
while(i<=5):
    print(i)
    i=i+1
i=1
while(i<=5):
    print(i)
#10,20,30..............200
i=10
while(i<=200):
    print(i,end=',')
    i=i+10
#to print 10 natural numbers in reverse order
i=10
while(i>0):
    print(i)
    i=i-1

i=5
while(i>0):
    print(i,end='')
    print(i*i-1*i-2*i-3*i-4)
    i=i-1
    i=int(input())'''
####factorial program
i=int(input())
fact=1
while(i>0):
    fact=fact*i
    i=i-1
print(fact)
i=int(input())
fact=1
while(i>0):
    fact=fact*i
    i=i-1
    print(fact)
    
    
