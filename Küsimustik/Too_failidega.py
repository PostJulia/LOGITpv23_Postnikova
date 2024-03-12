from MinuOmaMoodul import *
kus_vas={}

küsimused, vastused=loe_ankeet("Ankeet.txt")
print(küsimused)
print(vastused)
for i in range(len(küsimused)):
    print(f"{i+1}. Küsimus on: "+küsimused[i]+" vastus on: "+vastused[i])




