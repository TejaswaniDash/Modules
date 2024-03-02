"""
library is actually the module

https://docs.python.org/3/library/

we don't use the module itself, we use the function present in the module
"""
#the first for most thing is to import module
#demonstrate the use of math module
import math
#create class

class ModulesDemo():
#let's create a method

    def builtin_modules(self):
        print(math.sqrt(100))

#object the class
m= ModulesDemo()
m.builtin_modules()

print("*"*40)

"""
when you import the complete module called math, 
all the functions available in math are gonna just be pulled up into the code, 
and it's just gonna take a lot of memory and a lot of processing for the computer. 
So what's usually preferred is, 
unless you need pretty much all the methods, o
r maybe 50% of the methods for that particular module, 
then what you can do is you can just say, 'from', and 'math', 
so 'from math import', and you guys can just say 'sqrt',
"""

import math
from math import sqrt

class ModulesDemo():


    def builtin_modules(self):
        print(sqrt(100))

#object the class
m= ModulesDemo()
m.builtin_modules()

print("*"*40)

"""
CREATE YOUR OWN MODULE
"""

import math
import Modules.car as car #have to mention "as car" to functionalize it
from math import sqrt


class ModulesDemo():


    def builtin_modules(self):
        print(math.sqrt(100))
        print(sqrt(100))

    def car_description(self):
        make ="bmw"
        model = "5501"
        year = "2016"
        car.info(make, model, year)

#object the class
m= ModulesDemo()
#m.builtin_modules()
m.car_description()

print("*"*40)

#Another way

import math
#import Modules.car as car #have to mention "as car" to functionalize it
from math import sqrt
from Modules import car


class ModulesDemo():


    def builtin_modules(self):
        print(math.sqrt(100))
        print(sqrt(100))

    def car_description(self):
        make ="bmw"
        model = "5501"
        year = "2016"
        car.info(make, model, year)

#object the class
m= ModulesDemo()
#m.builtin_modules()
m.car_description()

print("*"*40)

#let's try to import only the function that is needed

import math
#import Modules.car as car #have to mention "as car" to functionalize it
from math import sqrt
#from Modules import car

from Modules.car import info



class ModulesDemo():


    def builtin_modules(self):
        print(math.sqrt(100))
        print(sqrt(100))

    def car_description(self):
        make ="bmw"
        model = "5501"
        year = "2016"
        info(make, model, year)

#object the class
m= ModulesDemo()
#m.builtin_modules()
m.car_description()

print("*"*40)