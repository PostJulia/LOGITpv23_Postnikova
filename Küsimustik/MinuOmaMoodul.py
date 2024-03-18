from string import *
from time import sleep
from string import *
from random import *
def loe_ankeet(fail:str)->any:
    fail=open(fail,"r",encoding="utf-8")
    kus=[]
    vas=[]
    #kus_vas={}
    for line in fail:
        n=line.find(":")# , - разделитель
        kus.append(line[0:n].strip())
        vas.append(line[n+1:len(line)].strip())

        #k.v=line.strip().split(":")
        #kus_vas[k]=v

    fail.close()
    return kus,vas #,kus_vas

def autoriseerimine(kasutajad:list, paroolid:list):
    kasutajad={"Julia": "Postu"}
    while True:
        kasutaja=input("Sisestage kasutajanimi: ")
        parool=input("Sisestage parool: ")
        if kasutajad.get(kasutaja)==parool:
            print("Sisselogimine õnnestus!")
            return kasutaja
        else:
             p=0
             while True:
                 nimi=input("Sisesta kasutajanimi: ")
                 if nimi in kasutajad:
                     while True:
                         parool=input("Sisesta salasõna: ")
                         p+=1
                         try:
                             if kasutajad.index(nimi)==paroolid.index(parool):
                                 print (f"Tere tulemast! {nimi}")
                         except:
                             print("Vale nimi või salasõna!")
                             if p==5:
                                 print("Proovi uuesti 10 sek pärast")
                                 for i in range(10):
                                     sleep(1)
                                     print(f"On jäänud {10-i} sek")
                 else:
                     print("Kasutajat pole")
                     break
    
def loe(Ankeet.txt):
    kus_vas={}
    fail=open(Ankeet.txt, 'r', encoding='utf-8')
    for line in fail:
        küsimus, vastus=line.strip().split(':', 1)
        kus_vas[küsimus.strip()]=vastus.strip()
    fail.close()
    return kus_vas

def lisa(kus_vas, Ankeet.txt):
    fail=open(Ankeet.txt, 'a', encoding='utf-8')
    for küsimus, vastus in kus_vas.items():
        fail.write(f"{küsimus}:{vastus}\n")
    fail.close()

def küsimus_vastus(kus_vas, n):
    punktid=0
    küsimused=random.sample(list(kus_vas.keys()), n)
    for küsimus in küsimused:
        print(küsimus)
        vastus=input("Vastus: ").strip()
        if vastus.lower()==kus_vas[küsimus].lower():
            punktid+=1
    return punktid

def salvesta(osaleja_nimi, punktid, Oiged.txt, Valed.txt):
    if punktid>len(kus_vas)/2:
        oiged=open(Oiged.txt, 'a', encoding='utf-8')
        oiged.write(f"{osaleja_nimi}\n")
        oiged.close()
    else:
        valed=open(Valed.txt, 'a', encoding='utf-8')
        valed.write(f"{osaleja_nimi}\n")
        valed.close()
def autoriseerimine(kasutajad:list,paroolid:list):
    p=0
    while True:
        nimi=input("Sisesta kasutajanimi: ")
        if nimi in kasutajad:
            while True:
                parool=input("Sisesta salasõna: ")
                p+=1
                try:
                    if kasutajad.index(nimi)==paroolid.index(parool):
                        print (f"Tere tulemast! {nimi}")
                        
                except:
                    print("Vale nimi või salasõna!")
                    if p==5:
                        print("Proovi uuesti 10 sek pärast")
                        for i in range(10):
                            sleep(1)
                            print(f"On jäänud {10-i} sek")
        else:
            print("Kasutajat pole")
        break