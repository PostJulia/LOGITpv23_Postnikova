from string import *
from time import sleep
import random
#def loe_ankeet(fail:str)->any:
#    fail=open(fail,"r",encoding="utf-8")
#    kus=[]
#    vas=[]
#    #kus_vas={}
#    for line in fail:
#        n=line.find(":")# , - разделитель
#        kus.append(line[0:n].strip())
#        vas.append(line[n+1:len(line)].strip())

#        #k.v=line.strip().split(":")
#        #kus_vas[k]=v

#    fail.close()
#    return kus,vas #,kus_vas

def autoriseerimine(kasutajad:list, paroolid:list):
    p=0
    while True:
        kasutaja=input("Sisestage kasutajanimi: ")
        parool=input("Sisestage parool: ")
        if kasutajad.index(kasutaja)==paroolid.index(parool):
            print("Sisselogimine õnnestus!")
            return kasutaja
        else:
            p+=1
            print("Vale nimi või salasõna!")
            if p==5:
                print("Proovi uuesti 10 sek pärast")
                for i in range(10):
                    sleep(1)
                    print(f"On jäänud {10-i} sek")
            else:
                print("Kasutajat pole")
                break
    
def loe(Ankeet:str):
    fail=open(Ankeet,"r",encoding="utf-8")
    kus=[]
    vas=[]
    fail=open(Ankeet, 'r', encoding='utf-8')
    for line in fail:
        n=line.find(":")
        kus.append(line[0:n].strip())
        vas.append(line[n+1:len(line)].strip())
        fail.close()
        return kus,vas

def lisa(kus, Ankeet:str):
    fail=open(Ankeet, 'a', encoding='utf-8')
    for küsimus, vastus in kus.items():
        fail.write(f"{küsimus}:{vastus}\n")
    fail.close()

def küsimus_vastus(kus, N):
    punktid=0
    küsimused=random.sample(list(kus), N>=0)
    for küsimus in küsimused:
        print(küsimus)
        vastus=input("Vastus: ").strip()
        if vastus==:
            punktid+=1
    return punktid
    
def salvesta(osaleja_nimi, punktid, Oiged:str, Valed:str, N):
    if punktid==(N):
        oiged=open(Oiged, 'a', encoding='utf-8')
        oiged.write(f"{osaleja_nimi}\n")
        oiged.close()
    else:
        valed=open(Valed, 'a', encoding='utf-8')
        valed.write(f"{osaleja_nimi}\n")
        valed.close()