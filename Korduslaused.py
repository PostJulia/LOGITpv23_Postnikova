from random import *
from datetime import *
#3
k=0
while True:
    k+=1
    a=randint(1,50)
    b=randint(1,50)
    p=0
    while p!=3:
        p+=1
        v=int(input("Millega võrdub {0}+{1}= ".format(a,b)))
        if v==a+b:
            print("Tubli!")
            break
        else:
            print("Mõtle veel!")
    print("{0}+{1}={2}".format(a,b,a+b))
        
    if k==5:break












#2 summa 10 arvud
summa=0
for i in range(10):
    arv=float(input("Sisesta arv: "))
    summa+=arv
print(summa)

summa=0
i=0
while True:
    i+=1
    arv=float(input("Sisesta arv: "))
    summa+=arv
    if i==10: break
print(summa)






#1 Siim
nimi=input("Mis on sinu nimi?").capitalize()
mitu=int(input("Mitu korda tervistada?"))
for i in range(1,mitu+1):
    print("Ole tervitatud, "+nimi+", "+str(i)+". korda.")








#0
print("1. variandt -while True-")
while True:
    v=input("Anna mulle raha!").lower()
    if v=="hästi":break
print("2. variandt -while tingimusega-")
v=""
while v!="hästi":
    v=input("Anna mulle raha!").lower()
print("3. variandt -for-")
kusimus=["Anna mulle raha!","Rohkem!"]
vastma=["Hästi","Okei"]
for i in range(2):
    print(kusimus[i]+"-"+vastma[i])







#Komm
print("1. variandt -while True-")
while True:
    v=input("Tahan komme!").lower()
    if v=="komm": break

print("2. variandt -while tingimusega-")
v=""
while v!="komm":
     v=input("Tahan komme!").lower()




#Nädala päevad
paevad=["Esmaspäev","Teisipäev","Kolmapäev","Neljapäev","Reede","Laupäev","Pühapäev"]
tunnid=["8 tundi","9 tundi","4 tundi","9 tundi","6 tundi","tunde pole","tunde pole"]
for i in range(7):
    print(paevad[i]+"-"+tunnid[i])

#8 Poes korduslausega
arve_nr=datetime.now() # date.today()
print(arve_nr)
tsekk="Arve: "+str(arve_nr)+"\nToode Hind Kogus Summa\n"
summa=0
tooded=["Piim","Leib","Komm"] #index 0-1-2
for i in range(3): #i=0,i=1,i=2
    toode=tooded[i]
    hind=randint(50,150)/100
    v=input("Toode:"+toode+" Hind:"+str(hind)+ "\nKas tahad osta?").lower()
    if v=="jah":
        mitu=int(input("Mitu?"))
        tsekk+=toode+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"\n"
        summa+=mitu*hind
        
tsekk+="Kokku maksta: "+str(summa)
print(tsekk)
    
