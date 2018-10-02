from collections import namedtuple

class Duck():
    def __init__(self,input_name):
        self.__name=input_name
    def get_name(self):
        print('inside the getter')
        return self.__name
    def set_name(self,input_name):
        print('inside the setter')
        self.__name = input_name
    name = property(get_name,set_name)

fowl = Duck('Howard')
print(fowl.name)

fowl.name = 'Daffy'
print(fowl.name)
print(fowl._Duck__name)


class Circle():
    def __init__(self,radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius
c = Circle(5)
print(c.radius)
print(c.diameter)
c.radius = 8
print(c.radius)
print(c.diameter)

class Word():
    def __init__(self,text):
        self.text = text

    def __eq__(self,word2):
        return self.text.lower() == word2.text.lower()

    def __add__(self, other):
        return self.text + other.text + other.text


first = Word('ha')
second = Word('HA')
third = Word('eh')

num1 = Word(1)
num2 = Word(2)
print(num1+num2)

print(first == second)

print(str(1111111111))

Foo1 = namedtuple('Foo', ('bar', 'bas', 'baz'))

foo = Foo1(1,2,3)
for item in foo:
    print(item)

print(Foo1)

print("---------6-1---------")
class Thing():
    pass

example = Thing
print(example)

print("---------6-2---------")
class Things2():
    def __init__(self,letters):
        self.letters = letters

letter = Things2("abc")
print(letter.letters)

print("---------6-3---------")

print("---------6-4---------")
class Element():
    def __init__(self,name,symbol,number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return "name:"+self.name+", symbol:"+self.symbol+", number:"+self.number

#one = Element('Hydrogen','H',"1")

print("---------6-5---------")
Hydro_dict = {'name':"Hydrogen",'symbol':'H','number':'1'}
hydrogen = Element(Hydro_dict.get('name'),Hydro_dict.get('symbol'),Hydro_dict.get('number'))

print("---------6-6---------")
#Element.dump(hydrogen)
print("---------6-7---------")
print(hydrogen)

print("---------6-8---------")

print("---------6-9---------")
class Bear():
    def eats(self):
        return "'berris'(Bear)"
class rabbits():
    def eats(self):
        return "'clover'(rabbits)"
class Octhope():
    def eats(self):
        return "'campers'(Octhope)"

bear = Bear()
usagi = rabbits()
octhope = Octhope()

print(bear.eats())
print(usagi.eats())
print(octhope.eats())

print("---------6-10---------")









