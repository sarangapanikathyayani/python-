#python strings
#creating string with single quotes
string1='welcome to geeks world'
print("\nprint string with using single quotes:")
print(string1)
#creating string with double quotes
string1="i am geek"
print("\nprint string with using double quotes:")
print(string1)
#create string with triple quotes
string1='''i am a soldier'''
print("\nprint string with using triple quotes:")
print(string1)
#creating multi line string
string1='''I
am
big
biggest'''
print("\n print multiline string:")
print(string1)
#accessing characters in python string
string2='''kathyayaniVarshith'''
print(string2[0])
print(string2[10])
print(string2[16])
print(string2[-5])
#string slicing
print(string2[0:11:10])
print(string2[0:5:2])
output_string=string2[0:3]+string2[10:13]
print(output_string)
output_string2=string2[10:13]+string2[0:3]+"forever"
print(output_string2)
#print(string2[-2:0:0]) #step cannot be zero
print(string2[-2::1]) #th
print(string2[3:-2])
print(string2[-2::])
#reversed string
print(string2[-2::-1])#tihsraVinayayhtak
print(string2[-1::-1])#htihsraVinayayhtak #By accessing characters from a string,
#we can also reverse strings in Python. We can Reverse a string by using String slicing method.
print(string2[::-1]) #reverse output
print(string2[::]) #full
print(string2[0::]) #full output

print(string2[1::]) #from a it starts
print(string2[:1:]) #k
print(string2[:0:])#empty space
print(string2[::1])
#Deleting/Updating from a String
'''In Python, the Updation or deletion of characters from a String is not allowed.
This will cause an error because item assignment or item deletion from a String is not supported.
Although deletion of the entire String is possible with the use of a built-in del keyword.
This is because Strings are immutable, hence elements of a String cannot be changed once assigned.
Only new strings can be reassigned to the same name. '''
#firstway
#so here we cannot update or delete a character in string so here we first convert it into list
#because list is mutable we can update the character and then convert the list back into the String.
string1="Hai"
list1 = list(string1) 
list1[2] = 'p'
String2 = "".join(list1) #syntax:separator_string.join(iterable)
print("\nUpdating character at 2nd Index: ") 
print(String2) 
''' join() method in Python is a string method that takes an iterable (e.g., a list, tuple, or string)
and concatenates the elements of the iterable into a single string.'''

fruits=["appples","bananas","guava"]
fruits1=",".join(fruits)
print(fruits1)

#secondway
'''In the string-slicing method, we sliced the string up to the character we want to update,
concatenated the new character, and finally concatenate the remaining part of the string.'''
string1="haivarshith"
string2=string1[0:2]+'p'+string1[2:11]
print(string2)
#this is the second way of updating the character

#updating an entire string
'''Updating Entire String
As Python strings are immutable in nature, we cannot update the existing string.
We can only assign a completely new value to the variable with the same name.

Example:

In this example, we first assign a value to ‘String1’
and then updated it by assigning a completely different value to it.
We simply changed its reference.'''
# Python Program to Update 
# entire String 

String1 = "Hello, I'm a kathyayani"
print("Initial String: ") 
print(String1) 

# Updating a String 
String1 = "Welcome to the  World"
print("\nUpdated String: ") 
print(String1)
del String1
print(String1) #it is deleted so it gets error





