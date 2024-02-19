from random import *
from datetime import *
#15
katsed=0
while True:
    vastus=input("Osta elevant ära! Kirjuta 'elevant': ")
    katsed+=1

    if vastus.lower()=='elevant':
        print(f"Õige! Ostsid elevanti ära {katsed} katsega.")
        break
    else:
        print("Vale vastus. Proovi uuesti.")





#14 Korrutustabel
for j in range(1,11):
    for i in range(1,11):
        print(f"{j*i:2}",end=" ")
    print()
   






#13
print("Arv Ruut Kuup")
print()

for i in range(1,11):
    ruut=i**2
    kuup=i**3
    print(f"{i:2} {ruut:2} {kuup:3}")




#12 Pank
algsumma=float(input("Mis summa paneme panka?"))
alg=lõppsumma=algsumma
intress=randint(1,10)
print(f"Paned panka summa, mis võrdub {algsumma}. Intress on {intress}")
aastad=int(input("Mitmeks aastaks?"))
print("Aasta Algsumma Intress Aasta_lõpuks")
for i in range(1, aastad+1):
    intsumma=(algsumma*intress)/100
    lõppsumma=algsumma+intsumma
    print(f"{i} {algsumma} {intsumma} {lõppsumma}")
    algsumma=lõppsumma
print(f"Summa kokku: {lõppsumma} Eur")
print(f"Kasum: {lõppsumma-alg} Eur")




#11
number=randint(1,100)
katsed=3

while katsed>0:
    külaline==int(input("Угадайте число от 1 до 100: "))
    if külaline==number:
        print("Поздравляем, вы угадали число!")
        break
    else:
        katsed-=1
        print(f"Неверно. У вас осталось {katsed} попыток.")
        if katsed==0:
            print(f"Извините, вы использовали всё попытки. Загаданное число было {number}.")
            veelkord=input("Хотите ли угадать?: ").lower()
            if veelkord.lower()=="нет":
                break
            else:
                katsed=3




#10
for arv in range(1,101):
    if arv%5==0:
        print(arv)






#9
korrutamine=["5"]
arv=["1","2","3","4","5","6","7","8","9","10"]
for i in range(10):
    tulemus=int(arv[i])*5
    print(f"{arv[i]}*5={tulemus}")


korrutamine=5

for i in range(1,11):
    tulemus=(i)*5
    print(f"{i}*5={tulemus}")





#8
paaris=0
paaritu=0
for i in range(1,101):
    if i%2==0:
        print(f"{i}-paaris")
        paaris+=1
    else:
        print(f"{i}-paaritu")
        paaritu+=1

print(f"Paarisarvude arv: {paaris}")
print(f"Paaritute arvude arv: {paaritu}")



#7
for i in range(5):
    number=randint(0,9)
    print(number, end="")
print()







#5















#4
korrutamine=1
for i in range(1,11):
    tulemus=(i)*1
    print(f"{i}*1={tulemus}")




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
    
