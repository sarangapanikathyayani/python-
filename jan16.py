'''Seee we can write multiple statements in one line but it is not good practice
it reduces readablity of the code try to avoid multiple statements in single line
but still you can write multiple statements by using this tereminator'''#;'''
a=10;b=20;c=a+b;
print(a);print(b);print(c)

'''Some statements may become very long and may force you to scroll the screen
left and right
frequently.
You can fit your code in such a way that you do not have to scroll here and there.
Python allows you to write a single statement in multiple lines, also known
as line continuation.
They are two types lc
1)implict continuation
2)explict continuation'''

# Example 1 

# The following code is valid 
a = [ 
    [1, 2, 3], 
    [3, 4, 5], 
    [5, 6, 7] 
    ] 

print(a) 

# Example 2 
# The following code is also valid 

person_1 = 18
person_2 = 20
person_3 = 12

if ( 
person_1 >= 18 and
person_2 >= 18 and
person_3 < 18
): 
	print('2 Persons should have ID Cards') 
'''Explicit Line Continuation
Explicit Line joining is used mostly when implicit line joining is not applicable.'''
# Example 

'''x =1 + 2 \ 
   + 5 + 6 \ 
   + 10

print(x) '''
# Example 

x = [1, 2, 3] 
y = 2

""" Following is incorrect, and will generate syntax error 
a = yin x 
"""

# Corrected version is written as 
a = y in x 
print(a) 
# Example 

'''x = 10

while(x != 0):
    if(x > 5):
        print('x > 5') 
    else:
        print('x < 5') 
x -= 2'''
'''Taking multiple inputs from user in Python
for taking multiple inputs from user we are using two methods 1) spilt method
2) by using list comprehension'''
#split method
x,y=input("enter two values").split()
print("Number of boys:",x)
print("number of girls",y)
'''x,y,z=int(input("enter three values:")).split()
print("Number of dooo",x)
print("Number of doo",y)
print("Number of thoo",z)'''
#hence here you cannot convert it into directly to convert t you have to do like this
#x=int(x)
#y=int(y)
#or  to convert it into all values for that #int_values = [int(val) for val in values]'''


values=input("enter two  values ").split()
int_values=[int(val) for val in values] # we used for loop for entering all values into float or integer
x,y=int_values
print(x,y)

values=input("enter all values of float type").split()
float_values=[float(val) for val in values]
x,y,z,u,w,x=float_values
print(x,y,z,u,w,x)

x, y = [int(x) for x in input("Enter two values: ").split()]
print("First number is {} and second number is {}".format(x, y))
  #format is used for instead of using the word again and again {} we just give brackects and at last we give format method atlast

x = [int(x) for x in input("Enter multiple values: ").split()]
print("Number of list is: ", x) 






