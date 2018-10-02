class Person():
    def __init__(self,name):
        self.name = name

class MDPerson(Person):
    def __init__(self,name):
        self.name = "Doctor "+name
    def birthday(self):
        print("20151206")

class EMailPerson(Person):
    def __init__(self,name,email):
        super().__init__(name)
        self.email=email

bob = EMailPerson('Bob',"bob@gmail.com")
print(bob.name)
print(bob.email)

hunter = Person('makugirisu')
docter = MDPerson("oruga")

print(hunter.name)
print(docter.name)
docter.birthday()

class Car():
    def exclaim(self):
        print("I am a Car!")

class Yugo(Car):
    def exclaim(self):
        print("I am a Car too!")
    def yugiou(self):
        print("duel!!")

gime_a_car=Car()
gime_a_yugo=Yugo()
gime_a_car.exclaim()
gime_a_yugo.exclaim()
gime_a_yugo.yugiou()