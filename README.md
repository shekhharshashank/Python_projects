# Python_projects
# interactiveshell 

Ranges
You can create a list of numbers automatically using a range. For example:

list(range(1, 10))

That will output:

[1, 2, 3, 4, 5, 6, 7, 8, 9]

As you can see we just needed to specify the list boundaries inside range(). So, we specified 1and 10. Note that 10 is not included in the list. The generated list always runs up to one number before the upper number. In our example it goes up to 9 since the upper number is 10.

You can also specify a step as a third argument:

list(range(1, 10, 2))

That will output:

[1, 3, 5, 7, 9]

So, the count happens every two items starting from 1 and ending at 9.


#tuples are mutable
Lists are Immuatable

Summary: Integers, Floats, Lists, Dictionaries, Tuples, dir, help
In this section you learned that:

Integers are for representing whole numbers:

rank = 10
eggs = 12
people = 3
Floats represent continuous values:

temperature = 10.2
rainfall = 5.98
elevation = 1031.88
Strings represent any text:

message = "Welcome to our online shop!"
name = "John"
serial = "R001991981SW"
Lists represent arrays of values that may change during the course of the program:

members = ["Sim Soony", "Marry Roundknee", "Jack Corridor"]
pixel_values = [252, 251, 251, 253, 250, 248, 247]
Dictionaries represent pairs of keys and values:

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
volcano_elevations = {"Glacier Peak": 3213.9, "Rainer": 4392.1}
Keys of a dictionary can be extracted with:

phone_numbers.keys()
Values of a dictionary can be extracted with:

phone_numbers.values()
Tuples represent arrays of values that are not to be changed during the course of the program:

vowels = ('a', 'e', 'i', 'o', 'u')
one_digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
To find out what attributes a type has:

dir(str)
dir(list)
dir(dict)
To find out what Python builtin functions there are:

dir(__builtins__)
Documentation for a Python command can be found with:

help(str)
help(str.replace)
help(dict.values)


Summary: Positive/Negative Indexes, Slicing
In this section you learned that:

Lists, strings, and tuples have a positive index system:

["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
   0      1      2      3      4      5      6
And a negative index system:

["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
  -7     -6     -5     -4     -3     -2     -1
In a list, the 2nd, 3rd, and 4th items can be accessed with:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[1:4]
Output: ['Tue', 'Wed', 'Thu']
First three items of a list:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:3]
Output:['Mon', 'Tue', 'Wed'] 
Last three items of a list:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[-3:]
Output: ['Fri', 'Sat', 'Sun']
Everything but the last:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:-1] 
Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 
Everything but the last two:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:-2] 
Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'] 
A single in a dictionary can be accessed using its key:

phone_numbers = {"John Smith":"+37682929928","Marry Simpsons":"+423998200919"}
phone_numbers["Marry Simpsons"]
Output: '+423998200919'


Summary: Functions and Conditionals
In this section you learned to:

Define a function:

def cube_volume(a):
    return a * a * a
Write a conditional block:

message = "hello there"
 
if "hello" in message:
    print("hi")
else:
    print("I don't understand")
Write a conditional block of multiple conditions:

message = "hello there"
 
if "hello" in message:
    print("hi")
elif "hi" in message:
    print("hi")
elif "hey" in message:
    print("hi")
else:
    print("I don't understand")
Use the and operator to check if both conditions are True at the same time:

x = 1
y = 1
 
if x == 1 and y==1:
    print("Yes")
else:
    print("No")
Output is Yes since both x and y are 1.

Use the or operator to check if at least one condition is True:

x = 1
y = 2
 
if x == 1 or y==2:
    print("Yes")
else:
    print("No")
Output is Yes since x is 1.

Check if a value is of a certain type with:

isinstance("abc", str)
isinstance([1, 2, 3], list)
or

type("abc") == str
type([1, 2, 3]) == lst


Summary: Processing User Input
In this section you learned that:

A Python program can get user input via the input function:

The input function halts the execution of the program and gets text input from the user:

name = input("Enter your name: ")
The input function converts any input to a string, but you can convert it back to int or float:

experience_months = input("Enter your experience in months: ")
experience_years = int(experience_months) / 12
You can format strings with (works both on Python 2 and 3):

name = "Sim"
experience_years = 1.5
print("Hi %s, you have %s years of experience." % (name, experience_years))
Output: Hi Sim, you have 1.5 years of experience.

You can also format strings with:

name = "Sim"
experience_years = 1.5
print("Hi {}, you have {} years of experience".format(name, experience_years))
Output: Hi Sim, you have 1.5 years of experience.

Summary: Loops
In this section you learned that:

For loops are useful for executing a command over a large number of items.

You can create a for loop like so:

for letter in 'abc':
    print(letter.upper())
Output:

A
B
C

The name after for (e.g. letter) is just a variable name



You can loop over dictionary keys:

phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
for value in phone_numbers.keys():
    print(value)
Output:

John Smith
Marry Simpsons

You can loop over dictionary values:

phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
for value in phone_numbers.values():
    print(value)
Output:

+37682929928
+423998200919

You can loop over dictionary items:

phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
for key, value in phone_numbers.items():
    print(key, value)
Output: 

('John Smith', '+37682929928')

('Marry Simpons', '+423998200919')



While loops will run as long as a condition is true:

while datetime.datetime.now() < datetime.datetime(2090, 8, 20, 19, 30, 20):
    print("It's not yet 19:30:20 of 2090.8.20")
The loop above will print out the string inside print() over and over again until the 20th of August, 2090.




