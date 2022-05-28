#!/usr/bin/env python
# coding: utf-8

# In[1]:


Python - basics
Various datatypes in python
String, Float, Integer, Boolean - single values
Lists, Sets, Tuples, Dictionary - collection of values (data structures)
Integer
Arithmetic operators
[18]
a=19  ## variable assignment
b=3
[19]
print(a+b)
22

[20]
a*b
57
[24]
b-a
-16
[21]
print(a**b)  ## raised to the power (exponentiation)
6859

[25]
a%b  ##modulo operator
1
[22]
print((a*b)+(a/b))   ###BODMAS
63.333333333333336

[13]
print(a/b)  ##division
6.333333333333333

[14]
print(a//b)  ##floor division
6

Certain inbuilt functions
[15]
type(a)  ###type() - to check the datatype
int
[16]
type('python')
str
[17]
type([1,2,3,4])
list
[23]
type(True)  ###boolean
bool
[26]
first_name = 'Laxmi'
last_name = 'Ravi'
[28]
print("My first name is {} and last name is {}".format(last_name,first_name))
My first name is Ravi and last name is Laxmi

[29]
print("My first name is {first} and last name is {last}".format(last=last_name,first=first_name))
My first name is Laxmi and last name is Ravi

[30]
help(round)  ##help()
Help on built-in function round in module builtins:

round(number, ndigits=None)
    Round a number to a given precision in decimal digits.
    
    The return value is an integer if ndigits is omitted or None.  Otherwise
    the return value has the same type as the number.  ndigits may be negative.


[31]
len(first_name)
5
String (text) ..' ', '' ''
[35]
type('3')
str
[33]
type('hello')
str
[40]
my_name = "Lakshmi"
[46]
print(my_name.isalnum())
print(my_name.isnumeric())
print(my_name.isdecimal())
print(my_name.istitle())
print(my_name.islower())
print(my_name.isspace())
True
False
False
True
False
False

Boolean operator - True/false (or) 0/1
[47]
True and True
True
[48]
True and False
False
[49]
True or True
True
[50]
False or True
True
[51]
type(True)
bool
Float
[52]
type(9.99)
float
List
[ ] square brackets, different data types
Mutable (Modify/change, add, remove)
each element in a list - item
[53]
lst = ['Maths', 'Science', 10,20,30,40]
[54]
len(lst)
6


# In[ ]:


String functions - split()
[1]
s = "hello"
[2]
s
'hello'
[3]
s[0]
'h'
[5]
s[0]='k' ### string sequences are immutable
---------------------------------------------------------------------------
TypeError Traceback (most recent call last)
<ipython-input-5-2707c8588208> in <module> ----> 1 s[0]='k' ### string sequences are immutable
TypeError: 'str' object does not support item assignment
[6]
s.upper()
'HELLO'
[7]
'This is my class'.split()
['This', 'is', 'my', 'class']
[21]
s = 'this is. my class'.split('.')
s
['this is', ' my class']
[9]
s.split()
['this', 'is', 'my', 'class']
[10]
'This is my class'.split('c')
['This is my ', 'lass']
[33]
record = '600100, Chennai, India'.split(',')
[34]
pin = record[0]
city = record[1]
country = record[2]
[19]
pin
'600100'
[40]
record = '600100, Chennai, India'.split(',', maxsplit=1)  ##optional
[41]
record
['600100', ' Chennai, India']
[42]
a = "hello"  ## Joining 2 string
b = "world"
[43]
print(" ".join([a,b]))  ## join() function
hello world

[28]
a+' '+b
'hello world'
[30]
a =  'World'
b = 20
a+ str(b)
'World20'
Indexing
[44]
text = "ice cream"
[52]
text[-5]
'c'
[50]
text[4:9]
'cream'
[45]
text[0]
'i'
[46]
text[4]
'c'
[47]
text[0:3]
'ice'
[48]
text[:7]
'ice cre'
[56]
text = "Let's learn python"
text
"Let's learn python"
List
[92]
num = [12, 23, 45, 77, 80]
[93]
num.append(40)
[94]
num
[12, 23, 45, 77, 80, 40]
[95]
num.extend([90,32]) 
num
[12, 23, 45, 77, 80, 40, 90, 32]
[74]
num.insert(2, 78)
[75]
num
[12, 23, 78, 45, 77, 80, 40]
[76]
num.remove(23)
[77]
num
[12, 78, 45, 77, 80, 40]
[78]
num.pop()
40
[79]
num
[12, 78, 45, 77, 80]
[80]
num.pop(1)
78
[81]
num
[12, 45, 77, 80]
[68]
del num[2:]
[69]
num
[12, 45]
[67]
## in-built functions
[82]
num = [12, 23, 45, 77, 80]
[83]
min(num)
12
[84]
max(num)
80
[85]
sum(num)
237
[86]
names = ["Kate", "John", "Mia"]
values = [19.6, "House", 40]
[87]
misc = [names, values]  ### nested list
misc
[['Kate', 'John', 'Mia'], [19.6, 'House', 40]]
[96]
misc[1][2]
40
Sets
unordered collection of data types, mutable
NOTE: NO DUPLICATE ELEMENTS

[100]
a = {1,3,2,4,6,7,8,2,5,3,1,1}
[98]
type(a)
set
[99]
a
{1, 2, 3, 4, 5, 6, 7, 8}
[102]
a[0]   ###Sets do not support indexing
---------------------------------------------------------------------------
TypeError Traceback (most recent call last)
<ipython-input-102-8c4982f4a684> in <module> ----> 1 a[0] ###Sets do not support indexing
TypeError: 'set' object is not subscriptable
[103]
movies = {"hulk", "iron", "fb"}
[104]
movies.add("string")
[105]
movies
{'fb', 'hulk', 'iron', 'string'}
[106]
set1 = {"a", "b", "c"}
set2 = {"a", "c", "d", "e"}
[107]
set2.difference(set1)
{'d', 'e'}
[108]
set2.difference_update(set1)
[109]
set2
{'d', 'e'}
Tuples
Immutable
[110]
my_tuple = ("python", "ML", "AI")
[111]
my_tuple[0]
'python'
[112]
my_tuple[0] = 'Learn'
---------------------------------------------------------------------------
TypeError Traceback (most recent call last)
<ipython-input-112-bfd518f498ae> in <module> ----> 1 my_tuple[0] = 'Learn'
TypeError: 'tuple' object does not support item assignment
[115]
## in-built functions
my_tuple.index('python')
0
Dictionaries
Sequences in key-value pairs
Mutable
Iterable
[117]
dict={}
[118]
expenses = {"books": 400, "cars": 300, "Internet": "Airtel"}
[124]
expenses['misc']= 800
[126]
expenses
{'books': 400, 'cars': 300, 'Internet': 'Airtel', 'misc': 800}
[128]
d1 = {"city": "pune", "pin": 567890}
[129]
expenses.update(d1)
[131]
expenses
{'books': 400,
 'cars': 300,
 'Internet': 'Airtel',
 'misc': 800,
 'city': 'pune',
 'pin': 567890}
[133]
expenses['books']= 1990
expenses
{'books': 1990,
 'cars': 300,
 'Internet': 'Airtel',
 'misc': 800,
 'city': 'pune',
 'pin': 567890}
[127]
expenses['rent']
---------------------------------------------------------------------------
KeyError Traceback (most recent call last)
<ipython-input-127-fe532103dde8> in <module> ----> 1 expenses['rent']
KeyError: 'rent'
[119]
expenses['books']  ## accessing the item based on its key
400
[122]
expenses.items()
dict_items([('books', 400), ('cars', 300), ('Internet', 'Airtel')])
[134]
expenses.values()
dict_values([1990, 300, 'Airtel', 800, 'pune', 567890])
[123]
## Looping

for x in expenses.values():
    print(x)
400
300
Airtel


# In[ ]:





# In[ ]:


Conditional statements
If, else, elif
[1]
num = input("Enter a number: ")
num=int(num)

if num%2==0:
    print("Number {} is even".format(num))
else:
    print("Number {} is odd".format(num))
    
Enter a number: 8
Number 8 is even

###Comparison operators:

== equal to
< less than,
[21]
language = "Python"

if language=="Python":
    print("True")
else:
    print("No match")
True

[3]
language = input("Enter programming language: ")

if language=="Python":
    print("True")
elif language=='Java':
    print('Language is Java')
elif language=='React':
    print('Language is React')
else:
    print("No match")
Enter programming language: java
No match

1. Write a program to read 3 float numbers and print the largest value
[4]
### Write a program that takes the age of the dog as an input and calculates the equivalent age in human years???
[5]
age = int(input("Age of the dog: "))
print()

if age<0:
    print("This cannot be True")
elif age==0:
    print("Corresponds to zero human years")
elif age==1:
    print("Age is approx 14 human years")
else:
    human = 22+ (age-2) * 5
    print("Corresponds to "+ str(human) +" human years!!!")
Age of the dog: 1

Age is approx 14 human years

Loops:
For loop
while loop
[8]
## Store the monthly expenses in a list and find out the total expenses for all month

expenses= [2200, 2000, 4200, 3100, 2980]
total = expenses[0]+ expenses[1]+ expenses[2]+ expenses[3]+ expenses[4]
total
14480
[11]
sum(expenses)
14480
[9]
total=0

for i in expenses:
    total=total+i
print(total)
14480

[12]
expenses= [2200, 2000, 4200, 3100, 2980]
total = 0

for i in range(len(expenses)):
    print('Month: ', (i+1), 'Expenses: ', expenses[i])
    total = total+expenses[i]
print("Total expense: ", total)
Month:  1 Expenses:  2200
Month:  2 Expenses:  2000
Month:  3 Expenses:  4200
Month:  4 Expenses:  3100
Month:  5 Expenses:  2980
Total expense:  14480

[10]
###print 1 to 10 using range()

for i in range(1,11):
    print(i)
1
2
3
4
5
6
7
8
9
10

For loop and break statement:
[13]
key_location = "chair"
locations = ["hall", "living room", "chair", "park"]

for i in locations:
    if i==key_location:
        print("Key is found in ", i)
        break
    else:
        print("Key is NOT found in ", i)
Key is NOT found in  hall
Key is NOT found in  living room
Key is found in  chair

For loop and continue statement:
[17]
for i in range(1,11):
    if i%2==0:
        continue
    print(i)
1
3
5
7
9

[18]
for i in range(1,5):
    if i<=3:
        continue
    print(i)
4

while loop
takes only one condition
we have increment/decrement it with a counter
[23]
## to print 1 to 5
i = 5

while i>=1:
    print(i)
    i = i-1
5
4
3
2
1

Function
num = input("Enter a number: ")
num=int(num)

if num%2==0:
    print("Number {} is even".format(num))
else:
    print("Number {} is odd".format(num))
[24]
def even_or_odd(num):
    if num%2==0:
        print("Number {} is even".format(num))
    else:
        print("Number {} is odd".format(num))
[26]
even_or_odd(12)
Number 12 is even


# In[ ]:





# In[6]:


def name_of_function(arg1,arg2):
    '''
    This is where the function's Document String (doc-string) goes
    '''
    # Do stuff here
    #return desired result
[2]
def say_hello(name):
    print('hello', name)
    print('How do you do?')
[3]
say_hello('Aarthi')
hello Aarthi
get_ipython().set_next_input('How do you do');get_ipython().run_line_magic('pinfo', 'do')

[34]### print will print once but it will not store in variable but return will once execute then also work 
### Write a function to add any 3 numbers:   ###x,y = positional arguments, ##z= keyword argument

def sum(x,y,z=11):
    total = x+y+z
    return total
[35]
sum(56,78)
145
[6]
sum(5.4, 6.7, 8.9)
21.0
[7]
for i in [1,2,3,4]:
    print(i)
1
2
3
4

[25]
marks1 = [68,78,98,45,34]
marks2 = [77,67,57,88,76]

total = 0
for i in marks1:
    total=total+i
print("Total marks of 1st student:", total)

total = 0
for i in marks2:
    total=total+i
print("Total marks of 2nd student:", total)
Total marks of 1st student: 323
Total marks of 2nd student: 365

[26]
def calculate_total(marks):
    total=0
    for i in marks:
        total=total+i
    return total
[27]
sum_of_marks1 = calculate_total(marks1)
print("Total sum:", sum_of_marks1)
Total sum: 323

[28]
sum_of_marks2 = calculate_total(marks2)
print("Total sum:", sum_of_marks2)
Total sum: 365

[29]
## Absolute value:

def absolute_value(num):
    if num>=0:
        return num
    else:
        return -num
[31]
print(absolute_value(-5))
5

positional and keyword arguments
[36]
def hello(name, age=35):
    print("My name is {} and my age is {}".format(name, age))
[37]
hello('Aarthi')
My name is Aarthi and my age is 35

[39]
hello('Aarthi', 34)
My name is Aarthi and my age is 34

[40]
def hello(*args, **kwargs):
    print(args)
    print(kwargs)
[41]
hello("Laksh", "Ravi", age=23, dob=1977)
('Laksh', 'Ravi')
{'age': 23, 'dob': 1977}

[42]
names=['Laksh', 'Ravi']
dict_args={'age': 23, 'dob': 1977}
[44]
hello(names, dict_args)
(['Laksh', 'Ravi'], {'age': 23, 'dob': 1977})
{}

[56]
hello(*names, **dict_args)
('Laksh', 'Ravi')
{'age': 23, 'dob': 1977}

[62]
## Given a list, write a fn to calculate the sum of all even numbers and all odds numbers

lst=[12,44,56,33,56,7,8,56,22,97,25,6]

def even_odd_sum(lst):
    even_sum = 0
    odd_sum = 0
    
    for i in lst:
        if i%2==0:
            even_sum = even_sum+i
        else:
            odd_sum = odd_sum+i
    return even_sum, odd_sum

even_odd_sum(lst)
(260, 162)
Map function
[64]
def even_or_odd(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"
[65]
even_or_odd(45)
'Odd'
[66]
lst=[12,44,56,33,56,7,8,56,22,97,25,6]
[69]
list(map(even_or_odd, lst)) ### map(function, iterable)
['Even',
 'Even',
 'Even',
 'Odd',
 'Even',
 'Odd',
 'Even',
 'Even',
 'Even',
 'Odd',
 'Odd',
 'Even']
lambda function/ anonymous function
[70]
def add(a,b):
    sum = a+b
    return sum
[71]
add(2,3)
5
[72]
sum=lambda a,b:a+b   ###lambda input:operation
[73]
sum(10,70)
80
[74]
even=lambda n:n%2==0
[77]
even(9)
False
[78]
### add 2 lists using map and lambda

l1 = [1,2,3]
l2 = [7,8,9]

list(map(lambda x,y:x+y, l1,l2))
[8, 10, 12]
[80]
## create 2 function to add (add_num())and multiply 2 numbers

## marks=[70,80,77,86,99]
###write a function to cal the average marks.
###write a function to cal the grade of the students based on avg marks (if,elif,else)
[81]
### List comprehension

lst1=[]

def lst_sq(lst):
    for i in lst:
        lst1.append(i*i)
        
    return lst1
[82]
lst_sq([2,3,4])
[4, 9, 16]
[85]
lst = [2,3,4]
lst1= [i*4 for i in lst]
print(lst1)
[8, 12, 16]

[88]
lst2 =[i*i for i in lst if i%2!=0]
print(lst2)
[9]


# In[5]:


def hello(name):
    print('how are u')
    print('hey')
    print('total')
hello('aarti')


# In[ ]:


Encapsulation
input ----> [] ----> Output

[] = function???

Encapsulation is an another powerful way to extend a class which consists on wrapping an object with a second one. There are two main reasons to use encapsulation:

Composition
Dynamic Extension
1.1 Composition
The abstraction process relies on creating a simplified model that remove useless details from a concept. In order to be simplified, a model should be described in terms of other simpler concepts. For example, we can say that a car is composed by:

Tyres
Engine
Body
And break down each one of these elements in simpler parts until we reach primitive data.

[8]
class Tyres:
    def __init__(self, branch, belted_bias, opt_pressure):
        self.branch = branch
        self.belted_bias = belted_bias
        self.opt_pressure = opt_pressure
        
    def __str__(self):
        return ("Tyres: \n \tBranch: " + self.branch +
               "\n \tBelted-bias: " + str(self.belted_bias) + 
               "\n \tOptimal pressure: " + str(self.opt_pressure))
        
class Engine:
    def __init__(self, fuel_type, noise_level):
        self.fuel_type = fuel_type
        self.noise_level = noise_level
        
    def __str__(self):
        return ("Engine: \n \tFuel type: " + self.fuel_type +
                "\n \tNoise level:" + str(self.noise_level))
        
class Body:
    def __init__(self, size):
        self.size = size
        
    def __str__(self):
        return "Body:\n \tSize: " + self.size
        
class Car:
    def __init__(self, t, e, b):
        self.tyres = t
        self.engine = e
        self.body = b
        
    def tyrespec(self):
        return "self.tyre"
        
    def __str__(self):
        return str(self.tyres) + "\n" + str(self.engine) + "\n" + str(self.body)

[4]
car= Car('black', 'petrol', 'suv')
print(car)
black
petrol
suv

t = Tyres('Pirelli', True, 2.0) e = Engine('Diesel', 3) b = Body('Medium') c = Car(t, e, b) print(c)

1.2 Dynamic Extension
Sometimes it's necessary to model a concept that may be a subclass of another one, but it isn't possible to know which class should be its superclass until runtime.

Example
Suppose we want to model a simple dog school that trains instructors too. It will be nice to re-use Person and Student but students can be dogs or peoples. So we can remodel it this way:

[14]
class Dog:
    def __init__(self, name, year_of_birth, breed):
        self._name = name
        self._year_of_birth = year_of_birth
        self._breed = breed

    def __str__(self):
        return "%s is a %s breed born in the year %d." % (self._name, self._breed, self._year_of_birth)

papillon = Dog("Papillon", 1954, "Laika")
print(papillon)
Papillon is a Laika breed born in the year 1954.

[15]
class Student:
    def __init__(self, anagraphic, student_id):
        self._anagraphic = anagraphic
        self._student_id = student_id
    def __str__(self):
        return str(self._anagraphic) + " Student ID: %d" % self._student_id


alex_student = Student("dsfs",1)
papillon_student = Student(papillon, 2)

print(alex_student)
print(papillon_student)

dsfs Student ID: 1
Papillon is a Laika breed born in the year 1954. Student ID: 2

Assignment:
class - create 3 classes class1(a1,a2,a3),m1, class2(b1,b2,b3)m2, class3(c1,c2,c3)m3 then, create an obj for 3 classes (c1,c2,c3), create a 4th class4(d1,d2,d3),m4


# In[ ]:





# In[ ]:


day5


# In[ ]:


lst = [1,2,3,4,5,6,7]
for i in lst:
    print(i)
1
2
3
4
5
6
7

[16]
lst1=iter(lst)
lst1   ### Memory has not been initialized here
<list_iterator at 0x1440f5b6c10>
[17]
next(lst1)  ### elements in the list are initialized one at a time - next()
1
String Formatting
[18]
print("Hello world")
Hello world

[19]
def greet(name):
    return "Hello {}, welcome!".format(name)
[20]
greet('Arya')
'Hello Arya, welcome!'
[21]
def welcome_email(name, age):
    return "My name is {} and I am {} yrs old".format(name, age)
[22]
welcome_email('Aarthi', 35)
'My name is Aarthi and I am 35 yrs old'
[25]
def welcome_email(name, age):
    return "My name is {name} and I am {years} yrs old".format(years=age,name=name)
[26]
welcome_email('Prem', 34)
'My name is Prem and I am 34 yrs old'
Class in python
Class - Has 2 entities: properties, methods class - Abstraction of some entities that contain common set of properties (attributes) and methods (activities in real world)

Object - specific instance of a class

behavior varies, gender varies, occupation varies
class Human:
    def __init__(self):
        self.name=""
        self.occupation=""
## properties of the class "human"
[28]
class Human:
    def __init__(self, n, o):
        self.name= n
        self.occupation= o
    def our_work(self):
        if self.occupation=="badminton":
            print(self.name, "plays badminton")
        elif self.occupation=="artist":
            print(self.name,"acts in movies")
    def speaks(self):
        print(self.name, "says how are you?")
[31]
##create an instance

tom = Human("Tom", "artist")
tom.our_work()
Tom acts in movies

[32]
tom.speaks()
get_ipython().set_next_input('Tom says how are you');get_ipython().run_line_magic('pinfo', 'you')

[33]
class car:
    pass
[37]
car1 = car()  ###obj/instance called car1
car1.windows = 5
car1.doors = 4
[38]
print(car1.windows)
5

[41]
car2=car()
car2.windows = 6
car2.enginetype="petrol"
[45]
class car:
    def __init__(self, windows, doors, enginetype):
        self.windows = windows
        self.door=doors
        self.enginetype = enginetype
[46]
car1=car(4,5,"Diesel")
[44]
print(car1.enginetype)
Diesel

[47]
dir(car1)
['__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 'door',
 'enginetype',
 'windows']
Modules in python
[48]
import math
[49]
math.sqrt(25)
5.0
[50]
math.pow(2,3)
8.0
[51]
math.pi
3.141592653589793
[53]
math.log10(1000)
3.0
[55]
import calendar as cal
[59]
c = cal.month(2021,10)
print(c)
    October 2021
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31


[60]
cal.isleap(2021)
False


# In[ ]:


class human
    def __init__(self,height,weight):
        self.height=1
        self.weight="h"
    def ourclass(self):
        


# In[ ]:


class Human:
    def __init__(self, n, o):
        self.name= n
        self.occupation= o
    def our_work(self):
        if self.occupation=="badminton":
            print(self.name, "plays badminton")
        elif self.occupation=="artist":
            print(self.name,"acts in movies")
    def speaks(self):
        print(self.name, "says how are you?")


# In[ ]:


class 6


# In[ ]:


Exception Handling
Exception : Error detected at the time of program execution

Reason for handling exceptions:

Program never crashes
We can give the right statement to the user
[9]
a=20
b=0
[10]
c=a/b
print(c)
---------------------------------------------------------------------------
ZeroDivisionError Traceback (most recent call last)
<ipython-input-10-5224659fe8a5> in <module> ----> 1 c=a/b 2 print(c)
ZeroDivisionError: division by zero
[13]
a=10
[15]
a=c
---------------------------------------------------------------------------
NameError Traceback (most recent call last)
<ipython-input-15-eb70dc206e9a> in <module> ----> 1 a=c
NameError: name 'c' is not defined
try-else
[16]
try:
    a=c
except NameError as ex1:
    print("The variable c was not defined")
except Exception as ex:
    print(ex)
The variable c was not defined

[18]
x= 23
y= "s"
z=x+y
---------------------------------------------------------------------------
TypeError Traceback (most recent call last)
<ipython-input-18-06a871036fb4> in <module> 1 x= 23 2 y= "s" ----> 3 z=x+y
TypeError: unsupported operand type(s) for +: 'int' and 'str'
[20]
try:
    x= 23
    y= "s"
    z=x+y
except TypeError as ex1:
    print("The datatypes are not similar")
except NameError as ex1:
    print("The variable c was not defined")
except Exception as ex:
    print(ex)
The datatypes are not similar

[22]
a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))

