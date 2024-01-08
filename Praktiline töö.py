#8 Poes
from random import *
from datetime import *
arve_nr=datetime.now() # date.today()
print(arve_nr)
tsekk="Arve: "+str(arve_nr)+"\nToode Hind Kogus Summa\n"
summa=0
toode="Piim"
hind=randint(50,150)/100
v=input("Toode:"+toode+" Hind:"+str(hind)+ "\nKas tahad osta?").lower()
if v=="jah":
    mitu=int(input("Mitu?"))
    tsekk+=toode+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"\n"
    summa+=mitu*hind
toode="Saia"
hind=randint(20,300)/100
v=input("Toode:"+toode+" Hind:"+str(hind)+ "\nKas tahad osta?").lower()
if v=="jah":
    mitu=int(input("Mitu?"))
    tsekk+=toode+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"\n"
    summa+=mitu*hind
toode="Leib"
hind=randint(50,257)/100
v=input("Toode:"+toode+" Hind:"+str(hind)+ "\nKas tahad osta?").lower()
if v=="jah":
    mitu=int(input("Mitu?"))
    tsekk+=toode+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"\n"
    summa+mitu*hind
toode="Kommid"
hind=randint(40,1800)/100
v=input("Toode:"+toode+" Hind:"+str(hind)+ "\nKas tahad osta?").lower()
if v=="jah":
    mitu=int(input("Mitu?"))
    tsekk+=toode+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"\n"
    summa+=mitu*hind
tsekk+="Kokku maksta: "+str(summa)
print(tsekk)




#7 Inimese pikkus ja sugu
sugu=input("Kas sa oled mees vai naine?").lower()
if sugu=="naine" or sugu=="n":
    l1=155
    l2=170
    l3=255
elif sugu=="mees" or sugu=="m":
    l1=160
    l2=180
    l3=255
else:
    l1=0
    print("Viga")
if l1!=0: #l1==155 or l1==160
    try:
        pikkus=int(input("Sisesta oma pikkus: "))
        if pikkus>29 and pikkus<l1: #100
            vastus="lühike"
        elif pikkus>=l1 and pikkus<l2: #165
            vastus="keskmine"
        elif pikkus>=l2 and pikkus<=l3: #200
            vastus="pikk"
        else:                             #-10, 300
            vastus="tundmatu"
        print("Sinu pikkus on {0}".format(vastus))
    except :
        print("Vale andmete formaat!")





#6 Inimese pikkus
try:
    pikkus=int(input("Sisesta oma pikkus: "))
    if pikkus>29 and pikkus<155: #100
        vastus="lühike"
    elif pikkus>=155 and pikkus<170: #165
        vastus="keskmine"
    elif pikkus>=170 and pikkus<=255: #200
        vastus="pikk"
    else:                             #-10, 300
        vastus="tundmatu"
    print("Sinu pikkus on {0}".format(vastus))
except :
    print("Vale andmete formaat!")





#5
try:
    t=float(input("Mis on ruumi temperatuur?"))
    if t>18:
       print(str(t))
    else:
        print("See on külm")
except:
    print("Viga")





#4
try:
    hind=float(input("Hind:"))
    if hind>=700:
        hind*=0.7
    print(hind)
except :
    print("Viga")





#3
try:
    pikkus=float(input("Pikkus:"))
    try:
        laius=float(input("Laius:"))
        S=pikkus*laius
        print("Pindala võrdub",S)
        soov=input("Kas tahad remondi teha?").lower() #jah, Jah ,JAH -> upper()->JAH
        if soov=="jah" or soov=="да":
            try:
                hind=float(input("Ruurmeetri hind: "))
                summa=hind*S
                print("Remondi summa on ", summa)
            except :
                print("Viga")
        else:
            print("Head aega")
    except :
        print("Viga")
except :
    print("Viga")





#2
eesnimi1=input("Mis on 1. nimi?").capitalize()   #"Julia" "Kolja"
eesnimi2=input("Mis on 2. nimi?").capitalize()
if (eesnimi1=="Julia" and eesnimi2=="Kolja") or (eesnimi1=="Kolja" and eesnimi2=="Julia"):
    print("Need on pinginaabrid")
else:
    print("Rühmakaaslased")
if(eesnimi1!=eesnimi2) and eesnimi1 and eesnimi2 in ["Julia", "Kolja"] or eesnimi1 and eesnimi2 in ["Karina", "Egor"]:
    print("Need on pinginaabrid")
else:
    print("Rühmakaaslased")




#1
eesnimi=input("Mis on sinu nimi?").capitalize() #"Juku"
if eesnimi=="Juku":
    try:
        vanus=int(input("Kui vana sa oled?"))
        print("Jukule ostame ", end="")
        if 0<vanus<6:
            print("tasuta pilet")
        elif 6<=vanus<14:
            print("lastepilet")
        elif 14<=vanus<65:
            print("täispilet")
        elif 65<=vanus<=100:
            print("sooduspilet")
        else:
            print("Mitte midagi. Viga andmetega!")
    except :
        print("Int andmetüüp on vaja kasutada!")
else:
    print("Mine ise kinno!")