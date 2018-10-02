disaster = False

#if disaster:
#    print("yeah")
#else:
#    print("OMG")


#color = "blue"
#if color == "red":
#    print("nero")
#elif color   ==     "blue":
#    print("arthor")
#else:
#    print("who")

#count = 1
#while count <= 5:
#    print(count)
#    count += 1

#while True:
#    stuff = input("String to Capitalize [type q to quit]")
#    if stuff == "q":
#        print("input finish")
#        break
#    print(stuff.capitalize())

rabbits = ['parple1','gold4','red5']
pilots = ['hikasa','geek','hero']
#rabbits = []

for rabbit,pirot in zip(rabbits,pilots):
    print(rabbit,pirot)
    #break
else:
    print("no rabbits")

def do_nothing():
    pass

def make_a_sound():
    print("quack")

make_a_sound()

def edit_story(words,func):
    for word in words:
        print(func(word))

stairs=['one','two','three']

edit_story(stairs, lambda test: test.upper())


def count_up():
    x = 0
    while 1==1:
        yield x
        x += 1

y = count_up()
print(y)
for i in y:
    print(i)
    if i == 5:
        break

for i in y:
    print(i)
    if i == 20:
        break

def doc_it(func):
    def new_func(*args,**kward):
        print('fuck',func.__name__)
        print('fuck',args)
        result = func(*args,**kward)
        print('fuck',result)
        return result
    return new_func

@doc_it
def add_ints(a,b):
    return a+b



add_ints(3,5)

#4-1

#guess_me=7
#if guess_me < 7:
#    print('too low')
#elif guess_me>7:
#    print('too high')
#elif guess_me==7:
#    print('just light')

#4-2

guess_me = 7
start = 1
while guess_me>=start:
    if start < guess_me:
        print('too low')
    elif start==guess_me:
        print('found it')
    elif start>guess_me:
        print('Oops')
        break
    start +=1

#4-3
numlist=[3,2,1,0]
for i in numlist:
    print(i)

#4-4

numberlist = [number for number in range(10)if number%2==0 ]
print(numberlist)

#4-5
squares = {number :number *number for number in range(10)}
print(squares)
#4-6
odd = {number1 for number1 in range(10) if number1 %2==1 }
print (odd)
#4-7

fuckgene = (number for number in range(10))
for number in fuckgene:
    print('GOT ',number)

for number in fuckgene:
    print('GOT ',number)

#4-8
def good():
    return ['Harry','Ron','Hermione']

print(good())

#4-9
def  get_odd():
    number = 1
    while number <10:
        yield number
        number +=2

fuckgetodd = get_odd()
for x in fuckgetodd:
    print(x)

#4-10
def test(func):
    def new_func(*args,**kward):
        print('start')
        print(func(*args,**kward))
        print('end')
    return new_func

@test
def good2():
    return ['Harry','Ron','Hermione']

good2()

#4-11
class OopsException(Exception):
    pass

words=["1","2","3"]
try:
    raise OopsException("test")
except OopsException as exc:
    print(exc)


#4-12
titles =['hobits','Fate']
plots = ['load of the ring','typemoon']
movies = dict(zip(titles,plots))
print(movies)