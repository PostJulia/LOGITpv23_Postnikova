print("Tere! Olen sinu uus sõber - Python!")
nimi = input("Mis on sinu nimi?: ").capitalize()
print(nimi + ", oi kui ilus nimi!")
vastus = input(nimi + "! Kas leian Sinu keha indeksi? 0-ei, 1-jah => ")
if vastus == "0":
    if vastus == "1":
   try:
       pikkus = int(input("Sisesta oma pikkus: "))
       mass = float(input("Sisesta oma kaal: "))
       indeks = mass/(0.01 * pikkus)**2
       print(nimi + ", Sinu keha indeks on: "+ str(indeks))
        if indeks < 16:
           print("Tervisele ohtlik alakaal")
        elif 16 <= indeks < 19:
           print("Alakaal")
        elif 19 <= indeks < 25:
           print("Normaalkaal")
        elif 25 <= indeks < 30:
           print("Ülekaal")
        elif 30 <= indeks < 35:
           print("Rasvumine")
        elif 35 <= indeks < 40:
           print("Tugev rasvumine")
        else:
           print("Tervisele ohtlik rasvumine")
    else:
        print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")
else:
    print("Kahju! See on väga kasulik info!")




















#print("Tere! Olen sinu uus sõber - Python!")
#nimi=input("Mis on sinu nimi? ").capitalize()
#print(nimi,", oi kui ilus nimi!")
#print(nimi,"! Kas leian Sinu keha indeksi? 0-ei, 1-jah => ")
#vastus=float(input("Vastus: "))
#try:
#    if vastus.isalpha() and (vastus.lower()=="0" or vastus.lower()=="1"):
#        if vastus.lower()=="0":
#            print("Kahju! See on väga kasulik info!")
#        else:
            
#except :
#    print




















#from random import *
#from datetime import *
#a=10        #int
#b=2.3       #float
#c="programma" #str
#d="1.1"    #str
#print(b.is_integer()) #False "11111" #False "1.1"
#print(c.isalpha()) #True "11111" #True "1.1"
#print(d.isalpha()) #False "11111" #False "1.1"
#print(d.isnumeric()) #True "11111" #False "1.1"
#print(d.isdigit()) #True "11111" #False "1.1"
#print(d.isdecimal()) #True "11111" #False "1.1"











#13 Jalgpalli meeskond
try:
    gender=input("Sugu: ")
    if gender.isalpha() and (gender.lower()=="naine" or gender.lower()=="mees"):
        if gender.lower()=="naine":
            print("Ei soobi")
        else:
            try:
                age=int(input("Vanus: "))
                if 16<=age<=18:
                    print("Oled meeskonnas!")
                else:
                    print("Vanus ei soobi!")
            except :
                print("Vale vanus! Viga andmetüübiga!")
    else:
        print("Sisesta õige tekst!")
except :
    print("Viga andmetüübiga!")





#12 Müük
try:
    hind = float(input("Sisesta toote hind: "))
    if hind <0:
        print("Hind ei saa olla negatiivne!")
    elif hind<=10:
        soodustus = hind * 0.1
        okonnelik_hind = hind - soodustus
        print("Lõplik hind on", okonnelik_hind, "€")
    else: 
        soodustus = hind * 0.2
        okonnelik_hind = hind - soodustus
        print("Lõplik hind on", okonnelik_hind, "€")
except:
    print("Palun sisestage teine ​​number!")





#10
from math import *
try:
    n1=float(input("Sisestage esimene number: "))
    n2=float(input("Sisestage teine ​​number: "))
except :
    pass










#9
try:
    s1=float(input("Sisestage ruudu esimese külje pikkus: "))
    s2=float(input("Sisestage ruudu teise külje pikkus: "))
    if s1==s2:
        print("See on ruut!")
    else:
        print("See ei ole ruut!")
except :
    print("Kuskil on viga, vaata tüüpi, nagu sa andmed määrasid!")





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