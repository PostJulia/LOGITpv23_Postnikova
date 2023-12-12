#10
from random import*
from math import*
try:
    P=int(input("Sõbrade kogus: "))
except :
    print("Kogus on täisarv")
hind=12.90
hind*=hind*1.1 #hind+10%
print("Igaüks maksab", hind/P)








#9
from random import*
from math import*
try:
    a=float(input("a: "))
    try:
        b=float(input("b: "))
        try:
            c=float(input("c: "))
            #OK
            P=a+b+c
            print("Ümbermõõt: ",P)
        except :
            print("Viga c muutujaga!")
    except :
        print("Viga b muutujaga!")
except :
    print("Viga a muutujaga!")





#8
from random import*
from math import*
print("@..@".center(10," "))
print("(----)".center(10," "))
print("( \__/ )".center(10," "))
print('^^ "" ^^'.center(10," "))





#7
from random import*
from math import*
try:
    min_=int(input("Min: "))
except :
    print("On vaja täisarv kasutada!")
try:
    max_=int(input("Max: "))
except :
    print("Viga max_ muutujaga")
a1=randint(min_,max_)
a2=randint(min_,max_)
a3=randint(min_,max_)
a4=randint(min_,max_)
a5=randint(min_,max_)
keskmine=(a1+a2+a3+a4+a5)/5
print("Arvud: {0},{1},{2},{3},{4}. Aritmetiline keskmine on: {5}".format(a1,a2,a3,a4,a5,keskmine))





#6
from random import*
from math import*
try:
    aeg = float(input("Mitu tundi kulus sõiduks? "))
    try:
        teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
        kiirus = teepikkus/aeg
        print("Sinu kiirus oli " + str(kiirus) + " km/h")
    except :
        print("Viga andmetaga!")
except :
    print("On vaja ainult numbreid sisestada!")





#5
from random import *
from math import *
a=float(input("pikkus: "))
b=float(input("laius: "))
d=sqrt(a**2+b**2)
print("Diagonaal=",d,"m")





#4
from random import *
from math import *
u=float(input("Ümbermõtt: ")) #L=pi*2*r=pi*d
d=round(u/pi,2)
print("Läbimõõt =",d)





#3
from random import *
kokku=randint(1,100)
print("Laual peal on",kokku,"kommid. Mitu tahad süüa?")
kommid=int(input())
kokku-=kommid
print("Nüüd kokku on",kokku)




#2
vanus=18
eesnimi="Jaak"
pikkus=16.5
kas_käib_koolis=True

print("Muutuja vanus=",vanus,"on", type(vanus))
print("Muutuja eesnimi=",eesnimi,"on", type(eesnimi))
print("Muutuja pikkus=",pikkus,"on", type(pikkus))
print("Muutuja kas_käib_koolis=",kas_käib_koolis,"on", type(kas_käib_koolis))




#Калькулятор
arv1=float(input("Arv1: "))
t=input("Tehe: ")
arv2=float(input("Arv2: "))
vastus=eval(str(arv1)+t+str(arv2))
print(str(arv1)+t+str(arv2)+"="+str(vastus))
print(arv1,t,arv2,"=",vastus,sep="")
print("{0}{1}{2}={3}".format(arv1,t,arv2,vastus))




#1
print("Tere maailm!".center(75,"-"))
nimi=input("Mis on sinu nimi? ").capitalize() #python->Python
print("Tere "+nimi+"!")
print("Tere",nimi+"!")
print("Tere {0}!".format(nimi))
vanus=int(input("Kui vana sa oled?"))    #"21"!=21
print("Tere {0}! Sa oled {1} aastat vana".format(nimi,vanus))
print("Muutuja nimi=",nimi,type(nimi))
print("Muutuja vanus=",vanus,type(vanus))