c=a+b
d=a/b
e=a*b
print(c)
print(d)
print(e)
Enter the 1st number: 12
Enter the 2nd number: 0

---------------------------------------------------------------------------
ZeroDivisionError Traceback (most recent call last)
<ipython-input-22-6c08e4f4c1d7> in <module> 3 4 c=a+b ----> 5 d=a/b 6 e=a*b 7 print(c)
ZeroDivisionError: division by zero
try:
    a = int(input("Enter the 1st number: "))
    b = int(input("Enter the 2nd number: "))

    c=a+b
    d=a/b
    e=a*b
except ZeroDivisionError:
    print("Enter a number greater than 0")
except Exception as ex:  ###generic exception should be added at the end
    print(ex)
[26]
try:
    a = int(input("Enter the 1st number: "))
    b = int(input("Enter the 2nd number: "))

    c=a/b
except TypeError as ex1:
    print("The datatypes are not similar")
except NameError as ex1:
    print("The variable was not defined")
except ZeroDivisionError:
    print("Enter a number greater than 0")
except Exception as ex:
    print(ex)
    
else:
    print(c)
Enter the 1st number: 12
Enter the 2nd number: s
invalid literal for int() with base 10: 's'

try-else-finally
try:
    a = int(input("Enter the 1st number: "))
    b = int(input("Enter the 2nd number: "))

    c=a/b
except TypeError:
    print("The datatypes are not similar")
except NameError:
    print("The variable was not defined")
except ZeroDivisionError:
    print("Enter a number greater than 0")
except Exception as ex:
    print(ex)
    
else:
    print(c)
finally:
    print("The execution is complete")   ###Used to close any db connection
## Create your own custom exception

class Error(Exception):
    """ This exception was created to handle"""
    pass

class dobException(Error):
    pass

class cutoffException(Error):
    pass

yr_input = int(input("Enter the year of birth "))
age = 2021-yr_input

try:
    if age<=28 and age>20:
        print("You are eligible to apply for the exam")
    else:
        raise dobException
except dobException:
    print("You are not eligible to apply for the exam")
score = int(input("Enter the exam score "))
cut_off = 85

try: 
    if score>=cut_off:
        print("Pass")
    else:
        raise cutoffException
except cutoffException:
    print("Re-attempt")
write a function that converts a temperature from degrees Kelvin to degrees Fahrenheit. Since zero degrees Kelvin is as cold as it gets, the function bails out if it sees a negative temperature.

Write a exception in this case


# In[ ]:


day7


# In[ ]:


Inheritance
When a child class (***Derived class) inherits the properties of a parent class (***Base class)

class Parent: def function1(self): print("This is a parent function")

class Child(Parent): def function2(self): print("This is a child function")

c = Child()
c.function1()
This is a parent function

c.function2()
This is a child function

class Animals:   ###Parent class
    def eat(self):
        print('I can eat')
        
class Cat(Animals):  ### Child class
    def grumpy(self):
        print('I am grumpy')
class Dog(Animals):
    def bark(self):
        print('I bark')
dog1=Dog()
dog1.eat()
I can eat

dog1.bark()
I bark

cat1=Cat()
cat1.eat()
I can eat

init function: (Initialization constructor)

Init function is called automatically everytime the class is used to create a object

class Polygon:
    def __init__(self, sides):
        self.sides = sides    #### public variables
    def display_info(self):
        print("A polygon is a 2-D with straight lines")
    def get_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter
    

class triangle(Polygon):
    def display_info(self):
        print("A triangle has 3-sides")

class quadrilateral(Polygon):
    def display_info(self):
        print("A quadrilateral has 4-sides")
t=triangle([5,6,8])
perimeter=t.get_perimeter()
print("The perimeter of the triangle is", perimeter)
The perimeter of the triangle is 19

method overriding
It can be achieved to change the functionality of parent class function

t.display_info()  ## method overriding
A triangle has 3-sides

Types of Inheritance:

Single - Involves 1 child class and 1 parent class

Multiple - Involves more than 1 parent class

Multi-level - child class acts as a parent class for another child class

Hierarchical- More than 2 derived classes from a single base class

Hybrid - More than 1 type of inheritance

class Parent:
    def fn1(self):
        print('This is function1')

class Parent2(Parent):
    def fn3(self):
        print('This is function3')

class Parent3(Parent):
    def fn4(self):
        print('This is function4')
        
class Child(Parent2):
    def fn2(self):
        print('This is function2')
ob=Child()
ob.fn3()
This is function3

class Car:
    def __init__(self, windows, doors, engine):
        self.windows = windows  ### self._windows- protected variable,
        self.doors = doors      ### self.__windows- private variable,
        self.engine = engine    ## self.windows = windows== public variable
    def drive(self):
        print('I love driving')
        
class audi(Car):
    def __init__(self, windows, doors, engine, voice):
        self.voice = voice
    def selfdriving(self):
        print('Audi supports self-driving')
    
a7=audi(4,5,'diesel',True)
a7.drive()
I love driving

car1=Car(2, 3, 'petrol')
car1.engine
'petrol'
Try this:

Create a parent class called 'person' and define with attributes like name, empid...create a child class called 'employee' with added features like designation, salary etc...create a object variable for the child class and call any of the function defined under parent class 'person'


