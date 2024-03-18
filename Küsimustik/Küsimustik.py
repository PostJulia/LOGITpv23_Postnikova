from MinuOmaMoodul import *

kasutajad=["Julia"]
paroolid=["Postu"]
kus_vas=loe("Ankeet.txt")

print("1-soorita test\n2-logi administraatorina sisse")
vastus=int(input("Sisestage arv "))

if vastus==1:
    print("Soorita test")
    osaleja_nimi=input("Palun sisestage oma nimi: ")
    N=int(input("Mitu küsimust soovid esitada? "))
    punktid=küsimus_vastus(kus_vas, N)
    salvesta(osaleja_nimi, punktid, "Oiged.txt", "Valed.txt")
    print("\nEdukalt läbinud osalejad:")
    oiged_fail=open("oiged.txt",'r',encoding='utf-8')
    print(oiged_fail.read())
    oiged_fail.close()
    print("\nEbaõnnestunud osalejad:")
    valed_fail=open("valed.txt",'r',encoding='utf-8')
    print(valed_fail.read())
    valed_fail.close()

elif vastus==2:
    print("Administraator")
    autoriseerimine(kasutajad,paroolid)
    uued={}
    uute_arv=int(input("Mitu uut küsimust soovid lisada? "))
    for i in range(uute_arv):
        küsimus=input("Sisestage uus küsimus: ")
        vastus=input("Sisestage vastus uuele küsimusele: ")
        uued[küsimus]=vastus
    lisa(uued,"Ankeet.txt")

#kus_vas={}

#    küsimused, vastused=loe_ankeet("Ankeet.txt")
#    print(küsimused)
#    print(vastused)
#    for i in range(len(küsimused)):
#        print(f"{i+1}. Küsimus on: "+küsimused[i]+" vastus on: "+vastused[i])