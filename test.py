#####リスト操作

datelist = ['monday','tuesday','Thursday','friday','saturday',]
timelist =['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
numlist=[2,3,4,5,6,1]

#datelist.extend('sunday')
otherdate=['sunday']
datelist.extend(otherdate)
datelist.insert(2,'wednesday')

del datelist[0]
datelist.remove('sunday')
may_firstweek= [datelist,timelist]
numlist.sort()
##################################

##辞書操作
athor_list={
    "blueking":{"アーサー","エクスカリバー"},
    "blackking":{"アーサー","オルタ","エクスカリバー"},
    "redking":{"ネロ"},
    "kinglily":{"アーサー","カリバーン"}
}
#

lance_athor_list={
    "lanceking":{"アーサー","ロンゴミニアド"},
    "blacklanceking":{"アーサー","オルタ","ロンゴミニアド"}
}
#for name ,contents in athor_list.items():
#    if 'アーサー' in contents and not contents &{'カリバーン'}:
#        print(name)

blue=athor_list['blueking']
black=athor_list['blackking']

#print(black<blue)

##################################



#######復習課題3章
#3-1]
year_list = [1985,1986,1987,1988,1989,1990]
print(year_list)

#3-2
print(year_list[3])

#3-3
print(year_list[-1])

#3-4
things=["mozzarella","cinderella","salmonella"]

#3-5
things[1] =things[1].title()
print(things)

#3-6
things[0]= things[0].upper()
print(things)

#3-7
del things[2]
print(things)

#3-8
surprise=["Groucho","Chiro","Harpo"]

#3-9
surprise[2]=surprise[2].lower()
surprise[2]=surprise[2][::-1]
surprise[2]=surprise[2].title()

print(surprise)

#3-10
e2f ={
    "dog": "chien",
    "cat": "chat",
    "walrus": "morse"
}
print(e2f)

#3-11
print(e2f.get('walrus'))

#3-12
for fuckenglish,fuckfrench in e2f.items():
    print(fuckenglish,fuckfrench)