# In[ ]:


day8


# In[ ]:


Multiple Inheritance
[2]
## Parent class
class A:
    def method1(self):
        print("A class method")
[3]
### derived classes of A
class B(A):
    def method2(self):
        print("B class method")
[4]
class C(A):
    def method3(self):
        print("C class method")
[5]
class D(B,C):
    def method4(self):
        print("D class method")
[6]
d=D()
[12]
d.method1()
A class method

[13]
class A:
    def method1(self):
        print("A class method")
[15]
### derived classes of A
class B(A):
    def method1(self):
        print("B class method")
class C(A):
    def method1(self):
        print("C class method")
[24]
class D(B,C):
    def method1(self):
        print("D class method")
        C.method1(self)
        B.method1(self)
        A.method1(self)
        
[25]
d=D()
[26]
d.method1()
D class method
C class method
B class method
A class method

[20]
C.method1(d)
C class method

[22]
A.method1(d)
A class method

Public, Protected and Private class variables - Access modifiers
self.name = Public class variable
self._name = Protected class variable
self.__name = Private variables
[27]
## All the class variables are public:

class Letsupgrade:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def displayAge(self):
        print("The age is", self.age)   
[36]
obj = Letsupgrade("Ram", 20)
[37]
dir(obj)
['__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 'age',
 'displayAge',
 'name']
[29]
obj.displayAge()
The age is 20

[31]
obj.age
20
[32]
obj.age = 21
[33]
obj.age
21
[39]
### Protected access modifiers

class LU:
    def __init__(self, name, age, roll):
        self._name = name
        self._age = age
        self._roll = roll

class batch(LU):
    def __init__(self, name, age, roll, rank):
        super().__init__(name, age, roll)
        self.rank = rank
       
[40]
b = batch("Sam", 20, 1801, 3)
[42]
b._age
20
[43]
b._age=31
[44]
b._age
31
[41]
dir(b)
['__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 '_age',
 '_name',
 '_roll',
 'rank']
[35]
s = LU("Ram", 23, 1701)
[38]
dir(s)
['__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 '_age',
 '_name',
 '_roll']
[45]
### Private access modifiers

class LU:
    def __init__(self, name, age, roll):
        self.__name = name
        self.__age = age
        self.__roll = roll
[46]
s=LU("Mia", 24, 1898)
[49]
s._LU__age=28
[50]
s._LU__age
28
[47]
dir(s)
['_LU__age',
 '_LU__name',
 '_LU__roll',
 '__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__']
[109]
## Iterable

lst = [2,3,4,5,6,7,8,9]
for i in lst:
    print(i)
2
3
4
5
6
7
8
9

[110]
iter(lst)  ## iterator using iter()
<list_iterator at 0x2a7811fe610>
[111]
iterable = iter(lst)  ### We can iterate through an iterator
[115]
rev=reversed(lst)
print(rev)
<list_reverseiterator object at 0x000002A781CB8B20>

[118]
next(rev)
8
[72]
next(iterable)
2
[80]
try:
    print(next(iterable))
except StopIteration:
    print("The list is empty")
The list is empty

[81]
## Python generator
[84]
def cube(n):
    for i in range(n):
        return i**3
[86]
cube(4)
0
return - function returns a value and it destroys all its local variable
yield - preserves the state of the previous execution
[87]
## Generator
def cube(n):
    for i in range(n):
        yield i**3
[88]
cube(4)
<generator object cube at 0x000002A781CCCC10>
[99]
for i in  cube(4):
    print(i)
0
1
8
27

[100]
x=cube(4)
[101]
x
<generator object cube at 0x000002A781762D60>
[102]
next(x)  ###Using a generator, we can create an iterator!
0
[105]
### create a fibonacci sequence using a generator

def fib():
    x,y=0,1
    while True:
        yield x
        x,y = y,x+y
for i in fib():
    if i>50:
        break
    print(i)
0
1
1
2
3
5
8
13
21
34

[106]
## create a generator that can reverse a string
[119]
def rev_str(my_str):
    length = len(my_str)
    for i in range(length-1, -1,-1):
        yield my_str[i]
[124]
for i in rev_str("letsupgrade"):
    print(i)
e
d
a
r
g
p
u
s
t
e
l

[126]
lst = [2,5,7,8,9]

##list comprehension
lst1 = [x**2 for x in lst]
lst1
[4, 25, 49, 64, 81]
[134]
##using a generator expression using ()
gen=(x**2 for x in lst)
print(gen)
<generator object <genexpr> at 0x000002A7819004A0>

[135]
next(gen)
4
Create a generator to find out the sum of squares of numbers in fibonacci seq


# In[ ]:


Day 9


# In[ ]:


Decorators in python (OOPS)
A decorator takes in a function, adds some functionality and returns it.

Decorators are very powerful and useful tool in Python since it allows programmers to modify the behaviour of function or class. Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it.

[1]
## function copy
[2]
def welcome():
    print("Welcome to my class")
[4]
s=welcome()
Welcome to my class

[6]
print(s)
None

[7]
def welcome():
    return "Welcome to my class"
[8]
s=welcome()
[9]
s
'Welcome to my class'
[10]
del welcome
[11]
s
'Welcome to my class'
[12]
welcome()
---------------------------------------------------------------------------
NameError Traceback (most recent call last)
<ipython-input-12-a401d7101853> in <module> ----> 1 welcome()
NameError: name 'welcome' is not defined
[13]
def school():
    return "VKV"
[15]
batch = school()
batch
'VKV'
[16]
del school
[17]
batch
'VKV'
Closure: A function within a function
We can provide input in the main function and when we are defining the inner function, we can use the variable i.e availale in the main func...

[20]
def main_message():
    message = "Hello all"
    def sub_message():
        print("Welcome to my class")
        print(message)
        print("Learn everyday")
    return sub_message()
[21]
main_message()
Welcome to my class
Hello all
Learn everyday

[22]
def main_message(message):
    def sub_message():
        print("Welcome to my class")
        print(message)
        print("Learn everyday")
    return sub_message()
[23]
main_message("Motivate yourself")
Welcome to my class
Motivate yourself
Learn everyday

[30]
def main_message(function):
    def sub_message():
        print("Welcome to my class")
        function("ABC")
        print("Learn everyday")
    return sub_message()
[31]
main_message(print)
Welcome to my class
ABC
Learn everyday

[33]
def main_message(function):
    def sub_message():
        print("Welcome to my class")
        print(function("ABC"))
        print("Learn everyday")
    return sub_message()
[34]
main_message(len)
Welcome to my class
3
Learn everyday

[35]
def main_message(function):
    def sub_message():
        print("Welcome to my class")
        print(function([2,3,4,5,6,7]))
        print("Learn everyday")
    return sub_message()
[37]
main_message(len)   #### closure wrt in-built functions - function can be called inside the sub-function
Welcome to my class
6
Learn everyday

decorator
[38]
def main_message(function):
    def sub_message():
        print("Welcome to my class")
        function()
        print("Learn everyday")
    return sub_message()
[42]
def class_name():
    print("This is Python batch 6") 
[44]
main_message(class_name)   ####this is a decorator - pass a func as a parameter
Welcome to my class
This is Python batch 6
Learn everyday

[45]
def main_message(function):
    def sub_message():
        print("Welcome to my class")
        function()
        print("Learn everyday")
    return sub_message()
@main_message   ##### define a decorator 
def class_name():
    print("This is Python batch 6") 
Assert statement
used only in logical expressions
Used to check if a logical exp is T or F
as a part exception handling too
[47]
5>10
False
[48]
n=5
[54]
assert n>5
---------------------------------------------------------------------------
AssertionError Traceback (most recent call last)
<ipython-input-54-35cd90740f5c> in <module> ----> 1 assert n>5
AssertionError:
[58]
try:
    num=int(input("Enter any number"))
    assert num%2==0
    print("Number is Even")
except AssertionError:
    print("Enter a even num")
Enter any number21
Enter a even num

IS and == (comparison operator)
[59]
lst_1=["A", "B", "C"]
lst_2=["A", "B", "C"]
[60]
lst_1==lst_2
True
[61]
a="Python"
b="Python"
a==b
True
[62]
lst_1=["A", "B", "C"]
lst_2=lst_1
[63]
lst_1 is lst_2
True
[65]
lst_2[1]="Z"
[66]
lst_2
['A', 'Z', 'C']
[67]
lst_1
['A', 'Z', 'C']
[70]
lst_1=lst_2
[71]
lst_2[0]=100
[74]
lst_1, lst_2
([100, 'Z', 'C'], [100, 'Z', 'C'])
[79]
lst_1=[1,2,3,4]
lst_2=lst_1.copy()   #### Shallow copy using copy()
[76]
lst_2, lst_1
([1, 2, 3, 4], [1, 2, 3, 4])
[77]
lst_2[0]=100
[78]
lst_2, lst_1
([100, 2, 3, 4], [1, 2, 3, 4])
[81]
lst1=[[1,2,3,4],[20,30,40,50]]
lst2=lst1.copy()
[82]
lst1, lst2
([[1, 2, 3, 4], [20, 30, 40, 50]], [[1, 2, 3, 4], [20, 30, 40, 50]])
[84]
lst1[1][0]=5000
[85]
lst1
[[1, 2, 3, 4], [5000, 30, 40, 50]]
[86]
lst2
[[1, 2, 3, 4], [5000, 30, 40, 50]]
[90]
### Deep copy 

import copy
[91]
lst1=[1,2,3,4]
lst2=copy.deepcopy(lst1)
[94]
lst2[0]=90
[95]
lst2
[90, 2, 3, 4]
[97]
lst1  #### Here shallow copy=deep copy in a single list
[1, 2, 3, 4]
[98]
lst1=[[1,2,3], [3,4,5], [4,5,6]]
lst2=copy.deepcopy(lst1)
[99]
lst2
[[1, 2, 3], [3, 4, 5], [4, 5, 6]]
[102]
lst1[1][1]=700
[103]
lst1
[[1, 2, 3], [3, 700, 5], [4, 5, 6]]
[104]
lst2
[[1, 2, 3], [3, 4, 5], [4, 5, 6]]
### Global variables = Not defined inside any func, accessible 
### Local variable = Defined inside a function, access only within, __init__


# In[ ]:


Day10


# In[ ]:


Encapsulation
input ----> [] ----> Output

[] = function???

Encapsulation is an another powerful way to extend a class which consists on wrapping an object with a second one. There are two main reasons to use encapsulation:

Composition
Dynamic Extension
1.1 Composition
The abstraction process relies on creating a simplified model that remove useless details from a concept. In order to be simplified, a model should be described in terms of other simpler concepts. For example, we can say that a car is composed by:

Tyres
Engine
Body
And break down each one of these elements in simpler parts until we reach primitive data.

[8]
class Tyres:
    def __init__(self, branch, belted_bias, opt_pressure):
        self.branch = branch
        self.belted_bias = belted_bias
        self.opt_pressure = opt_pressure
        
    def __str__(self):
        return ("Tyres: \n \tBranch: " + self.branch +
               "\n \tBelted-bias: " + str(self.belted_bias) + 
               "\n \tOptimal pressure: " + str(self.opt_pressure))
        
class Engine:
    def __init__(self, fuel_type, noise_level):
        self.fuel_type = fuel_type
        self.noise_level = noise_level
        
    def __str__(self):
        return ("Engine: \n \tFuel type: " + self.fuel_type +
                "\n \tNoise level:" + str(self.noise_level))
        
class Body:
    def __init__(self, size):
        self.size = size
        
    def __str__(self):
        return "Body:\n \tSize: " + self.size
        
class Car:
    def __init__(self, t, e, b):
        self.tyres = t
        self.engine = e
        self.body = b
        
    def tyrespec(self):
        return "self.tyre"
        
    def __str__(self):
        return str(self.tyres) + "\n" + str(self.engine) + "\n" + str(self.body)

[4]
car= Car('black', 'petrol', 'suv')
print(car)
black
petrol
suv

t = Tyres('Pirelli', True, 2.0) e = Engine('Diesel', 3) b = Body('Medium') c = Car(t, e, b) print(c)

1.2 Dynamic Extension
Sometimes it's necessary to model a concept that may be a subclass of another one, but it isn't possible to know which class should be its superclass until runtime.

Example
Suppose we want to model a simple dog school that trains instructors too. It will be nice to re-use Person and Student but students can be dogs or peoples. So we can remodel it this way:

[14]
class Dog:
    def __init__(self, name, year_of_birth, breed):
        self._name = name
        self._year_of_birth = year_of_birth
        self._breed = breed

    def __str__(self):
        return "%s is a %s breed born in the year %d." % (self._name, self._breed, self._year_of_birth)

papillon = Dog("Papillon", 1954, "Laika")
print(papillon)
Papillon is a Laika breed born in the year 1954.

[15]
class Student:
    def __init__(self, anagraphic, student_id):
        self._anagraphic = anagraphic
        self._student_id = student_id
    def __str__(self):
        return str(self._anagraphic) + " Student ID: %d" % self._student_id


alex_student = Student("dsfs",1)
papillon_student = Student(papillon, 2)

print(alex_student)
print(papillon_student)

dsfs Student ID: 1
Papillon is a Laika breed born in the year 1954. Student ID: 2

Assignment:
class - create 3 classes class1(a1,a2,a3),m1, class2(b1,b2,b3)m2, class3(c1,c2,c3)m3 then, create an obj for 3 classes (c1,c2,c3), create a 4th class4(d1,d2,d3),m4


# In[ ]:





# In[ ]:


day 10


# In[ ]:


Encapsulation
input ----> [] ----> Output

[] = function???

Encapsulation is an another powerful way to extend a class which consists on wrapping an object with a second one. There are two main reasons to use encapsulation:

Composition
Dynamic Extension
1.1 Composition
The abstraction process relies on creating a simplified model that remove useless details from a concept. In order to be simplified, a model should be described in terms of other simpler concepts. For example, we can say that a car is composed by:

Tyres
Engine
Body
And break down each one of these elements in simpler parts until we reach primitive data.

