import report
import sys
#from report import get_description as do_it

#print(do_it())

for place in sys.path:
    print(place)

periodic_table={'Hydrogen':1,'helium':2}
print(periodic_table)

carbon = periodic_table.setdefault('carbon',12)
print(periodic_table)

from collections import defaultdict
def_int_table = defaultdict(int)

def_int_table['haruo']=1
def_int_table['yuko']
print(def_int_table)

from collections import Counter
breakfast = ['spam','spam','eggs']
lunch=['meat','fish','eggs']
breakfastcount = Counter(breakfast)
lunchcount = Counter(lunch)
print(breakfastcount)
print(breakfastcount+breakfastcount)
print(breakfastcount-lunchcount)


from collections import OrderedDict
quotes = OrderedDict([
    ('Moe','A wise guy'),
    ('Larry','Ow'),
    ('Curly','Nyuk Nyuk')
])
print(quotes)
quotes2 = {
    ('Moe','A wise guy'),
    ('Larry','Ow'),
    ('Curly','Nyuk Nyuk')
}
print(quotes2)

import itertools
for item in itertools.chain(['spam','spam','eggs'],['spam2','spam2','eggs'],['spam','spam','eggs']):
    print(item)

for item2 in itertools.accumulate([1,2,3,4]):
    print(item2)

from pprint import pprint
pprint(quotes)

#5-1
import zoo
zoo.hours()


#5-2
import zoo as menageriue
menageriue.hours()

#5-3
from zoo import hours
hours()

#5-4
from zoo import hours as info
info()

#5-5

plain ={
    "dog": "chien",
    "cat": "chat",
    "walrus": "morse"
}
print(plain)

fancy = OrderedDict([
    ('dog','chien'),
    ('cat','chat'),
    ('walrus','morse')
])
print(fancy)

#5-7
dict_of_lists = defaultdict(list)
dict_of_lists["a"]="somethin for a"
print(dict_of_lists['a'])