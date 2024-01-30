#4
g=0
age=1
while g<=100:
    g+=age
    lõpp=age+1
    print("Kingitus ületab 100 dollarit", lõpp ,"sünnipäev")












#3
from random import *
from math import *
#n=randint(1,30)
#h=randint(1,5)
#for j in range(h):
#    for i in range(n):
#        r=sum(h)/n
#    print(r)











#2
n=int(input("Sisestage number n:"))  #Küsime kasutajalt numbrit n
k=int(input("Sisesta astendaja:"))  #Küsime kasutajalt astendajat
for i in range(k+1):
    r=n**i #Siin loeb kood loeb n võimsuseks i ja määrab selle kõik r
    if r<=n**k:
       print(r)
    else:
        break






#1
n=int(input("Sisestage arv vahemikus 1 kuni 9: "))
if n<10:
  for i in range(n):
     if i<n+1:       
        print("-----".center(10," "))
        print("|  O  |".center(10," "))
        print("!  -  !".center(10," "))
        print("-----".center(10," "))
else:        
    print("Viga!")