[8]
class Tyres:
    def __init__(self, branch, belted_bias, opt_pressure):
        self.branch = branch
        self.belted_bias = belted_bias
        self.opt_pressure = opt_pressure
        
    def __str__(self):
        return ("Tyres: \n \tBranch: " + self.branch +
               "\n \tBelted-bias: " + str(self.belted_bias) + 
               "\n \tOptimal pressure: " + str(self.opt_pressure))
        
class Engine:
    def __init__(self, fuel_type, noise_level):
        self.fuel_type = fuel_type
        self.noise_level = noise_level
        
    def __str__(self):
        return ("Engine: \n \tFuel type: " + self.fuel_type +
                "\n \tNoise level:" + str(self.noise_level))
        
class Body:
    def __init__(self, size):
        self.size = size
        
    def __str__(self):
        return "Body:\n \tSize: " + self.size
        
class Car:
    def __init__(self, t, e, b):
        self.tyres = t
        self.engine = e
        self.body = b
        
    def tyrespec(self):
        return "self.tyre"
        
    def __str__(self):
        return str(self.tyres) + "\n" + str(self.engine) + "\n" + str(self.body)

[4]
car= Car('black', 'petrol', 'suv')
print(car)
black
petrol
suv

t = Tyres('Pirelli', True, 2.0) e = Engine('Diesel', 3) b = Body('Medium') c = Car(t, e, b) print(c)

1.2 Dynamic Extension
Sometimes it's necessary to model a concept that may be a subclass of another one, but it isn't possible to know which class should be its superclass until runtime.

Example
Suppose we want to model a simple dog school that trains instructors too. It will be nice to re-use Person and Student but students can be dogs or peoples. So we can remodel it this way:

[14]
class Dog:
    def __init__(self, name, year_of_birth, breed):
        self._name = name
        self._year_of_birth = year_of_birth
        self._breed = breed

    def __str__(self):
        return "%s is a %s breed born in the year %d." % (self._name, self._breed, self._year_of_birth)

papillon = Dog("Papillon", 1954, "Laika")
print(papillon)
Papillon is a Laika breed born in the year 1954.

[15]
class Student:
    def __init__(self, anagraphic, student_id):
        self._anagraphic = anagraphic
        self._student_id = student_id
    def __str__(self):
        return str(self._anagraphic) + " Student ID: %d" % self._student_id


alex_student = Student("dsfs",1)
papillon_student = Student(papillon, 2)

print(alex_student)
print(papillon_student)

dsfs Student ID: 1
Papillon is a Laika breed born in the year 1954. Student ID: 2

Assignment:
class - create 3 classes class1(a1,a2,a3),m1, class2(b1,b2,b3)m2, class3(c1,c2,c3)m3 then, create an obj for 3 classes (c1,c2,c3), create a 4th class4(d1,d2,d3),m4


# In[ ]:


Day11


# In[1]:


### list less memory NUMPY MORE MEMORY
Numpy
[2]
import numpy as np
[4]
a=np.array([1,2,3])
print(a)  ###1-d array
[1 2 3]

[11]
a.shape
(3,)
[12]
a.ndim  ###get the dimension
1
[17]
a.size  ##total number of elements
3
[20]
a.dtype
dtype('int32')
[19]
a.itemsize
4
[5]
type(a)
numpy.ndarray
[9]
b=np.array([[2,3,4],[4,5,6]])
print(b)  ### 2-d array
[[2 3 4]
 [4 5 6]]

[10]
b.shape  ##(rows, columns)
(2, 3)
[13]
b.ndim
2
[14]
b.dtype  #### int32= 4 bytes (1byte=8bits)
dtype('int32')
[15]
b=np.array([[2,3,4],[4,5,6]], dtype="int16")
print(b)  ### 2-d array
[[2 3 4]
 [4 5 6]]

[16]
b.dtype
dtype('int16')
[18]
b.size
6
[21]
b.itemsize  ###equiv no. of bytes 
2
Access/change specific rows and columns [row,column], startindex:endindex
[44]
a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)   
[[ 1  2  3  4  5  6  7]
 [ 8  9 10 11 12 13 14]]

[86]
a[0,1:6:2]    ####Important!!! ####Important!!! ####Important!!! ####Important!!!
array([2, 4, 6])
[87]
a[0,1:-1:2]
array([2, 4, 6])
[88]
a[0,3]
4
[89]
a.shape
(2, 7)
[90]
a[0,5]
6
[91]
a[:,2]
array([ 3, 10])
[92]
a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)
[[ 1  2  3  4  5  6  7]
 [ 8  9 10 11 12 13 14]]

[93]
a[1,5]=22
[94]
a
array([[ 1,  2,  3,  4,  5,  6,  7],
       [ 8,  9, 10, 11, 12, 22, 14]])
[95]
a[:,2]=5
a
array([[ 1,  2,  5,  4,  5,  6,  7],
       [ 8,  9,  5, 11, 12, 22, 14]])
[96]
a[:,2]=9,10
a
array([[ 1,  2,  9,  4,  5,  6,  7],
       [ 8,  9, 10, 11, 12, 22, 14]])
Initializing different types of array
[97]
## All zeros matrix

np.zeros(5) ## vector 
array([0., 0., 0., 0., 0.])
[98]
np.zeros((2,3))  ## 2-d matrix
array([[0., 0., 0.],
       [0., 0., 0.]])
[99]
np.zeros((2,3,4))
array([[[0., 0., 0., 0.],
        [0., 0., 0., 0.],
        [0., 0., 0., 0.]],

       [[0., 0., 0., 0.],
        [0., 0., 0., 0.],
        [0., 0., 0., 0.]]])
[100]
## All ones matrix

np.ones((4,3))
array([[1., 1., 1.],
       [1., 1., 1.],
       [1., 1., 1.],
       [1., 1., 1.]])
[101]
np.full((3,3,2), 109)
array([[[109, 109],
        [109, 109],
        [109, 109]],

       [[109, 109],
        [109, 109],
        [109, 109]],

       [[109, 109],
        [109, 109],
        [109, 109]]])
[102]
c = np.full_like(a,6)
print(c)
[[6 6 6 6 6 6 6]
 [6 6 6 6 6 6 6]]

[103]
c.shape
(2, 7)
[104]
c.reshape(7,2)
array([[6, 6],
       [6, 6],
       [6, 6],
       [6, 6],
       [6, 6],
       [6, 6],
       [6, 6]])
[105]
### Initialize a matrix of random numbers

np.random.rand(4,3)   ####Important!!!
array([[0.13053884, 0.72429221, 0.53334079],
       [0.55123812, 0.66241585, 0.15933155],
       [0.09759562, 0.52388649, 0.50356599],
       [0.97233964, 0.99720478, 0.42731397]])
[106]
np.random.random_sample(a.shape)
array([[0.92745177, 0.87219667, 0.54875854, 0.48337739, 0.66032712,
        0.09056309, 0.3654313 ],
       [0.52346551, 0.0900956 , 0.11125731, 0.8666918 , 0.3501635 ,
        0.55702811, 0.73370433]])
[107]
### Random integer values

np.random.randint(6, size=(3,3))   ####Important!!!
array([[1, 3, 3],
       [3, 2, 2],
       [4, 3, 4]])
[108]
np.random.randint(-8,8, size=(4,3))
array([[-8, -5,  4],
       [-5, -3, -7],
       [ 2, -6, -7],
       [-8,  3,  1]])
[109]
## Identity matrix
[110]
np.identity(3)  ### square matrix    ####Important!!!
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])
[111]
np.identity(5)  ### square matrix
array([[1., 0., 0., 0., 0.],
       [0., 1., 0., 0., 0.],
       [0., 0., 1., 0., 0.],
       [0., 0., 0., 1., 0.],
       [0., 0., 0., 0., 1.]])
[112]
### repeat an array
[117]
arr=np.array([[1,2,3]])
arr1=np.repeat(arr,3, axis=0)
print(arr1)
[[1 2 3]
 [1 2 3]
 [1 2 3]]

[118]
a=np.array([1,2,3])
b=a
b
array([1, 2, 3])
[121]
b[0]=900
b
array([900,   2,   3])
[122]
a
array([900,   2,   3])
[124]
a=np.array([1,2,3])
b=a.copy()
b[0]=900
b
array([900,   2,   3])
[125]
a
array([1, 2, 3])
[134]
a=np.array([1,2,3,4])
print(a)
[1 2 3 4]

[135]
a/2
array([0.5, 1. , 1.5, 2. ])
[136]
a
array([1, 2, 3, 4])
[137]
a+=2
a
array([3, 4, 5, 6])
[138]
b=np.array([3,0,4,0])
[140]
a+b
array([6, 4, 9, 6])
[141]
a**b
array([ 27,   1, 625,   1], dtype=int32)
[142]
a
array([3, 4, 5, 6])
[143]
np.sin(a)
array([ 0.14112001, -0.7568025 , -0.95892427, -0.2794155 ])
[144]
np.cos(a)
array([-0.9899925 , -0.65364362,  0.28366219,  0.96017029])
##Linear algebra using np


# In[ ]:


LIST        NUMPY

SLOW         fast
more memory    less memory
insert, delete, concadinate, append function are similar


# In[ ]:


day 12


# In[ ]:


##List
n=[6,7,8,9]
[4]
n[1:3]  ### [start_index: end_index]
[7, 8]
[5]
n[-1]
9
[6]
import numpy as np
[7]
a=np.array([6,7,8])
[8]
a[0:2]
array([6, 7])
[9]
a[-1]
8
[11]
a=np.array([[6,7,8],[1,2,3],[7,8,9]])
a
array([[6, 7, 8],
       [1, 2, 3],
       [7, 8, 9]])
[17]
a[2,:]
array([7, 8, 9])
[16]
a[:,1:3]
array([[7, 8],
       [2, 3],
       [8, 9]])
[14]
a[2,0:2]
array([7, 8])
[12]
a[1,2]
3
[13]
a[0:2,2]
array([8, 3])
[18]
### Iterate through an array

a=np.array([[6,7,8],[1,2,3],[7,8,9]])
a
array([[6, 7, 8],
       [1, 2, 3],
       [7, 8, 9]])
[19]
for row in a:
    print(row)
[6 7 8]
[1 2 3]
[7 8 9]

[21]
## flattening this 2d array into a 1-D array
for cell in a.flat:
    print(cell)
6
7
8
1
2
3
7
8
9

[23]
#### Stacking through arrays together
a=np.arange(6).reshape(3,2)
a
array([[0, 1],
       [2, 3],
       [4, 5]])
[26]
b=np.arange(6,12).reshape(3,2)
b
array([[ 6,  7],
       [ 8,  9],
       [10, 11]])
[27]
## vertical stack of a over b
np.vstack((a,b))
array([[ 0,  1],
       [ 2,  3],
       [ 4,  5],
       [ 6,  7],
       [ 8,  9],
       [10, 11]])
[28]
## horizontal stack, side-ways
np.hstack((a,b))
array([[ 0,  1,  6,  7],
       [ 2,  3,  8,  9],
       [ 4,  5, 10, 11]])
[29]
## Horizontal split
a=np.arange(30).reshape(2,15)
a
array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]])
[32]
np.hsplit(a,5)
[array([[ 0,  1,  2],
        [15, 16, 17]]),
 array([[ 3,  4,  5],
        [18, 19, 20]]),
 array([[ 6,  7,  8],
        [21, 22, 23]]),
 array([[ 9, 10, 11],
        [24, 25, 26]]),
 array([[12, 13, 14],
        [27, 28, 29]])]
[35]
v=np.vsplit(a,2)
[36]
v[0]
array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14]])
[37]
v[1]
array([[15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]])
[38]
### Indexing with boolean arrays
[39]
a=np.arange(12).reshape(3,4)
a
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
[41]
b=a>4
b
array([[False, False, False, False],
       [False,  True,  True,  True],
       [ True,  True,  True,  True]])
[42]
a[b]
array([ 5,  6,  7,  8,  9, 10, 11])
[43]
a[b]=-1
a
array([[ 0,  1,  2,  3],
       [ 4, -1, -1, -1],
       [-1, -1, -1, -1]])
[44]
a=np.arange(12).reshape(3,4)
a
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
[46]
for x in np.nditer(a,order='F'):
    print(x)
0
4
8
1
5
9
2
6
10
3
7
11

[47]
for x in np.nditer(a,order='F', flags=['external_loop']):
    print(x)
[0 4 8]
[1 5 9]
[ 2  6 10]
[ 3  7 11]

[48]
## Linear algebra
[50]
a=np.ones((2,3))
a
array([[1., 1., 1.],
       [1., 1., 1.]])
[51]
b=np.full((3,2),2)
b
array([[2, 2],
       [2, 2],
       [2, 2]])
[54]
np.matmul(a,b) ##matrix multiplication
array([[6., 6.],
       [6., 6.]])
[56]
c=np.identity(3)
c
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])
[57]
np.linalg.det(c)
1.0
[58]
##Statistics

a=np.array([[1,2,3],[4,5,6]])
a
array([[1, 2, 3],
       [4, 5, 6]])
[63]
np.sum(a)
21
[64]
np.sum(a, axis=0)  ##row
array([5, 7, 9])
[59]
np.min(a)
1
[60]
np.max(a)
6
[62]
np.max(a, axis=1) ###axis=0(ROW) axis=1(COLUMN)
array([3, 6])
Pandas
[65]
import pandas as pd
[67]
x=['a','b','c','d','e']
y=[1,2,3,4,5]
type(x)
list
[70]
a=pd.Series(x,y)
a
1    a
2    b
3    c
4    d
5    e
dtype: object
[69]
type(a)
pandas.core.series.Series
[72]
## creating a dataframe 
r=np.random.randint(1,25,(5,4))
r
array([[ 1,  2,  8,  6],
       [24, 24, 19,  9],
       [13, 13, 23, 19],
       [16, 19,  2, 16],
       [20,  3, 20, 10]])
[73]
df=pd.DataFrame(r)
df

[74]
df=pd.DataFrame(r,['a','b','c','d','e'],['w','x','y','z'])
df

[75]
type(df)
pandas.core.frame.DataFrame
[90]
df['s']=df['y']+df['z']  ### create a new column
df

[79]
### drop a specific row/column
df.drop('e')

[82]
df.drop('s', axis=1)

[83]
df

[84]
df.drop('e', inplace=True)  ### To permanently drop the row/column
[85]
df

[87]
df.drop('s', axis=1, inplace=True)
[91]
df

