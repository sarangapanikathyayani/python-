#lambda expressions
'''actualy lambda is an anonymous function that means it has no name
if u consider def is a normal function by using def we will run the code in lines
but by using lambda we will finish in one line'''
#see the difference between example 1 and example 2
#example 1
def add(x):
    return x+x
num=[1,2,3,4]
add_num=map(add,num)
result=list(add_num)
print(result)
#but when u see lambda function
#example 2
lambda_add=lambda x:x+x
print(lambda_add(6))
#example 3
is_evenlist=[lambda arg=i:arg*10 for i in range(1,5)]

for item in is_evenlist:
    print(item())
#exampe 4
Max=lambda a,b:a if(a>b) else b
print(Max(1,2))
#example 5 About sorted and sort
numbers=[1,8,5,7]
sorted_numbers=sorted(numbers)
print(sorted_numbers)
print(numbers)
#example 6
numbers=[4,3,5,6]
numbers.sort()
print(numbers)
#now by using sorted() u cannot change orginal value but u can change orginal value
list=[[2,3,6],[4,5,7],[8,11,4]]
sortlist=lambda x:(sorted(i) for i in x)
secondLargest = lambda x, f : [y[len(y)-2] for y in f(x)]
res = secondLargest(list, sortlist)
 
print(res)
