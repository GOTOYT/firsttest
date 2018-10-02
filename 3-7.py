def unicord_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print ('value="%s", name="%s",value2="%s"'%(value,name,value2))

unicord_test("\u00e9")

print("caf\u00e9")

snowman = "\u2603"
print(snowman + " ,len:" +str(len(snowman)))

ds = snowman.encode('utf-8')
print(ds)
print(len(ds))


dsa = snowman.encode('ascii','replace')
print(dsa)
print(len(dsa))


print("---------------------7.1.1.14------------------------")

place = 'caf\u00e9'
print(place)
print(type(place))

place_bytes = place.encode('utf-8')
print(place_bytes)
print(type(place_bytes))

place = place_bytes.decode('utf-8')
print(place)
print(type(place))

1
print("---------------------7.1.2.1------------------------")

print('%x'%16)

print("%10d %10f %10s"   %(42 ,7.03 ,"Cheese"))

print("---------------------7.1.2.2------------------------")
print('{2} {0} {1}'.format(42 ,7.03 ,"Cheese"))

n=42
f=7.03
s="String"

print('{0} {1} {2}'.format(n,f,s))

d = {'n':42,'f':7.03}

print('{0[n]:!^20d}{0[f]:?^20f} '.format(d,"other"))

ss='{0[n]:!^20d}{0[f]:?^20f} '.format(d,"other")

print(ss)
print(type(ss))

print("---------------------7.1.3------------------------")
import re
result1 = re.match('......Frank','Youhg Frankenstein')
result2 = re.match('You','Youhg Frankenstein')
if result1:
    print(result1.group())
else:
    print("nothing")
if result2:
    print(result2.group())


m = re.findall('..n',"Frankenstein")
print(m)

m = re.split('n',"Frankenstein")
print(m)

m = re.sub('n','?',"Frankenstein")
print(m)

import string
printable = string.printable
print(len(printable))
print(printable)

print(re.findall("\d",printable))
print(re.findall("\D",printable))
print(re.findall("\w",printable))
print(re.findall("\s",printable))


m = re.findall("\d",printable)


print("---------------------7.2------------------------")

blist = [1,2,3,255]
the_bytes = bytes(blist)
print(the_bytes)

the_byte_array= bytearray(blist)
print(the_byte_array)

the_byte_array[0]=255
print(the_byte_array)

the_bytes2 = bytes(range(0,256))
the_byte_array = bytearray(range(0,256))


print(the_bytes2)
print(the_byte_array)

print("---------------------7.2.2--writers-masturbation----------------------")
#突然画像を取扱始めたが、意図不明。エンディアンの説明をしたいようだが情報不足。バイナリ変換の実用方法はググろう。
print(0x9a)

print("---------------------7-1------------------------")
mystery = '\U0001f4a9'
print(mystery)
unicord_test(mystery)

print("---------------------7-2------------------------")
mystery
pop_bytes = mystery.encode('utf-8')
print(pop_bytes)

print("---------------------7-3------------------------")
pop_string = pop_bytes.decode('utf-8')
print(pop_string)

print("---------------------7-4------------------------")
print('{0} {1} {2}'.format("roast" "beef","ham","clam"))

print("---------------------7-5------------------------")
letter = '''Dear {salutation} {name},
... 
... Thank you for your letter. We are sorry that our {product} {verbed} in your {room}. Please note that it should never be used in a {room}, especially near any {animals}.
... 
... Send us your receipt and {amount} for shipping and handling. We will send you another {product} that, in our tests, is {percent}% less likely to have {verbed}.
... 
... Thank you for your support.
... 
... Sincerely,
... {spokesman}
... {job_title}
... '''

print(letter)

response = {}
response['salutation'] = 'Ms.'
response['name'] = 'Suzuki'
response['product'] = 'TV set'
response['verbed'] = 'broken'
response['room'] = 'bathroom'
response['animals'] = 'tigers'
response['amount'] = 1000
response['percent'] = 0.2
response['spokesman'] = 'Bill Blackgates'
response['job_title'] = 'Chairman'
print(response)

print(letter.format(**response))