Indexing and slicing in matrix/dataframe
.loc - name/labels of rows and columns
.iloc - index values
[95]
df

[99]
df.loc['c','z']
19
[96]
df.loc['b']
w    24
x    24
y    19
z     9
s    28
Name: b, dtype: int32
[97]
df.loc['b','y']
19
[100]
df

[103]
df.loc['c':'d','y':'s']

[101]
df.loc['a':'b','x':'y']

[104]
df

[106]
df.iloc[2:,1:4]

[105]
df.iloc[0:2,1:3]

[107]
df

[108]
df>6

[109]
df[df>6]  ###NaN - Not a number (Null values)

[110]
d={'a':[1,2,3,4,5], 'b':[6,8,9,10,np.nan], 'c':[11,12,4,np.nan,np.nan], 'd':[2,5,np.nan,np.nan,np.nan], 'e':[3,np.nan,np.nan,np.nan,np.nan]}
d
{'a': [1, 2, 3, 4, 5],
 'b': [6, 8, 9, 10, nan],
 'c': [11, 12, 4, nan, nan],
 'd': [2, 5, nan, nan, nan],
 'e': [3, nan, nan, nan, nan]}
[111]
d=pd.DataFrame(d)
d

[112]
## Drop the null values
d.dropna()

[117]
d.dropna(thresh=3) ### thresh value - means u need to have that many number of values

[121]
d.fillna(1)

[122]
d

[128]
d['b'].fillna(d['b'].mean(), inplace=True)
[129]
d

[131]
d['c'].fillna(d['c'].mean(), inplace=True)
d


# In[ ]:


DAY13


# In[ ]:





# In[ ]:


Pandas
Dataframe - 2D tabular data structures with labeled axis (rows and columns)
In [81]:
import pandas as pd import numpy as np
In [43]:
## create a dataframe
df1 = {'fruits': ['apples','apples', 'oranges','oranges','mangoes','mangoes','mangoes','b ananas'],
'month':['Nov','Dec','Jan','Feb','Mar','Apr','May','June'], 'Sales':[250,450,300,500,400,270,640,700]}
In [44]:
type(df1)
Out[44]:
dict
In [45]:
df1=pd.DataFrame(df1) df1
Out[45]:
    fruits month Sales
0 1 2 3 4 5 6 7
apples
apples
oranges
oranges
mangoes
mangoes
mangoes
bananas
Nov 250 Dec 450 Jan 300 Feb 500 Mar 400 Apr 270 May 640 June 700
In [46]:
 x=df1.groupby('fruits') x
Out[46]:
<pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001F29201C040>
In [47]:
x.mean() Out[47]:
Sales fruits
 
 
     banfarnunuaiaits 700.000000
mangoes 436.666667
oranges 400.000000
In [48]:
x.sum() Out[48]:
Sales fruits
apples 700 bananas 700 mangoes 1310 oranges 800
In [49]:
x.describe() ### Summary of statistical measures Out[49]:
        fruits
apples
bananas
mangoes
oranges
In [71]:
Sales
count mean std
2.0 350.000000 141.421356
1.0 700.000000 NaN
3.0 436.666667 187.705443
2.0 400.000000 141.421356
min 25% 50%
250.0 300.0 350.0 700.0 700.0 700.0 270.0 335.0 400.0 300.0 350.0 400.0
75% max
400.0 450.0 700.0 700.0 520.0 640.0 450.0 500.0
           df=pd.read_csv('titanic.csv') df
Out[71]:
PassengerId Survived Pclass
Name
Sex
male
female
male
...
female
Age 34.5
47.0
62.0 27.0
...
NaN
39.0 0 0 PC 17758
                      0 1
2 3
...
413 414
892 0
893 1
895 0
... ...
1306 1
3 Kelly, Mr. James
Wilkes, Mrs. 3 James (Ellen Needs)
3 Wirz, Mr. Albert
... ...
1 Oliva y Ocana, Dona. Fermina
SibSp Parch
0 0
1 0
0 0
0 0
... ...
Ticket
330911
363272
240276
315154
...
Fare Cabin Embarked
7.8292 NaN Q
7.0000 NaN S
9.6875 NaN Q
8.6625 NaN S
... ... ...
8.0500 NaN S
108.9000 C105 C
  894 0 2 Myles, Mr. male Thomas Francis
 Hirvonen, Mrs.
4 896 1 3 Alexander female 22.0 1 1 3101298 12.2875 NaN S (Helga E
Lindqvist)
  1305 0 3 Spector, Mr. male Woolf
0 0 A.5.3236
          apples S3S5a0le.0s00000

    Saether, Mr. PassengerId Survived Pclass Name Sex
Age 415 38.5
416 1308 0 3 Ware,Mr. male NaN Frederick
417 NaN 418 rows × 12 columns
In [51]:
df.head(10) ### for displaying first 5 rows Out[51]:
0 0
1 1
359309
2668
8.0500 NaN S
22.3583 NaN C
1307 0 3 Simon Sivertsen male
SOTON/O.Q.
SibSp Parch Ticket Fare Cabin Embarked
0 0 3101262 7.2500 NaN S
             PassengerId Survived Pclass
Name Sex
Ticket
330911
363272
240276
315154
7538
330972
248738
2657
A/4 48871
Ticket
A.5. 3236
PC 17758
Fare Cabin Embarked
7.8292 NaN Q
7.0000 NaN S
9.6875 NaN Q
8.6625 NaN S
9.2250 NaN S
7.6292 NaN Q
29.0000 NaN S
7.2292 NaN C
24.1500 NaN S
Fare Cabin Embarked
8.0500 NaN S
108.9000 C105 C
Age SibSp Parch
                        0 892 1 893
2
3 895
4
5 897
6 898 7 899
8
9 901
In [52]:
0 3
1 3
0 3
0 3
1 3
0 2
0 3
Kelly, Mr. James
Wilkes, Mrs. James (Ellen Needs)
Wirz, Mr. Albert
Svensson, Mr. Johan Cervin
Connolly, Miss. Kate
Caldwell, Mr. Albert Francis
Davies, Mr. John Samuel
male 34.5 0 female 47.0 1
62.0 0 male 27.0 0
22.0
male 14.0 0
female 30.0 0 male 26.0 1
18.0 0 male 21.0 2
0
0
0
0
0
0
1
0
0
  894 0 2 Myles, Mr. Thomas male Francis
  Hirvonen, Mrs.
896 1 3 Alexander (Helga E female
Lindqvist)
1 1 3101298 12.2875 NaN S
    900 1 3 Abrahim, Mrs. Joseph female (Sophie Halaut Easu)
 df.tail() ### last 5 rows Out[52]:
PassengerId Survived Pclass
Name
Oliva y Ocana, Dona. Fermina
Ware, Mr. Frederick
Sex Age SibSp Parch NaN 00
                    413
414 1306
415
416 1308 417
In [53]:
1 1
0 3
female
male
39.0 00 38.5
NaN 00 NaN 11
359309 8.0500
2668 22.3583
NaN S
NaN C
1309 0 3 Peter, Master. male Michael J
1305 0 3 Spector, Mr. male Woolf
  Saether, Mr.
1307 0 3 Simon male
Sivertsen
0 0 SOTON/O.Q. 7.2500 NaN S 3101262
  1309 0 3 Peter, Master. male Michael J
 df.shape ##(rows,columns) Out[53]:
(418, 12)

  In [54]:
df.columns ### to view the column names
Out[54]:
Index(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
dtype='object')
In [55]:
df.dtypes ### to check the datatypes of variables Out[55]:
  PassengerId
Survived
Pclass
Name
Sex
Age
SibSp
Parch
Ticket
Fare
Cabin
Embarked
dtype: object
In [56]:
  int64
  int64
  int64
object
 object
float64
  int64
  int64
 object
float64
 object
 object
 ## To access a single column
df.Name
Out[56]:
0 1 2 3 4
Kelly, Mr. James Wilkes, Mrs. James (Ellen Needs) Myles, Mr. Thomas Francis Wirz, Mr. Albert Hirvonen, Mrs. Alexander (Helga E Lindqvist)
...
Spector, Mr. Woolf Oliva y Ocana, Dona. Fermina Saether, Mr. Simon Sivertsen Ware, Mr. Frederick Peter, Master. Michael J
df[['Name','Age']] ### Viewing a single/multiple column(s) as a dataframe Out[57]:
413
414
415
416
417
Name: Name, Length: 418, dtype: object
In [57]:
   0 1 2 3 4
...
413 414 415
Name Age
Kelly, Mr. James 34.5 Wilkes, Mrs. James (Ellen Needs) 47.0 Myles, Mr. Thomas Francis 62.0 Wirz, Mr. Albert 27.0 Hirvonen, Mrs. Alexander (Helga E Lindqvist) 22.0 ... ... Spector, Mr. Woolf NaN Oliva y Ocana, Dona. Fermina 39.0 38.5
    Saether, Mr. Simon Sivertsen

   Name Age 416 Ware, Mr. Frederick NaN
417 Peter, Master. Michael J NaN
418 rows × 2 columns
In [58]:
type(df[['Name']]) Out[58]: pandas.core.frame.DataFrame
In [59]:
### Checking the missing values
df.isnull().sum()
Out[59]:
PassengerId 0 Survived 0 Pclass 0 Name 0 Sex 0 Age 86 SibSp 0 Parch 0 Ticket 0 Fare 1 Cabin 327 Embarked 0 dtype: int64
In [60]:
df['Survived'].value_counts()
Out[60]:
0 266
1 152
Name: Survived, dtype: int64
In [61]:
df['Pclass'].value_counts()
Out[61]:
3 218
1 107
2 93
Name: Pclass, dtype: int64
In [75]:
df['Sex'].value_counts()
Out[75]:
male 266
female 152
Name: Sex, dtype: int64
In [84]:
table=pd.pivot_table(df, index=['Sex'], values=['Age'], aggfunc=np.mean) table
Out[84]:
         
  Age Sex
female 30.272362
male 30.272732
In [89]:
df.rename(columns={'Sex':'Gender'}, inplace=True) df
      Out[89]:
                      0 1
2 3
...
413 414
415
416 417
PassengerId
893
895
...
1306
1308
Survived
1
0
...
1
0
Pclass
3
3
...
1
3
Name
Wilkes, Mrs. James (Ellen Needs)
Wirz, Mr. Albert
...
Oliva y Ocana, Dona. Fermina
Ware, Mr. Frederick
Gender
female
male
...
female
male
Age SibSp Parch 34.5 0 0
47.0 1 0
62.0 0 0 27.0 0 0
... ... ...
NaN 0 0 39.0 0 0
38.5
NaN 0 0
NaN 1 1
Ticket
330911
363272
240276
315154
...
A.5. 3236
PC 17758
359309
2668
Fare Cabin Embarked
7.8292 NaN Q
7.0000 NaN S
9.6875 NaN Q
8.6625 NaN S
... ... ...
8.0500 NaN S
108.9000 C105 C
8.0500 NaN S
22.3583 NaN C
892 0 3 Kelly, Mr. male James
  894 0 2 Myles, Mr. male Thomas Francis
 Hirvonen, Mrs.
4 896 1 3 Alexander female 22.0 1 1 3101298 12.2875 NaN S (Helga E
Lindqvist)
  1305 0 3 Spector, Mr. male Woolf
  Saether, Mr.
1307 0 3 Simon male
Sivertsen
0 0 SOTON/O.Q. 7.2500 NaN S 3101262
  418 rows × 12 columns
In [88]:
##masking a column
1309 0 3 Peter, Master. male Michael J
 df[(df.Gender=='male')] Out[88]:
                      0 2
3 5 7
PassengerId Survived Pclass
894 0 2
897 0 3
Name
Myles, Mr. Thomas Francis
Svensson, Mr. Johan Cervin
Gender
male
male
Age SibSp Parch 34.5 0 0
62.0 0 0
27.0 0 0 14.0 0 0 26.0 1 1
Ticket
330911
240276
315154
7538
Fare Cabin Embarked
7.8292 NaN Q
9.6875 NaN Q
8.6625 NaN S
9.2250 NaN S
892 0 3 Kelly, Mr. male James
  895 0 3 Wirz, Mr. male Albert
  899 0 2 Caldwell, Mr. male Albert Francis
248738 29.0000 NaN S
 ... ... ... ... ... ... ... ... ... ... ... ... ...

  ...
407 413
415
416 417
... ... ... ... PassengerId Survived Pclass Name
... ... Gender Age
50.0 male NaN
38.5
male NaN NaN
... ... SibSp Parch
0 0
0 0
1 1
... Ticket
A.5. 3236
359309
2668
... ... Fare Cabin
8.0500 NaN
8.0500 NaN
22.3583 NaN
... Embarked
     1299 0 1 Widener, Mr. male George Dunton
       1 1 113503 211.5000 C80 C
1305 0 3
1308 0 3
Spector, Mr. Woolf
Ware, Mr. Frederick
S
S
C
  Saether, Mr.
1307 0 3 Simon male
Sivertsen
0 0 SOTON/O.Q. 7.2500 NaN S 3101262
  266 rows × 12 columns
In [90]:
1309 0 3 Peter, Master. male Michael J
 from sklearn.datasets import load_boston In [95]:
