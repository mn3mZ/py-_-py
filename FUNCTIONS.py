#FUNCTIONS
#CREATING AND CALLING FUNCTION
def my_function():
  print("HELLO MN3M")

my_function()

#*********************************************#

#Arguments
def my_function(fname):
  print(fname + " TOP ")

my_function("MOHAMED")
my_function("MN3M")
my_function("MAGDY")

#********************************************#

#FUNCTION WITH FOR LOOP
def loop():
  for x in range(10):
    print (x)
    if x == 3:
      return
loop()

#*******************************************#

#pass function as parameter

def twice(y , x):
    return y(y(x))
def mul(x):
    return x**2
out = twice(mul , 2)
print(out)

#*******************************************#

#define function inside another

def function1(x):
    def function2(y):
        return y + 2
    return 3 * function2(x)
# call the function
a = function1(2)
print (a)


def function2(param):
  print(
    'mn3m 3mk'
  )


b = function2(2.5)
print (b)
#***************************************#

#Local Scope
def myfunc():
  x = 300
  print(x)

myfunc()

#**************************************#

#Global Scope
x = 300

def myfunc():
  print(x)

myfunc()

print(x)

#***************************************#

#global vs local
x = 1
def add_one (x):
    x = x + 1
    # add one to the local x
    return x
# call the function
y = add_one (x)
print(x)
print(y)
def f1():
    global x
    x = x + 1
    return x
def f2():
    return x
def f3():
    x = 5
    return x+1
x = 0
print(f1()) #global
print(f2()) #global
print(f3()) #local

#*************************************#

#Loop Through a List
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#*************************************************************#

#List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#*************************************************************#

#assignment using tubles
t = (1, 2, 3)
x, y, z = t
print (t) # (1, 2,3)
print (y) # 2

#**************************************************#

#Passing functions with arguments to another function in Python
def add(x, y):
  return x + y
def subtract(x, y):
  return x - y
def perform_operation(operation, a, b):
  result = operation(a, b)
  print(f"Result of the operation: {result}")
perform_operation(add, 5, 3)
perform_operation(subtract, 8, 4)

#***********************************************************#
#THE
#END



