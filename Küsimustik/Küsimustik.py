from MinuOmaMoodul import *

kasutajad=["Julia"]
paroolid=["Postu"]
print("1-soorita test\n2-logi administraatorina sisse")
vastus=int(input("Sisestage arv "))
if vastus==1:
    print("Soorita test")
elif vastus==2:
    print("Administraator")
    autoriseerimine(kasutajad,paroolid)

##kus_vas={}

#    küsimused, vastused=loe_ankeet("Ankeet.txt")
#    print(küsimused)
#    print(vastused)
#    for i in range(len(küsimused)):
#        print(f"{i+1}. Küsimus on: "+küsimused[i]+" vastus on: "+vastused[i])