boston_dataset=load_boston() boston_dataset
Out[95]:
 {'data': array([[6.3200e-03, 1.8000e+01, 2.3100e+00, ..., 1.5300e+01, 3.9690e+02, 4.9800e+00],
[2.7310e-02, 0.0000e+00, 7.0700e+00, ..., 1.7800e+01, 3.9690e+02, 9.1400e+00],
[2.7290e-02, 0.0000e+00, 7.0700e+00, ..., 1.7800e+01, 3.9283e+02, 4.0300e+00],
...,
[6.0760e-02, 0.0000e+00, 1.1930e+01, ..., 2.1000e+01, 3.9690e+02,
5.6400e+00],
[1.0959e-01, 0.0000e+00, 1.1930e+01, ..., 2.1000e+01, 3.9345e+02,
6.4800e+00],
[4.7410e-02, 0.0000e+00, 1.1930e+01, ..., 2.1000e+01, 3.9690e+02,
7.8800e+00]]),
'target': array([24. , 21.6, 34.7, 33.4, 36.2, 28.7, 22.9, 27.1, 16.5, 18.9, 15. ,
18.9, 21.7, 20.4, 18.2, 19.9, 23.1, 17.5, 20.2, 18.2, 13.6, 19.6, 15.2, 14.5, 15.6, 13.9, 16.6, 14.8, 18.4, 21. , 12.7, 14.5, 13.2, 13.1, 13.5, 18.9, 20. , 21. , 24.7, 30.8, 34.9, 26.6, 25.3, 24.7, 21.2, 19.3, 20. , 16.6, 14.4, 19.4, 19.7, 20.5, 25. , 23.4, 18.9, 35.4, 24.7, 31.6, 23.3, 19.6, 18.7, 16. , 22.2, 25. , 33. , 23.5, 19.4, 22. , 17.4, 20.9, 24.2, 21.7, 22.8, 23.4, 24.1, 21.4, 20. , 20.8, 21.2, 20.3, 28. , 23.9, 24.8, 22.9, 23.9, 26.6, 22.5, 22.2, 23.6, 28.7, 22.6, 22. , 22.9, 25. , 20.6, 28.4, 21.4, 38.7, 43.8, 33.2, 27.5, 26.5, 18.6, 19.3, 20.1, 19.5, 19.5, 20.4, 19.8, 19.4, 21.7, 22.8, 18.8, 18.7, 18.5, 18.3, 21.2, 19.2, 20.4, 19.3, 22. , 20.3, 20.5, 17.3, 18.8, 21.4, 15.7, 16.2, 18. , 14.3, 19.2, 19.6, 23. , 18.4, 15.6, 18.1, 17.4, 17.1, 13.3, 17.8, 14. , 14.4, 13.4, 15.6, 11.8, 13.8, 15.6, 14.6, 17.8, 15.4, 21.5, 19.6, 15.3, 19.4, 17. , 15.6, 13.1, 41.3, 24.3, 23.3, 27. , 50. , 50. , 50. , 22.7, 25. , 50. , 23.8, 23.8, 22.3, 17.4, 19.1, 23.1, 23.6, 22.6, 29.4, 23.2, 24.6, 29.9, 37.2, 39.8, 36.2, 37.9, 32.5, 26.4, 29.6, 50. , 32. , 29.8, 34.9, 37. , 30.5, 36.4, 31.1, 29.1, 50. , 33.3, 30.3, 34.6, 34.9, 32.9, 24.1, 42.3, 48.5, 50. , 22.6, 24.4, 22.5, 24.4, 20. , 21.7, 19.3, 22.4, 28.1, 23.7, 25. , 23.3, 28.7, 21.5, 23. , 26.7, 21.7, 27.5, 30.1, 44.8, 50. , 37.6, 31.6, 46.7, 31.5, 24.3, 31.7, 41.7, 48.3, 29. , 24. , 25.1, 31.5, 23.7, 23.3, 22. , 20.1, 22.2, 23.7, 17.6, 18.5, 24.3, 20.5, 24.5, 26.2, 24.4, 24.8, 29.6, 42.8, 21.9, 20.9, 44. , 50. , 36. , 30.1, 33.8, 43.1, 48.8, 31. , 36.5, 22.8, 30.7, 50. , 43.5, 20.7, 21.1, 25.2, 24.4, 35.2, 32.4, 32. , 33.2, 33.1, 29.1, 35.1, 45.4, 35.4, 46. , 50. , 32.2, 22. , 20.1, 23.2, 22.3, 24.8, 28.5, 37.3, 27.9, 23.9, 21.7, 28.6, 27.1, 20.3, 22.5, 29. , 24.8, 22. , 26.4, 33.1, 36.1, 28.4, 33.4, 28.2, 22.8, 20.3, 16.1, 22.1, 19.4, 21.6, 23.8, 16.2, 17.8, 19.8, 23.1, 21. , 23.8, 23.1, 20.4, 18.5, 25. , 24.6, 23. , 22.2, 19.3, 22.6,
 19.8, 17.1, 19.4, 22.2, 20.7, 21.1, 19.5, 18.5, 20.6, 19. , 18.7,

 198,171,194,222,207,211,195,185,206,19 ,187,
 ...........
32.7, 16.5, 23.9, 31.2, 17.5, 17.2, 23.1, 24.5, 26.6, 22.9, 24.1, 18.6, 30.1, 18.2, 20.6, 17.8, 21.7, 22.7, 22.6, 25. , 19.9, 20.8, 16.8, 21.9, 27.5, 21.9, 23.1, 50. , 50. , 50. , 50. , 50. , 13.8, 13.8, 15. , 13.9, 13.3, 13.1, 10.2, 10.4, 10.9, 11.3, 12.3, 8.8,
7.2, 10.5, 7.4, 10.2, 11.5, 15.1, 23.2, 9.7, 13.8, 12.7, 13.1, 12.5, 8.5, 5. , 6.3, 5.6, 7.2, 12.1, 8.3, 8.5, 5. , 11.9, 27.9, 17.2, 27.5, 15. , 17.2, 17.9, 16.3, 7. , 7.2, 7.5, 10.4,
8.8, 8.4, 16.7, 14.2, 20.8, 13.4, 11.7, 8.3, 10.2, 10.9, 11. ,
9.5, 14.5, 14.1, 16.1, 14.3, 11.7, 13.4, 9.6, 8.7, 8.4, 12.8, 10.5, 17.1, 18.4, 15.4, 10.8, 11.8, 14.9, 12.6, 14.1, 13. , 13.4, 15.2, 16.1, 17.8, 14.9, 14.1, 12.7, 13.5, 14.9, 20. , 16.4, 17.7, 19.5, 20.2, 21.4, 19.9, 19. , 19.1, 19.1, 20.1, 19.9, 19.6, 23.2, 29.8, 13.8, 13.3, 16.7, 12. , 14.6, 21.4, 23. , 23.7, 25. , 21.8, 20.6, 21.2, 19.1, 20.6, 15.2, 7. , 8.1, 13.6, 20.1, 21.8, 24.5, 23.1, 19.7, 18.3, 21.2, 17.5, 16.8, 22.4, 20.6, 23.9, 22. , 11.9]),
'feature_names': array(['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT'], dtype='<U7'),
'DESCR': ".. _boston_dataset:\n\nBoston house prices dataset\n------------------------- --\n\n**Data Set Characteristics:** \n\n :Number of Instances: 506 \n\n :Number of
Attributes: 13 target.\n\n
te by town\n sq.ft.\n
numeric/categorical predictive. Median Value (attribute 14) is usually the :Attribute Information (in order):\n - CRIM per capita crime ra
- ZN proportion of residential land zoned for lots over 25,000
- INDUS proportion of non-retail business acres per town\n
Charles
 nitric
 rooms per dwelling\n
River dummy variable oxides concentration
(= 1 if tract bounds river; 0 otherwise)\n (parts per 10 million)\n - RM
- CH - N average nu - AGE proportion of owner-occupied units built p
AS
OX
mber of
rior to 1940\n - DIS weighted distances to five Boston employment centres\n
- RAD
rty-tax
1000(Bk
r status of the population\n - MEDV Median value of owner-occupied homes in $1 000's\n\n :Missing Attribute Values: None\n\n :Creator: Harrison, D. and Rubinfeld, D.L.\n\nThis is a copy of UCI ML housing dataset.\nhttps://archive.ics.uci.edu/ml/machine -learning-databases/housing/\n\n\nThis dataset was taken from the StatLib library which i s maintained at Carnegie Mellon University.\n\nThe Boston house-price data of Harrison, D . and Rubinfeld, D.L. 'Hedonic\nprices and the demand for clean air', J. Environ. Economi cs & Management,\nvol.5, 81-102, 1978. Used in Belsley, Kuh & Welsch, 'Regression diagn ostics\n...', Wiley, 1980. N.B. Various transformations are used in the table on\npages 244-261 of the latter.\n\nThe Boston house-price data has been used in many machine learn ing papers that address regression\nproblems. \n \n.. topic:: References\n\n - Be lsley, Kuh & Welsch, 'Regression diagnostics: Identifying Influential Data and Sources of Collinearity', Wiley, 1980. 244-261.\n - Quinlan,R. (1993). Combining Instance-Based an d Model-Based Learning. In Proceedings on the Tenth International Conference of Machine L earning, 236-243, University of Massachusetts, Amherst. Morgan Kaufmann.\n",
'filename': 'C:\\Users\\Laxmi Ravindran\\anaconda3\\lib\\site-packages\\sklearn\\dataset s\\data\\boston_house_prices.csv'}
In [96]:
boston_df=pd.DataFrame(boston_dataset.data, columns=boston_dataset.feature_names)
In [97]:
boston_df
Out[97]:
CRIM ZN INDUS CHAS NOX RM AGE DIS RAD TAX PTRATIO B LSTAT
0 0.00632 18.0 2.31 0.0 0.538 6.575 65.2 4.0900 1.0 296.0 15.3 396.90 4.98 1 0.02731 0.0 7.07 0.0 0.469 6.421 78.9 4.9671 2.0 242.0 17.8 396.90 9.14 2 0.02729 0.0 7.07 0.0 0.469 7.185 61.1 4.9671 2.0 242.0 17.8 392.83 4.03 3 0.03237 0.0 2.18 0.0 0.458 6.998 45.8 6.0622 3.0 222.0 18.7 394.63 2.94 4 0.06905 0.0 2.18 0.0 0.458 7.147 54.2 6.0622 3.0 222.0 18.7 396.90 5.33
... ... ... ... ... ... ... ... ... ... ... ... ... ...
501 0.06263 0.0 11.93 0.0 0.573 6.593 69.1 2.4786 1.0 273.0 21.0 391.99 9.67 502 0.04527 0.0 11.93 0.0 0.573 6.120 76.7 2.2875 1.0 273.0 21.0 396.90 9.08
index of accessibility to radial highways\n - TAX full-value prope rate per $10,000\n - PTRATIO pupil-teacher ratio by town\n - B
- 0.63)^2 where Bk is the proportion of blacks by town\n - LSTAT % lowe
                               
     502 0.04527 0.0 11.93 0.0 0.573 6.120 76.7 2.2875 1.0 273.0 21.0 396.90 9.08
 ZN NOX RM AGE RAD TAX 503     0.0 0.573 6.976 91.0     1.0 273.0
504 0.10959 0.0 11.93 0.0 0.573 6.794 89.3 2.3889 1.0 273.0 21.0 393.45 6.48 505 0.04741 0.0 11.93 0.0 0.573 6.030 80.8 2.5050 1.0 273.0 21.0 396.90 7.88
506 rows × 13 columns
In [98]:
boston_df.head() Out[98]:
CRIM ZN INDUS CHAS NOX RM AGE DIS RAD TAX PTRATIO B LSTAT
CRIM 0.06076
DIS 2.1675
                     0 0.00632 18.0 2.31 0.0 0.538 6.575 65.2 1 0.02731 0.0 7.07 0.0 0.469 6.421 78.9 2 0.02729 0.0 7.07 0.0 0.469 7.185 61.1 3 0.03237 0.0 2.18 0.0 0.458 6.998 45.8 4 0.06905 0.0 2.18 0.0 0.458 7.147 54.2
In [99]:
boston_df.shape Out[99]:
(506, 13)
In [100]:
boston_df.info()
<class 'pandas.core.frame.DataFrame'> RangeIndex: 506 entries, 0 to 505 Data columns (total 13 columns):
4.0900 1.0 296.0 15.3 396.90 4.98 4.9671 2.0 242.0 17.8 396.90 9.14 4.9671 2.0 242.0 17.8 392.83 4.03 6.0622 3.0 222.0 18.7 394.63 2.94 6.0622 3.0 222.0 18.7 396.90 5.33
          # Column --- ------
0 CRIM
1 ZN
2 INDUS
3 CHAS
4 NOX
5 RM
6 AGE
7 DIS
8 RAD
9 TAX
10 PTRATIO
11 B
12 LSTAT
Non-Null Count -------------- 506 non-null 506 non-null 506 non-null 506 non-null 506 non-null 506 non-null 506 non-null 506 non-null 506 non-null 506 non-null 506 non-null 506 non-null 506 non-null
Dtype ----- float64 float64 float64 float64 float64 float64 float64 float64 float64 float64 float64 float64 float64
dtypes: float64(13) memory usage: 51.5 KB
In [101]:
boston_df.describe() Out[101]:
 CRIM
count 506.000000
mean 3.613524
std 8.601545
ZN INDUS CHAS NOX RM AGE
DIS
RAD
TAX
                     506.000000 506.000000 506.000000 506.000000 506.000000 506.000000 506.000000 506.000000 506.000000
11.363636
23.322453
11.136779
6.860353
0.460000
0.069170
0.253994
0.000000
0.554695
0.115878
0.385000
6.284634
0.702617
3.561000
68.574901
28.148861
3.795043
2.105710
1.129600
9.549407
8.707259
1.000000
408.237154 168.537116 187.000000
 min 0.006320
0.000000
2.900000
INDUS CHAS 11.93       0.0
PTRATIO B LSTAT 21.0 396.90 5.64
     50

      50%
75%
max
0.256510
3.677083
88.976200
0.000000
12.500000
100.000000
9.690000
18.100000
27.740000
0.000000
0.000000
1.000000
0.538000
0.624000
0.871000
6.208500
6.623500
8.780000
77.500000
94.075000
100.000000
3.207450
5.188425
12.126500
5.000000
24.000000
24.000000
0X0 330.000000 666.000000 711.000000
     In [102]:
 boston_df.count()
Out[102]:
CRIM       506
ZN         506
INDUS      506
CHAS       506
NOX        506
RM         506
AGE        506
DIS        506
RAD        506
TAX        506
PTRATIO    506
B          506
LSTAT      506
dtype: int64
In [103]:
 boston_df.mean() ### mean, column-wise Out[103]:
