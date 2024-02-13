spisok=[] #pustoy spisok
numbers=[1,2,3,4,5]
abc=["Abc","B","C"]
slovo="Programmeerimine"
slovo_list=list(slovo)
print(slovo)
print(slovo_list)
while True:
    print("1-добавить букву в список\n2-склеить списки\n3-длбавить бкукву на -i позицию\n4-показать функцию isspace\n5-удалить букву\n6-показать функцию istitle\n7-показать функцию upper\n8-показать функцию isdigit\n9-показать функцию title\n10-показать функцию isalnum\n11-показать функцию capitalize\n12-показать функцию lower\n13-показать функцию isalpha\n14-показать функцию swapcase\n15-показать функцию islower\n")
    valik=int(input())
    if valik==1:
        a=input("Введи букву")
        slovo_list.append(a)
        print(f"Добавили {a} новый список, ",slovo_list)
    elif valik==2:
        slovo_list.extend(abc)
        print(slovo_list)
    elif valik==3:
        a=input("Введи букву, которую хочешь добавить ")
        i=int(input("Введи номер позиции, куда хочешь добавить букву"))
        slovo_list.insert(i-1,a)
        print(slovo_list)
    elif valik==4:
        example_code=""
        print(slovo_list)
        s=input("Что вы хотите ввести?")
        result=s.isspace()
        print(example_code)
        print(result)
    elif valik==5:
        a=input("Введи букву, которую хочешь удалить")
        n=slovo_list.count(a)
        if n>0:
           for i in range(n):
                slovo_list.remove(a)
           else:
            print("Искомой буквы нет")
    elif valik==6:
        a=input("Введи слово или букву с заглавной буквы\n")
        t=a.istitle()
        print(a)
    elif valik==7:
        a=input("Введите слово или букву\n")
        r=a.upper()
        print(r)
    elif valik==8:
        a=input("Введите набор цифр\n")
        k=a.isdigit()
        print(k)
    elif valik==9:
        a=input("Введите слово или набор букв с маленькой и большой буквы\n")
        l=a.title()
        print(l)
    elif valik==10:
        a=input("Введите буквы или цифры\n")
        k=a.isalnum()
        print(k)
    elif valik==11:
        a=input("Введите слово\n")
        k=a.capitalize()
        print(k)
    elif valik==12:
        a=input("Введите слово\n")
        k=a.lower()
        print(k)
    elif valik==13:
        a=input("Введите слово\n")
        k=a.isalpha()
        print(k)
    elif valik==14:
        a=input("Введите слово\n")
        k=a.swapcase()
        print(k)
    elif valik==15:
        a=input("Введите слово\n")
        k=a.islower()
        print(k)

           








##isalnum()
##isalnum() kasutatakse stringi kontrollimiseks, kas string sisaldab tähti ja numbreid või mitte
##Valik 1, kus string koosneb tähtedest ja numbritest 
#a1="Tere1234"
#e=a1.isalnum()
#print(e)
##Valik 2, kus string koosneb tähtedest, numbritest ja muudest sümbolitest 
#a2="Tere1234€@&$"
#c= a2.isalnum()
#print(c)








##isalpha()
##isalpha kasutatakse stringi kontrollimiseks, st kas string sisaldab tähti või mitte, ja pole vahet, kas täht on suur või väike 
##Valik 1, kus string sisaldab ainult tähti 
#p1="Tere"
#t=p1.isalpha()
#print(t)
##Variant 2, kus string sisaldab tähti ja numbreid 
#p2="Tere1234!"
#u=p2.isalpha()
#print(u)





##isdigit()
##isdigit() kasutatakse stringi kontrollimiseks, st selle, kas string sisaldab numbreid või mitte
##Valik 1, kus rida koosneb ainult numbritest
#v1="12345"
#l= v1.isdigit()
#print(l)
##Valik 2, kus rida koosneb numbritest ja tähtedest
#v2="123abc"
#i= v2.isdigit()
#print(i)




##S1*3
##S1*3 kasutatakse stringi kordamiseks määratud arv kordi
#S1="Tere hommikust!"
#r=S1*3
#print(r)







##S1+S2
##S1+S2 ühendab kaks stringi üheks
#s1="Tere, "
#s2="hommikust!"
#b=s1+s2
#print(b)





##swapcase()
##swapcase() muudab kõik väikesed tähed suurtähtedeks ja kõik suured tähed väikesteks tähtedeks
#m="TeRe HoMmIkUsT".swapcase()
#print(m)







##title()
##title() Iga sõna esimene täht teisendatakse suureks ja kõik ülejäänud väikeste tähtedega
#v="Tere hommikust".title()
#print(v)






##upper()
##upper() teisendab väikesed tähed suurtähtedeks
#n="Tere hommikust".upper()
#print(n)





##lower()
##Kui kirjutate sõna suurtähtedega, muudab lower() sõna esimese tähe väikeseks
#while True:
#    v=input("Tahan komme!").lower()
#    if v=="komm": break





##capitalize() 
##Kui kirjutate sõna väikese algustähega, muudab capitalize() sõna esimese tähe suureks
#nimi=input("Mis on sinu nimi?").capitalize()
#mitu=int(input("Mitu korda tervistada?"))
#for i in range(1,mitu+1):
#    print("Ole tervitatud, "+nimi+", "+str(i)+". korda.")