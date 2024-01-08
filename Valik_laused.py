from random import *
vanus=randint(15,65)
print(vanus)
if vanus>=18:
    print("Täiskasvatud inimene. Vanemad ei saa kontrollida tulemusi")
else:
    print("Vanemad kontrollivad lapsi")



a=randint(-1000,1000)
print(a)
if a%3==0:
    print("{0} jagatakse kolmega".format(a))
else:
    print("Ei saa jagada kolmega")

hinne=input("Mis hinne sa täna sai?") #"A" "MA" "X" "5" "4" "3"
if hinne==int("5") or hinne=="A": #hinne==5
    print("Super!")
elif hinne=="4":
    print("Hea hinne!")
elif hinne=="3":
    print("Rahuldav!")
elif hinne=="2" or hinne=="1" or hinne=="MA":
    print("Halb!")
elif hinne=="X":
    print("On vaja töö soritada")
else:
    print("Ma ei tea, mis hinne see on!")



arv=int(input("Sisesta arv: "))
if arv==13:
    arv=77
print(arv)  

if arv>0:
    print("Positiivne arv")
elif arv<0:
    print("Negatiivne arv")
else:
    print("0")