CRIM
ZN
INDUS
CHAS
NOX
RM
AGE
DIS
RAD
TAX
PTRATIO
B
3.613524 11.363636 11.136779
0.069170 0.554695 6.284634
68.574901 3.795043 9.549407
408.237154 18.455534 356.674032 12.653063
boston_df.columns
Out[105]:
LSTAT
dtype: float64
In [105]:
 Index(['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT'],
dtype='object')
In [106]:
###Manipulating a dataframe
boston_df['Price']=boston_dataset.target
In [107]:
boston_df.head() Out[107]:
  25% 0.08C2R0I4M5 0.0000Z0N0 5.1IN90D0U0S0 0.0C00H0A0S0 0.449N0O0X0 5.8855R0M0 45.025A0G0E0 2.100D17IS5 4.000R0A0D0 279.000T0
          A

  CRIM ZN INDUS CHAS NOX RM AGE DIS RAD TAX PTRATIO B LSTAT Price CRIM ZN INDUS CHAS NOX RM AGE DIS RAD TAX PTRATIO B LSTAT Price
0 0.00632 18.0 2.31 0.0 0.538 6.575 65.2 4.0900 1.0 296.0 15.3 396.90 4.98 24.0 1 0.02731 0.0 7.07 0.0 0.469 6.421 78.9 4.9671 2.0 242.0 17.8 396.90 9.14 21.6 2 0.02729 0.0 7.07 0.0 0.469 7.185 61.1 4.9671 2.0 242.0 17.8 392.83 4.03 34.7 3 0.03237 0.0 2.18 0.0 0.458 6.998 45.8 6.0622 3.0 222.0 18.7 394.63 2.94 33.4 4 0.06905 0.0 2.18 0.0 0.458 7.147 54.2 6.0622 3.0 222.0 18.7 396.90 5.33 36.2
In [109]:
boston_df.drop(index=0, axis=0) Out[109]:
CRIM ZN INDUS CHAS NOX RM AGE DIS RAD TAX PTRATIO B LSTAT Price
                                           1 0.02731 0.0 7.07 0.0 0.469 6.421 78.9 4.9671 2.0 242.0 17.8 396.90 2 0.02729 0.0 7.07 0.0 0.469 7.185 61.1 4.9671 2.0 242.0 17.8 392.83 3 0.03237 0.0 2.18 0.0 0.458 6.998 45.8 6.0622 3.0 222.0 18.7 394.63 4 0.06905 0.0 2.18 0.0 0.458 7.147 54.2 6.0622 3.0 222.0 18.7 396.90 5 0.02985 0.0 2.18 0.0 0.458 6.430 58.7 6.0622 3.0 222.0 18.7 394.12
9.14 21.6 4.03 34.7 2.94 33.4 5.33 36.2 5.21 28.7
        ... ... ... ... ... ... ... ... ... ... ... ... ... ... ...
    501 0.06263 0.0 11.93 0.0 0.573 6.593 69.1 2.4786 1.0 273.0 21.0 391.99 502 0.04527 0.0 11.93 0.0 0.573 6.120 76.7 2.2875 1.0 273.0 21.0 396.90 503 0.06076 0.0 11.93 0.0 0.573 6.976 91.0 2.1675 1.0 273.0 21.0 396.90 504 0.10959 0.0 11.93 0.0 0.573 6.794 89.3 2.3889 1.0 273.0 21.0 393.45 505 0.04741 0.0 11.93 0.0 0.573 6.030 80.8 2.5050 1.0 273.0 21.0 396.90
505 rows × 14 columns
In [111]:
boston_df.drop(columns=['ZN','CHAS'], axis=1) Out[111]:
CRIM INDUS NOX RM AGE DIS RAD TAX PTRATIO B LSTAT Price
0 0.00632 2.31 0.538 6.575 65.2 4.0900 1.0 296.0 15.3 396.90 4.98 24.0 1 0.02731 7.07 0.469 6.421 78.9 4.9671 2.0 242.0 17.8 396.90 9.14 21.6 2 0.02729 7.07 0.469 7.185 61.1 4.9671 2.0 242.0 17.8 392.83 4.03 34.7 3 0.03237 2.18 0.458 6.998 45.8 6.0622 3.0 222.0 18.7 394.63 2.94 33.4 4 0.06905 2.18 0.458 7.147 54.2 6.0622 3.0 222.0 18.7 396.90 5.33 36.2
... ... ... ... ... ... ... ... ... ... ... ... ...
501 0.06263 11.93 0.573 6.593 69.1 2.4786 1.0 273.0 21.0 391.99 9.67 22.4 502 0.04527 11.93 0.573 6.120 76.7 2.2875 1.0 273.0 21.0 396.90 9.08 20.6 503 0.06076 11.93 0.573 6.976 91.0 2.1675 1.0 273.0 21.0 396.90 5.64 23.9 504 0.10959 11.93 0.573 6.794 89.3 2.3889 1.0 273.0 21.0 393.45 6.48 22.0 505 0.04741 11.93 0.573 6.030 80.8 2.5050 1.0 273.0 21.0 396.90 7.88 11.9
506 rows × 12 columns
In [113]:
boston_df.iloc[505] Out[113]:
9.67 22.4 9.08 20.6 5.64 23.9 6.48 22.0 7.88 11.9
                                        
 Out[113]:
CRIM
ZN
INDUS
CHAS
NOX
RM
AGE
DIS
RAD
TAX
PTRATIO
B
0.04741
0.00000 11.93000 0.00000 0.57300 6.03000 80.80000 2.50500 1.00000 273.00000 21.00000 396.90000 7.88000 11.90000
boston_df.iloc[:,-1]
Out[115]:
0 24.0
1 21.6
2 34.7
3 33.4
4 36.2
...
501 22.4
502 20.6
503 23.9
504 22.0
505 11.9
Name: Price, Length: 506, dtype: float64
In [116]:
## Assignment
from sklearn.datasets import load_diabetes In [ ]:
LSTAT
Price
Name: 505, dtype: float64
In [115]:
    


# In[ ]:


DAY14


# In[ ]:


import pandas as pd
import numpy as np
Rearranging the columns in a dataframe
[2]
df=pd.DataFrame(np.random.rand(10,5))
df

[3]
df['mean']=df.mean(1)
df

[4]
df.columns
Index([0, 1, 2, 3, 4, 'mean'], dtype='object')
[5]
df=df[[4,'mean',3,2,1]]
df

[6]
df=df.reindex(columns=['mean',1,2,3,4])
df

[7]
column_names=[4,3,'mean']
df=df.reindex(columns=column_names)
df

Handling missing values
[8]
df=pd.read_csv("weather_data.csv")
df

[9]
df.set_index('date', inplace=True)
[10]
df.head()

[11]
new_df=df.fillna(0)
new_df

[12]
new_df.columns
Index(['temperature', 'windspeed ', 'Events'], dtype='object')
[13]
new_df=df.fillna({'temperature':0,
                  'windspeed ':0,
                  'Events':'No event'})
new_df.head()

[14]
new_df=df.fillna(method="ffill")
new_df

[15]
new_df=df.fillna(method="bfill")
new_df

[16]
new_df=new_df.replace({'Cloudy':'Sunny'})
new_df

[17]
new_df=df.fillna(method="ffill", limit=2)
new_df

[21]
df

[24]
#new_df=df.interpolate()
#new_df
[25]
new_df.dtypes
temperature    object
windspeed      object
Events         object
dtype: object
[26]
df

[27]
new_df=df.dropna()
[28]
## to add the missing dates

dt=pd.date_range('01-01-2016','01-11-2016')
idx=pd.DatetimeIndex(dt)
df=df.reindex(idx)
[29]
type(idx)
pandas.core.indexes.datetimes.DatetimeIndex
[30]
df.dtypes
temperature    object
windspeed      object
Events         object
dtype: object
[31]
df=pd.read_csv('weather_data.csv')
df.head()

[32]
### regular expression (regex) - used to replace any patterns

df1=df.replace('[A-Za-z]','', regex=True)
df1

[33]
df1=df.replace({'temperature':'[A-Za-z]', 'windspeed ':'[A-Za-z]'},'', regex=True)
df1

[34]
#### Replace a list of values in a columns with a new list of values

df=pd.DataFrame({'Score':['Excel','good','avg','poor','Excel','good'],
                'Student':['a','b','c','d','e','f']})
df

[35]
new_df=df.replace(['poor','avg','good','Excel'],[1,2,3,4])
new_df


# In[ ]:


day15


# In[3]:


Data visualization using pandas
In [2]:
## Import libraries
import numpy as np
import pandas as pd
from numpy.random import randn, randint, uniform, sample
In [3]:
pd.DataFrame(randn(100)) Out[3]:
  
0 1 2 3 4
...
95 96 97 98 99
0
-1.362824
-1.303100
-0.078055
-0.368322
0.894979
...
0.596446
-1.272193
-0.207650
-0.857266
-0.080833
100 rows × 1 columns
In [5]:
df=pd.DataFrame(randn(100), index=pd.date_range('01-01-2021', periods=100), columns=['va lue'])
df.tail()
Out[5]:
2021-04-06 0.051694
2021-04-07 0.736291
2021-04-08 -0.723140
2021-04-09 -0.295126
2021-04-10 -0.419689
In [6]:
type(df)
Out[6]: pandas.core.frame.DataFrame
In [9]:
ds=pd.Series(randn(100), index=pd.date_range('01-01-2021', periods=100))
 value
   
   ds.head()
Out[9]:
2021-01-01 0.487739 2021-01-02 -0.420996 2021-01-03 0.554809 2021-01-04 -1.263474 2021-01-05 0.908801 Freq: D, dtype: float64
In [10]:
df.plot() Out[10]: <AxesSubplot:>
  In [12]:
ds.plot() Out[12]: <AxesSubplot:>
  In [13]:
import matplotlib.pyplot as plt %matplotlib inline
In [16]:
x = np.linspace(0, 10, 50) y = np.sin(x)
In [17]:
x
    
   Out[17]:
array([ 0. , 0.20408163, 0.40816327, 0.6122449 , 0.81632653, 1.02040816, 1.2244898 , 1.42857143, 1.63265306, 1.83673469, 2.04081633, 2.24489796, 2.44897959, 2.65306122, 2.85714286, 3.06122449, 3.26530612, 3.46938776, 3.67346939, 3.87755102, 4.08163265, 4.28571429, 4.48979592, 4.69387755, 4.89795918, 5.10204082, 5.30612245, 5.51020408, 5.71428571, 5.91836735, 6.12244898, 6.32653061, 6.53061224, 6.73469388, 6.93877551, 7.14285714, 7.34693878, 7.55102041, 7.75510204, 7.95918367, 8.16326531, 8.36734694, 8.57142857, 8.7755102 , 8.97959184, 9.18367347, 9.3877551 , 9.59183673, 9.79591837, 10. ])
In [18]:
y
Out[18]:
 array([
0. , 0.20266794, 0.39692415, 0.57470604, 0.72863478, 0.85232157, 0.94063279, 0.98990308, 0.99808748, 0.96484631, 0.89155923, 0.78126802, 0.63855032, 0.46932961, 0.2806294 , 0.08028167, -0.12339814, -0.32195632, -0.50715171, -0.67129779,
-0.80758169, -0.91034694, -0.97532829, -0.99982867, -0.9828312 , -0.92504137, -0.82885774, -0.6982724 , -0.53870529, -0.35677924, -0.16004509, 0.04333173, 0.24491007, 0.43632343, 0.6096272 ,
0.75762842, 0.8741843 , 0.9544572 , 0.99511539, 0.99447137, 0.95255185, 0.8710967 , 0.75348673, 0.60460332, 0.43062587, 0.23877532, 0.0370144 , -0.16628279, -0.36267843, -0.54402111])
In [27]:
## Line plot
#plt.plot(x,y,'g*')
plt.plot(x,y,color='green', marker='*', linestyle='dashed',linewidth=1, markersize=5) plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('sine wave')
plt.show()
In [31]:
x=np.linspace(-10,10,20) y=x**2
x
Out[31]:
array([-10. , -8.94736842, -7.89473684, -6.84210526, -5.78947368, -4.73684211, -3.68421053, -2.63157895, -1.57894737, -0.52631579, 0.52631579, 1.57894737,
2.63157895, 3.68421053, 4.73684211, 5.78947368, 6.84210526, 7.89473684, 8.94736842, 10. ])
    In [34]:

 In [34]:
plt.plot(x,y,'k-.') plt.show()
In [35]:
import seaborn as sns In [36]:
iris = sns.load_dataset('iris') iris.head()
Out[36]:
sepal_length sepal_width petal_length petal_width species
                0 5.1 1 4.9 2 4.7 3 4.6 4 5.0
In [37]:
iris.shape Out[37]: (150, 5)
In [39]:
3.5 1.4
3.0 1.4
3.2 1.3
3.1 1.5
3.6 1.4
0.2 setosa
0.2 setosa
0.2 setosa
0.2 setosa
0.2 setosa
    iris['species'].unique()
Out[39]:
array(['setosa', 'versicolor', 'virginica'], dtype=object)
In [42]:
ax=iris.plot(figsize=(15,8), title='Iris dataset') ax.set_xlabel('X-axis')
ax.set_ylabel('Y axis')
Out[42]:
Text(0, 0.5, 'Y axis')
   
   In [43]:
df=iris.drop(['species'], axis=1) df
Out[43]:
sepal_length sepal_width petal_length petal_width 0 5.1 3.5 1.4 0.2 1 4.9 3.0 1.4 0.2 2 4.7 3.2 1.3 0.2 3 4.6 3.1 1.5 0.2 4 5.0 3.6 1.4 0.2
... ... ... ... ...
145 6.7 3.0 5.2 2.3 146 6.3 2.5 5.0 1.9 147 6.5 3.0 5.2 2.0 148 6.2 3.4 5.4 2.3 149 5.9 3.0 5.1 1.8
150 rows × 4 columns
In [45]:
df.iloc[0] ### data from 0th index
Out[45]:
sepal_length 5.1 sepal_width 3.5 petal_length 1.4 petal_width 0.2 Name: 0, dtype: float64
In [72]:
x=[1,2,3,4,5,6] y=[1,4,6,8,10,12]
In [73]:
x2=np.arange(0,4,0.5)
                   
   x2**2
Out[73]:
array([ 0. , 0.25, 1. , 2.25, 4. , 6.25, 9. , 12.25])
In [75]:
plt.plot(x,y,'r^--', label='2x') plt.plot(x2, x2**2, 'g', label='x^2') plt.legend()
plt.show()
  Bar charts
