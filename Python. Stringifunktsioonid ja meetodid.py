#S1+S2
#S1+S2 ühendab kaks stringi üheks
s1="Tere, "
s2="hommikust!"
b=s1+s2
print(b)





#swapcase()
#swapcase() muudab kõik väikesed tähed suurtähtedeks ja kõik suured tähed väikesteks tähtedeks
m="TeRe HoMmIkUsT".swapcase()
print(m)







#title()
#title() Iga sõna esimene täht teisendatakse suureks ja kõik ülejäänud väikeste tähtedega
v="Tere hommikust".title()
print(v)






#upper()
#upper() teisendab väikesed tähed suurtähtedeks
n="Tere hommikust".upper()
print(n)





#lower()
#Kui kirjutate sõna suurtähtedega, muudab lower() sõna esimese tähe väikeseks
while True:
    v=input("Tahan komme!").lower()
    if v=="komm": break





#capitalize() 
#Kui kirjutate sõna väikese algustähega, muudab capitalize() sõna esimese tähe suureks
nimi=input("Mis on sinu nimi?").capitalize()
mitu=int(input("Mitu korda tervistada?"))
for i in range(1,mitu+1):
    print("Ole tervitatud, "+nimi+", "+str(i)+". korda.")
