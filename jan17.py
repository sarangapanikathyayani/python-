'''num=input("enter number")
for i in range(num):
    print(i)'''
#if u dont write int there string cannot be intrepeted as integer
'''num=int(input("enter number"))
val=0
for i in range(num):
    print(i,end=" ")
    val+=i
print("sum of numbers",val)'''
#this is the output
'''enter number5
0 1 2 3 4 sum of numbers 10 but here i dont want in only a single line so i just
added \n newline in the begining of the sentence and also i want to start with 1
so i used here range function'''
#about range function range(start,stop,step)

'''The range() function in Python is used to generate a sequence of numbers within a specified range.
It is often used with for loops to iterate over a sequence of numbers.
The basic syntax of the range() function is as follows:
range(start, stop, step)
start: The starting value of the sequence (optional, default is 0).
stop: The end value of the sequence (exclusive).
step: The step or interval between each number in the sequence (optional, default is 1).'''
#Input: 
'''5
1 2 3 4 5
Output:
15'''
num=int(input("enter number"))
val=0
for i in range(1,num+1): #if you give num then it stops upto the before number only
    print(i,end=" ")
    val+=i
print("\nsum of numbers",val)
#Input Methods for Competitive Programming in Python
'''Normal Method
Faster Method using Inbuilt Function
Taking User Input Given in a Single Line in Separate Variables
Taking User Inputs of List of Integers
Taking String Input from the User
Adding a buffered pipe io'''
#normal method
#here user will give the inputs

# input N
n = int(input())

# input the array
arr = [int(x) for x in input().split()]

# initialize variable
summation = 0

# calculate sum
for x in arr:
	summation += x
	
# print answer
print(summation)
#Faster Method using Inbuilt Function
'''but this makes memory usage dependent on the size of the input.'''
#Taking User Input Given in a Single Line in Separate Variables




#map
'''the map() function in Python is a built-in function that is used for
applying a given function to all items in an iterable
(such as a list) and returns an iterable map object (an iterator).
The basic syntax of the map() function is as follows:
map(function, iterable, ...)
function: The function to apply to each item in the iterable.
iterable: The iterable (e.g., list, tuple) whose elements will be processed by the function.'''
#example 1
def square(x):
    return x**2
numbers=[1,2,3,4,5]
squared_numbers=map(square,numbers) #dont print it directly if u print it directly it will give u the address
#so again convert it into list
result=list(squared_numbers)
print(result)

#example 2
def add(x):
    return x+x
num=[int(x) for x in input().split()]
add_numbers=map(add, num)
result=tuple(add_numbers)
print(result)

    #have to discuss about map with lambda