A bar chart or bar graph is a chart or graph that presents categorical data with rectangular bars with heights or lengths proportional to the values that they represent.
In [47]:
df.iloc[0].plot(kind='bar') Out[47]:
<AxesSubplot:>
  In [48]:
df.iloc[1].plot.bar() Out[48]: <AxesSubplot:>
   
   In [80]:
labels=['A', 'B', 'C'] values=[1,4,7] bars=plt.bar(labels,values) patterns=['/', 'O', '*'] bars[0].set_hatch('/') bars[1].set_hatch('o') bars[2].set_hatch('*') plt.show()
Histogram
A histogram is a graph showing frequency distributions.
It is a graph showing the number of observations within each given interval
In [52]:
iris['sepal_length'].plot.hist() plt.show()
    In [56]:
 
   #iris.plot.hist()
iris.plot(kind='hist')
Out[56]: <AxesSubplot:ylabel='Frequency'>
In [60]:
iris.plot(kind='hist', stacked=True, bins=50, orientation='horizontal') Out[60]:
<AxesSubplot:xlabel='Frequency'>
In [62]:
df=iris.drop(['species'], axis=1) df.diff().head()
Out[62]:
sepal_length sepal_width petal_length petal_width
             0 NaN NaN 1 -0.2 -0.5 2 -0.2 0.2 3 -0.1 -0.1 4 0.4 0.5
In [66]:
NaN NaN
0.0 0.0
-0.1 0.0
0.2 0.0
-0.1 0.0
   df.hist(color='#D733FF', figsize=(10,10))
Out[66]:
array([[<AxesSubplot:title={'center':'sepal_length'}>, <AxesSubplot:title={'center':'sepal width'}>],
 _

 <AxesSubplot:title={'center':'sepal width'}>],
 _
[<AxesSubplot:title={'center':'petal_length'}>, <AxesSubplot:title={'center':'petal_width'}>]], dtype=object)
Scatter
The scatter() function plots one dot for each observation. It needs two arrays of the same length, one for the values of the x-axis, and one for values on the y-axis
In [67]:
## scatter plot
iris.plot.scatter(x='sepal_length', y='petal_length') Out[67]:
<AxesSubplot:xlabel='sepal_length', ylabel='petal_length'>
    
 
In [ ]:
  


# In[ ]:


DAY16


# In[ ]:


### Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
[11]
### Line plot

yield_mangoes = [0.82,0.85, 0.90,0.93,0.98,0.87]
years = [2014, 2015, 2016, 2017, 2018, 2019]
[12]
plt.plot(years, yield_mangoes)
plt.show()

[13]
yield_apples = [0.82,0.75, 0.78,0.93,0.68,0.87]
years = [2014, 2015, 2016, 2017, 2018, 2019]
[14]
plt.plot(years, yield_apples)
[<matplotlib.lines.Line2D at 0x14767b30a60>]

[19]
plt.plot(years, yield_mangoes)
plt.plot(years, yield_apples)
plt.xlabel('Years')
plt.ylabel('Yield per hectare')
plt.legend(iris = sns.load_dataset('iris')
iris.head())
plt.show()

[20]
iris = sns.load_dataset('iris')
iris.head()

[21]
iris.shape
(150, 5)
[23]
iris['species'].nunique()
3
[25]
### Scatter plot - Bivariate analysis

sns.scatterplot(x=iris['petal_length'], y=iris['petal_width'], hue=iris['species'])
<AxesSubplot:xlabel='petal_length', ylabel='petal_width'>

[26]
sns.scatterplot(x=iris['sepal_length'], y=iris['sepal_width'], hue=iris['species'])
<AxesSubplot:xlabel='sepal_length', ylabel='sepal_width'>

[27]
##Pairplot

sns.set_style("whitegrid")
sns.pairplot(iris, hue="species", size=3)
plt.show()
C:\Users\Laxmi Ravindran\anaconda3\lib\site-packages\seaborn\axisgrid.py:1912: UserWarning: The `size` parameter has been renamed to `height`; please update your code.
  warnings.warn(msg, UserWarning)


[38]
### Histogram - Frequency distribution plot

plt.hist(iris['sepal_length'])
plt.show()

[43]
plt.hist(iris['petal_width'], bins=10, rwidth=0.75, color='g')
plt.show()

[44]
## Pie chart
expenses_labels=['rent', 'food', 'internet','car', 'misc']
expenses_values=[15000, 5000, 2000, 3000, 2000]
[64]
plt.pie(expenses_values, labels=expenses_labels, radius=1.35, autopct='%0.0f%%', shadow=True, explode=[0,0,0,0.1,0.2], startangle=180)
plt.show()
plt.savefig("piechart.png", transparent=True)

<Figure size 432x288 with 0 Axes>
[72]
## Distribution Plot [dist-plot] - univariate analysis

sns.FacetGrid(iris, hue="species", size=5).map(sns.distplot, 'petal_length').add_legend()
plt.show()
C:\Users\Laxmi Ravindran\anaconda3\lib\site-packages\seaborn\axisgrid.py:316: UserWarning: The `size` parameter has been renamed to `height`; please update your code.
  warnings.warn(msg, UserWarning)
C:\Users\Laxmi Ravindran\anaconda3\lib\site-packages\seaborn\distributions.py:2551: FutureWarning: `distplot` is a deprecated function and will be removed in a future version. Please adapt your code to use either `displot` (a figure-level function with similar flexibility) or `histplot` (an axes-level function for histograms).
  warnings.warn(msg, FutureWarning)
C:\Users\Laxmi Ravindran\anaconda3\lib\site-packages\seaborn\distributions.py:2551: FutureWarning: `distplot` is a deprecated function and will be removed in a future version. Please adapt your code to use either `displot` (a figure-level function with similar flexibility) or `histplot` (an axes-level function for histograms).
  warnings.warn(msg, FutureWarning)
C:\Users\Laxmi Ravindran\anaconda3\lib\site-packages\seaborn\distributions.py:2551: FutureWarning: `distplot` is a deprecated function and will be removed in a future version. Please adapt your code to use either `displot` (a figure-level function with similar flexibility) or `histplot` (an axes-level function for histograms).
  warnings.warn(msg, FutureWarning)


[73]
## barplot

df=sns.load_dataset("tips")
df.head()

[74]
df.shape
(244, 7)
[80]
sns.barplot(x='sex', y='total_bill', data=df, orient="v")
<AxesSubplot:xlabel='sex', ylabel='total_bill'>

[81]
sns.barplot(x='day', y='tip', data=df, orient="v")
<AxesSubplot:xlabel='day', ylabel='tip'>


# In[ ]:


DAY17


# In[ ]:


Seaborn
[1]
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
[14]
import sys

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")
[2]
train = pd.read_csv("titanic.csv")
[3]
train.head()

[4]
train.shape
(418, 12)
[6]
train['Age'].unique()
array([34.5 , 47.  , 62.  , 27.  , 22.  , 14.  , 30.  , 26.  , 18.  ,
       21.  ,   nan, 46.  , 23.  , 63.  , 24.  , 35.  , 45.  , 55.  ,
        9.  , 48.  , 50.  , 22.5 , 41.  , 33.  , 18.5 , 25.  , 39.  ,
       60.  , 36.  , 20.  , 28.  , 10.  , 17.  , 32.  , 13.  , 31.  ,
       29.  , 28.5 , 32.5 ,  6.  , 67.  , 49.  ,  2.  , 76.  , 43.  ,
       16.  ,  1.  , 12.  , 42.  , 53.  , 26.5 , 40.  , 61.  , 60.5 ,
        7.  , 15.  , 54.  , 64.  , 37.  , 34.  , 11.5 ,  8.  ,  0.33,
       38.  , 57.  , 40.5 ,  0.92, 19.  , 36.5 ,  0.75,  0.83, 58.  ,
        0.17, 59.  , 14.5 , 44.  ,  5.  , 51.  ,  3.  , 38.5 ])
[16]
### Box plot (box and whisker plot) - represent numerical data - Used to identify outlier - 

sns.boxplot(train['Fare'], orient="v")
plt.show()

[21]
train['Sex'].value_counts()
male      266
female    152
Name: Sex, dtype: int64
[26]
sns.barplot(x='Survived', y='Age', hue='Sex', data=train)
<AxesSubplot:xlabel='Survived', ylabel='Age'>

[27]
## Countplot

sns.countplot(train['Survived'])
<AxesSubplot:xlabel='Survived', ylabel='count'>

[28]
sns.countplot(x='Pclass', hue='Survived', data=train)
<AxesSubplot:xlabel='Pclass', ylabel='count'>

[30]
tips=sns.load_dataset("tips")
[31]
tips.head()

[62]
tips.dtypes
total_bill     float64
tip            float64
sex           category
smoker        category
day           category
time          category
size             int64
dtype: object
[65]
tips['size'].value_counts()
2    156
3     38
4     37
5      5
6      4
1      4
Name: size, dtype: int64
[64]
tips.corr()  ### correlation - meant only for numerical variables

[66]
## Heatmap - Very useful in feature selection 

sns.heatmap(tips.corr())
<AxesSubplot:>

[34]
sns.boxplot(data=tips, orient="v")
<AxesSubplot:>

[33]
## violin plot - helps us to see the data distribution in terms of both boxplot and kde

sns.violinplot(x='total_bill', y='day', data=tips)
<AxesSubplot:xlabel='total_bill', ylabel='day'>

[35]
## catplot - categorical variables
sns.catplot(x='day', y='total_bill', data=tips)
<seaborn.axisgrid.FacetGrid at 0x23ecbf85730>

[36]
sns.catplot(x='day', y='tip', data=tips)
<seaborn.axisgrid.FacetGrid at 0x23ecc222940>

[40]
## Relplot- numerical variables
plt.figure(figsize=(10,8))
sns.relplot(x='total_bill', y='tip', hue='smoker', col='time',data=tips)
<seaborn.axisgrid.FacetGrid at 0x23ecc346c70>
<Figure size 720x576 with 0 Axes>

[41]
### swarm plot

sns.swarmplot(x='day', y='total_bill', data=tips)
<AxesSubplot:xlabel='day', ylabel='total_bill'>

[42]
sns.lmplot(x='total_bill', y='tip', data=tips)
<seaborn.axisgrid.FacetGrid at 0x23ecc062b80>

[49]
### pip install plotly 
#### pip install cufflinks

import cufflinks as cf
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
[50]
init_notebook_mode(connected=True)

[51]
cf.go_offline()

[52]
df1=pd.DataFrame(np.random.rand(500,4), columns=['a','b', 'c', 'd'])
[53]
df1.head()

[54]
df2=pd.DataFrame({'x': ['p', 'q','r'],
                  'y': [1,2,3]})
[55]
df2

[58]
df1.iplot(kind='scatter', x='a', y='d', mode='markers')
df1.iplot
[59]
df2.iplot(kind='bar', x='x', y='y')
[61]
df1.iplot(kind='surface')  #### 3-D surface plot
[67]
df=sns.load_dataset("diamonds")
df.head()


# In[4]:


BOX PLOT IS FOR NUMERIC DATA
VIOLIN PLOT IS FOR CATEGORICAL DATA


# In[ ]:


DAY 8


# In[ ]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings('ignore')
[3]
df = pd.read_csv('covid_19_india.csv')
state = pd.read_csv('StatewiseTestingDetails.csv')
vaccine=pd.read_csv('covid_vaccine_statewise.csv')
[4]
df.head()

[5]
df.tail()

[6]
df.shape
(16850, 9)
[7]
df.columns
Index(['Sno', 'Date', 'Time', 'State/UnionTerritory',
       'ConfirmedIndianNational', 'ConfirmedForeignNational', 'Cured',
       'Deaths', 'Confirmed'],
      dtype='object')
[8]
df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 16850 entries, 0 to 16849
Data columns (total 9 columns):
 #   Column                    Non-Null Count  Dtype 
---  ------                    --------------  ----- 
 0   Sno                       16850 non-null  int64 
 1   Date                      16850 non-null  object
 2   Time                      16850 non-null  object
 3   State/UnionTerritory      16850 non-null  object
 4   ConfirmedIndianNational   16850 non-null  object
 5   ConfirmedForeignNational  16850 non-null  object
 6   Cured                     16850 non-null  int64 
 7   Deaths                    16850 non-null  int64 
 8   Confirmed                 16850 non-null  int64 
dtypes: int64(4), object(5)
memory usage: 1.2+ MB

[9]
##Drop the less important columns
df.drop(["Sno", "Time", "ConfirmedIndianNational", "ConfirmedForeignNational"], inplace=True,axis=1)
[10]
df.head()

[11]
## Change the datatype of 'Date'
df['Date']= pd.to_datetime(df['Date'], format='%Y-%m-%d')
[12]
df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 16850 entries, 0 to 16849
Data columns (total 5 columns):
 #   Column                Non-Null Count  Dtype         
---  ------                --------------  -----         
 0   Date                  16850 non-null  datetime64[ns]
 1   State/UnionTerritory  16850 non-null  object        
 2   Cured                 16850 non-null  int64         
 3   Deaths                16850 non-null  int64         
 4   Confirmed             16850 non-null  int64         
dtypes: datetime64[ns](1), int64(3), object(1)
memory usage: 658.3+ KB

[13]
## Active cases
df['Active_cases']= df['Confirmed']-(df['Cured']+df['Deaths'])
[14]
df.head()

[17]
## Statewise analysis

statewise=pd.pivot_table(df, values=["Confirmed", "Active_cases", "Deaths", "Cured"], index="State/UnionTerritory", aggfunc=max)
[21]
statewise['Recovery Rate']=statewise['Cured']*100/statewise['Confirmed']
statewise['Mortality Rate']=statewise['Deaths']*100/statewise['Confirmed']
statewise = statewise.sort_values(by="Recovery Rate", ascending=False)
statewise.style.background_gradient(cmap="YlOrRd")

[24]
## Print the top 10 active cases

top_10_active_states = df.groupby(by='State/UnionTerritory').max()[['Active_cases', 'Date']].sort_values(by="Active_cases", ascending=False).reset_index()
[26]
top_10_active_states[:10]

[28]
plt.figure(figsize=(15,8))
sns.barplot(data=top_10_active_states[:10], y="Active_cases", x="State/UnionTerritory")
<AxesSubplot:xlabel='State/UnionTerritory', ylabel='Active_cases'>


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




