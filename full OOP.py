#classes
#create a class with __init__ function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
print(p1.name)
print(p1.age)

#**************************************#

#python code explain inheritance
class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def display(self):
    print(self.name, self.age)
class Student(Person):
  def __init__(self, name, age):
    self.sName = name
    self.sAge = age
    # inheriting the properties of parent class
    super().__init__("amr", age)
  def displayInfo(self):
    print(self.sName, self.sAge)
obj = Student("mn3m", 23)
obj.display()
obj.displayInfo()

#**************************************************#

#python code explain Encapsulation
class Computer:
  def __init__(self):
    self.__maxprice = 900
  def sell(self):
    print("Selling Price: {}".format(self.__maxprice))
  def setMaxPrice(self, price):
    self.__maxprice = price
c = Computer()
c.sell()
c.__maxprice = 1000
c.sell()
c.setMaxPrice(1000)
c.sell()

#***************************************************************#

#python code explain Polymorphism
class Polygon:
  def render(self):
    print("Rendering Polygon...")
class Square(Polygon):
  def render(self):
    print("Rendering Square...")
class Circle(Polygon):
  def render(self):
    print("Rendering Circle...")
s1 = Square()
s1.render()
c1 = Circle()
c1.render()

#**********************************************************#

#python code explain super function
class Animal:
  def __init__(self, name):
    self.name = name
  def speak(self):
    print(f"{self.name} makes a sound")
class Dog(Animal):
  def __init__(self, name, breed):
    super().__init__(name)
    self.breed = breed
  def speak(self):
    super().speak()
    print(f"{self.name} barks")
my_dog = Dog("Buddy", "Golden Retriever")
my_dog.speak()

#*************************************************#

#python code explain getter and setter
class MyClass:
  def __init__(self, value):
    self._my_attribute = value
  def get_attribute(self):
    return self._my_attribute
  def set_attribute(self, new_value):
    if new_value >= 0:
      self._my_attribute = new_value
    else:
      print("Invalid value. Attribute must be non-negative.")
obj = MyClass(42)
current_value = obj.get_attribute()
print("Current value:", current_value)
obj.set_attribute(50)
new_value = obj.get_attribute()
print("New value:", new_value)
obj.set_attribute(-5)

#**********************************************************************#

#python code explain Multiple Inheritance
class Mammal:
  def mammal_info(self):
    print("Mammals can give direct birth.")
class WingedAnimal:
  def winged_animal_info(self):
    print("Winged animals can flap.")
class Bat(Mammal, WingedAnimal):
  pass
b1 = Bat()
b1.mammal_info()
b1.winged_animal_info()

#****************************************************************#

#python code explain Multilevel Inheritance
class SuperClass:
  def super_method(self):
    print("Super Class method called")
class DerivedClass1(SuperClass):
  def derived1_method(self):
    print("Derived class 1 method called")
class DerivedClass2(DerivedClass1):
  def derived2_method(self):
    print("Derived class 2 method called")
d2 = DerivedClass2()
d2.super_method()
d2.derived1_method()
d2.derived2_method()

#**********************************************************#

#python code explain Overriding
class Parent():
  def __init__(self):
    self.value = "Inside Parent"
  def show(self):
    print(self.value)
class Child(Parent):
  def __init__(self):
    self.value = "Inside Child"
  def show(self):
    print(self.value)
obj1 = Parent()
obj2 = Child()
obj1.show()
obj2.show()

#******************************************************#

#code demonstrates the use of abstract classes and abstract methods in Python.
from abc import ABC, abstractmethod
class Polygon(ABC):
	@abstractmethod
	def noofsides(self):
		pass

class Triangle(Polygon):
	def noofsides(self):
		print("I have 3 sides")

class Pentagon(Polygon):
	def noofsides(self):
		print("I have 5 sides")

class Hexagon(Polygon):
	def noofsides(self):
		print("I have 6 sides")

class Quadrilateral(Polygon):
	def noofsides(self):
		print("I have 4 sides")

R = Triangle()
R.noofsides()
K = Quadrilateral()
K.noofsides()
R = Pentagon()
R.noofsides()
K = Hexagon()
K.noofsides()

#******************************************************#

#Exceptions
x = 5
y = "hello"
a = [1,2,3]
try:
    print("Test1")
    print(a[3])
    z = x + y
    print("Test2")
except TypeError:
    print("Error: cannot add an int and a str")
except IndexError:
    print("Error1")
except:
    print("Error2")



